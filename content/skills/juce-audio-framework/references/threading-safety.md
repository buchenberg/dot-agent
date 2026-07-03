# JUCE Threading & Real-Time Safety

## Critical Rules for processBlock

| Rule | Reason |
|------|--------|
| **No allocations** | `new`, `malloc`, `std::vector::push_back`, `String` creation cause heap operations |
| **No locks** | `ScopedLock`, `std::mutex`, `CriticalSection` can block the audio thread |
| **No I/O** | File reads, network calls, `Logger::writeToLog` cause unpredictable latency |
| **No GUI updates** | `repaint()`, `setSize()`, `Label::setText()` must only run on message thread |

## Safe Cross-Thread Communication

### Audio → GUI (atomic or lock-free queue)

```cpp
std::atomic<float> currentLevel { 0.0f };  // set in processBlock, read in Timer
```

### GUI → Audio (atomic parameters)

```cpp
std::atomic<bool> shouldReset { false };
```

### Complex data: lock-free ring buffer

```cpp
// juce::AbstractFifo for managing read/write positions
// juce::dsp::FixedSizeFunction for deferred callbacks
```

## ScopedNoDenormals

Always use at the top of processBlock to prevent denormalized float performance hit:

```cpp
void processBlock (AudioBuffer<float>& buffer, MidiBuffer& midi) override
{
    juce::ScopedNoDenormals noDenormals;
    // ...
}
```

## MessageManager::callAsync

To trigger GUI updates from non-GUI threads:

```cpp
// From audio thread or any background thread
juce::MessageManager::callAsync ([this, level]
{
    levelMeter.setLevel (level);  // safe: runs on message thread
});
```

## Timer for Periodic GUI Updates

```cpp
class MyEditor : public juce::AudioProcessorEditor,
                 private juce::Timer
{
public:
    MyEditor (MyProcessor& p) : AudioProcessorEditor (&p)
    {
        startTimerHz (30);  // 30 Hz GUI update rate
    }

    void timerCallback() override
    {
        // Read atomic values set by audio thread
        auto level = processor.currentLevel.load();
        levelMeter.setLevel (level);
    }
};
```

## AudioProcessorValueTreeState Thread Safety

APVTS parameters are thread-safe for reading/writing via the host:
- `AudioParameterFloat::get()` — atomic read, returns actual float value
- `setValueNotifyingHost()` — atomic write, notifies host

For non-parameter state, use `SpinLock` or lock-free queues.

## Real-Time Allocation Patterns

### Pre-allocate in prepareToPlay

```cpp
void prepareToPlay (double sr, int blockSize) override
{
    // Allocate everything you'll need in processBlock
    tempBuffer.setSize (getTotalNumOutputChannels(), blockSize);
    delayBuffer.setSize (getTotalNumOutputChannels(), (int) sr * 2);
    delayBuffer.clear();
}
```

### Use std::array instead of std::vector

```cpp
// Bad: may allocate in processBlock
std::vector<float> samples;
samples.push_back (sample);

// Good: fixed-size, no allocation
std::array<float, 1024> samples;
```

### Reuse objects

```cpp
// Bad: creates new object each call
void processBlock (AudioBuffer<float>& buffer, MidiBuffer&) override
{
    juce::dsp::AudioBlock<float> block (buffer);  // OK: lightweight, no allocation
    juce::String name = "test";  // BAD: allocates
}

// Good: member variable, reused
class MyProcessor : public AudioProcessor
{
    juce::dsp::Oversampling<float> oversampling { 2, 3, /* ... */ };
};
```
