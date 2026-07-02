# JUCE Audio Utilities — SmoothedValue, AbstractFifo, AudioPlayHead, MidiMessageCollector

## SmoothedValue — Parameter Smoothing

Prevents audio glitches when parameters change. Smoothly ramps from current value to target.

### Template Parameters

```cpp
// Linear ramp (for gain, pan, etc.)
juce::SmoothedValue<float, juce::ValueSmoothingTypes::Linear> linearSmooth;

// Multiplicative/exponential ramp (for frequency, dB — never reaches zero)
juce::SmoothedValue<float, juce::ValueSmoothingTypes::Multiplicative> logSmooth;
```

### Key Methods

```cpp
// Initialize (call in prepareToPlay)
smooth.reset (sampleRate, 0.05);  // 50ms ramp time
smooth.setCurrentAndTargetValue (0.7f);  // snap to initial value

// Set new target (from parameter callback or processBlock)
smooth.setTargetValue (newParameterValue);

// Per-sample usage in processBlock
for (int i = 0; i < numSamples; ++i)
{
    float gain = smooth.getNextValue();  // call once per sample
    buffer.setSample (ch, i, buffer.getSample (ch, i) * gain);
}

// Or use the convenience method
smooth.applyGain (buffer.getWritePointer (ch), numSamples);

// Query
bool ramping = smooth.isSmoothing();
float current = smooth.getCurrentValue();
float target = smooth.getTargetValue();

// Fast-forward without per-sample calls
float value = smooth.skip (numSamples);  // returns final value
```

### Usage in Plugin

```cpp
class MyProcessor : public juce::AudioProcessor
{
    juce::SmoothedValue<float> smoothedGain;

    void prepareToPlay (double sr, int bs) override
    {
        smoothedGain.reset (sr, 0.02);  // 20ms ramp
        smoothedGain.setCurrentAndTargetValue (*gainParam);
    }

    void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer&) override
    {
        smoothedGain.setTargetValue (*gainParam);
        smoothedGain.applyGain (buffer);
    }
};
```

---

## AbstractFifo — Lock-Free FIFO

Single-reader, single-writer lock-free FIFO. Does NOT hold data — manages positions in your own buffer.

### Construction

```cpp
juce::AbstractFifo fifo (1024);  // capacity = 1023 (one slot reserved)
```

### Scoped API (preferred)

```cpp
// Writer side (e.g., audio thread)
{
    auto scope = fifo.write (numItems);  // ScopedWrite
    if (scope.blockSize1 > 0)
        std::memcpy (buffer.data() + scope.startIndex1, data, scope.blockSize1 * sizeof(float));
    if (scope.blockSize2 > 0)
        std::memcpy (buffer.data() + scope.startIndex2, data + scope.blockSize1, scope.blockSize2 * sizeof(float));
}

// Reader side (e.g., GUI thread)
{
    auto scope = fifo.read (numWanted);  // ScopedRead
    if (scope.blockSize1 > 0)
        std::memcpy (output, buffer.data() + scope.startIndex1, scope.blockSize1 * sizeof(float));
    if (scope.blockSize2 > 0)
        std::memcpy (output + scope.blockSize1, buffer.data() + scope.startIndex2, scope.blockSize2 * sizeof(float));
}
```

### Manual API

```cpp
// Write
int start1, size1, start2, size2;
fifo.prepareToWrite (numToWrite, start1, size1, start2, size2);
if (size1 > 0) { /* write to buffer[start1..start1+size1] */ }
if (size2 > 0) { /* write to buffer[start2..start2+size2] */ }
fifo.finishedWrite (size1 + size2);

// Read
fifo.prepareToRead (numWanted, start1, size1, start2, size2);
if (size1 > 0) { /* read from buffer[start1..start1+size1] */ }
if (size2 > 0) { /* read from buffer[start2..start2+size2] */ }
fifo.finishedRead (size1 + size2);
```

### Query

```cpp
int free = fifo.getFreeSpace();
int ready = fifo.getNumReady();
int total = fifo.getTotalSize();
fifo.reset();  // clear all
```

---

## AudioPlayHead — Host Transport Info

Provides transport state (playing, recording, BPM, time signature, position) from the host DAW.

### Usage in processBlock

```cpp
void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midi) override
{
    if (auto* playHead = getPlayHead())
    {
        if (auto position = playHead->getPosition())
        {
            bool isPlaying   = position->getIsPlaying();
            bool isRecording = position->getIsRecording();
            double bpm       = position->getBpm().orFallback (120.0);
            double timeSigN  = position->getTimeSignature().orFallback ({ 4, 4 }).numerator;
            double timeSigD  = position->getTimeSignature().orFallback ({ 4, 4 }).denominator;
            double ppq       = position->getPpqPosition().orFallback (0.0);
            double barStart  = position->getPpqPositionOfLastBarStart().orFallback (0.0);

            // Use transport info for tempo-synced effects, LFOs, etc.
        }
    }
}
```

### PositionInfo Key Methods

```cpp
position->getIsPlaying()         // bool
position->getIsRecording()       // bool
position->getBpm()               // Optional<double>
position->getTimeSignature()     // Optional<TimeSignature>
position->getPpqPosition()       // Optional<double> — pulses per quarter note
position->getPpqPositionOfLastBarStart()  // Optional<double>
position->getFrameRate()         // Optional<FrameRate>
position->getLoopPoints()        // Optional<LoopPoints>
position->getEditOriginTime()    // Optional<double>
position->getBarCount()          // Optional<int>
position->getIsLooping()         // bool
```

### Controlling Transport (if supported)

```cpp
if (auto* playHead = getPlayHead())
{
    if (playHead->canControlTransport())
    {
        playHead->transportPlay (true);   // start
        playHead->transportPlay (false);  // stop
        playHead->transportRewind();
        playHead->transportRecord (true); // arm recording
    }
}
```

---

## MidiMessageCollector — MIDI Buffer Management

Collects realtime MIDI messages and delivers them as timestamped blocks aligned with audio callbacks.

### Setup

```cpp
juce::MidiMessageCollector collector;

void prepareToPlay (double sr, int) override
{
    collector.reset (sr);
    collector.ensureStorageAllocated (512);  // pre-allocate
}
```

### Receiving MIDI (from MidiInput callback or keyboard)

```cpp
void handleIncomingMidiMessage (juce::MidiInput*, const juce::MidiMessage& msg) override
{
    collector.addMessageToQueue (msg);  // thread-safe with removeNextBlockOfMessages
}
```

### Processing in processBlock

```cpp
void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages) override
{
    juce::MidiBuffer incomingMidi;
    collector.removeNextBlockOfMessages (incomingMidi, buffer.getNumSamples());

    // incomingMidi now has timestamps 0..numSamples-1
    for (const auto metadata : incomingMidi)
    {
        auto msg = metadata.getMessage();
        int samplePosition = metadata.samplePosition;
        // process MIDI event at exact sample position
    }
}
```

### Key Methods

```cpp
void reset (double sampleRate);                              // clear + set rate
void addMessageToQueue (const MidiMessage&);                 // realtime input
void removeNextBlockOfMessages (MidiBuffer&, int numSamples); // get block
void ensureStorageAllocated (size_t bytes);                  // pre-allocate
```

---

## ChangeBroadcaster / ChangeListener — Observer Pattern

Asynchronous notification when something changes (e.g., file loaded, thumbnail ready).

```cpp
// Broadcaster (the thing that changes)
class MyDataSource : public juce::ChangeBroadcaster
{
    void loadData()
    {
        // ... load data ...
        sendChangeMessage();  // async notification to all listeners
    }
};

// Listener (wants to know about changes)
class MyComponent : public juce::Component, private juce::ChangeListener
{
    MyComponent (MyDataSource& source) : dataSource (source)
    {
        dataSource.addChangeListener (this);
    }

    ~MyComponent() override
    {
        dataSource.removeChangeListener (this);
    }

    void changeListenerCallback (juce::ChangeBroadcaster*) override
    {
        repaint();  // refresh UI
    }

    MyDataSource& dataSource;
};
```

## AsyncUpdater — Coalesced Async Callback

Posts a callback to the message thread. Multiple `triggerAsyncUpdate()` calls coalesce into one callback.

```cpp
class MyComponent : public juce::Component, private juce::AsyncUpdater
{
    void parameterChanged()
    {
        triggerAsyncUpdate();  // may block (posts to queue) — avoid from audio thread
    }

    void handleAsyncUpdate() override
    {
        // Runs once on message thread, even if triggerAsyncUpdate() was called 100 times
        updateUI();
    }
};
```

**WARNING**: `triggerAsyncUpdate()` may block. Use `MessageManager::callAsync` from the audio thread instead.

## Interpolators — Resampling

For sample-rate conversion or variable-speed playback:

```cpp
// High quality (200-point windowed sinc)
juce::Interpolators::WindowedSinc interpolator;

// Medium quality (4-point Lagrange)
juce::Interpolators::Lagrange lagrange;

// Lower quality, lower latency
juce::Interpolators::Linear linear;

// Zero-order hold (sample-and-hold)
juce::Interpolators::ZeroOrderHold zoh;
```

Usage:

```cpp
interpolator.reset (sourceSampleRate / targetSampleRate);  // ratio
interpolator.process (ratio, inputSamples, outputSamples, numOutputSamples);
```
