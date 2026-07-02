# JUCE DSP Module — Complete Reference

The `juce_dsp` module provides composable audio processing building blocks.

## ProcessSpec

All DSP processors are configured with a `ProcessSpec`:

```cpp
juce::dsp::ProcessSpec spec;
spec.sampleRate = sampleRate;
spec.maximumBlockSize = (juce::uint32) maxBlockSize;
spec.numChannels = (juce::uint32) getMainBusNumOutputChannels();
```

## AudioBlock

A lightweight, non-owning view over audio data:

```cpp
juce::dsp::AudioBlock<float> block (buffer);  // wraps AudioBuffer
auto numCh = block.getNumChannels();
auto numSamp = block.getNumSamples();
float* leftChannel = block.getChannelPointer (0);
auto subBlock = block.getSubsetChannelBlock (0, 2);  // first 2 channels
```

## ProcessContext

Wraps an AudioBlock with processing metadata:

```cpp
// In-place processing (input and output share the same buffer)
juce::dsp::ProcessContextReplacing<float> context (block);

// Separate input/output buffers
juce::dsp::ProcessContextNonReplacing<float> context (inputBlock, outputBlock);
```

## ProcessorChain

Compose processors in series:

```cpp
using MyChain = juce::dsp::ProcessorChain<
    juce::dsp::NoiseGate<float>,       // index 0
    juce::dsp::Gain<float>,            // index 1
    juce::dsp::Compressor<float>,      // index 2
    juce::dsp::LadderFilter<float>,    // index 3
    juce::dsp::Limiter<float>,         // index 4
    juce::dsp::Panner<float>           // index 5
>;

MyChain chain;

// In prepareToPlay:
chain.prepare (spec);

// Access individual processors by index:
auto& gate = chain.get<0>();
gate.setThreshold (-20.0f);
gate.setRatio (0.1f);

auto& gain = chain.get<1>();
gain.setGainDecibels (-6.0f);

// In processBlock:
chain.process (context);

// Bypass individual processors:
chain.setBypassed<0> (shouldBypassGate);
```

## Key DSP Processors

| Processor | Purpose | Key Methods |
|-----------|---------|-------------|
| `dsp::Gain<T>` | Volume control | `setGainLinear()`, `setGainDecibels()` |
| `dsp::Compressor<T>` | Dynamic compression | `setThreshold()`, `setRatio()`, `setAttack()`, `setRelease()` |
| `dsp::Limiter<T>` | Peak limiting | `setThreshold()`, `setRelease()` |
| `dsp::NoiseGate<T>` | Noise gate | `setThreshold()`, `setRatio()`, `setAttack()`, `setRelease()` |
| `dsp::LadderFilter<T>` | Analog-modeled filter | `setCutoffFrequency()`, `setResonance()`, `setMode()` |
| `dsp::StateVariableFilter<T>` | SVF (LP/HP/BP/Notch) | `setCutoffFrequency()`, `setResonance()`, `setType()` |
| `dsp::IIR::Filter<T>` | Biquad IIR | `coefficients` (static design methods) |
| `dsp::Phaser<T>` | Phaser effect | `setRate()`, `setDepth()`, `setCentreFrequency()` |
| `dsp::Chorus<T>` | Chorus effect | `setRate()`, `setDepth()`, `setCentreDelay()`, `setFeedback()`, `setMix()` |
| `dsp::DelayLine<T, Interpolation>` | Delay line | `setDelay()`, `pushSample()`, `popSample()`, `setMaximumDelayInSamples()` |
| `dsp::Convolution` | Convolution reverb | `loadImpulseResponse()`, uses background thread |
| `dsp::Oscillator<T>` | Signal generator | `setFrequency()`, `initialise()` with waveform lambda |
| `dsp::DryWetMixer<T>` | Parallel blend | `setWetMixProportion()`, `pushDrySamples()`, `mixWetSamples()` |
| `dsp::Oversampling<T>` | Oversampling | `initProcessing()`, `processSamplesUp()`, `processSamplesDown()` |
| `dsp::Panner<T>` | Stereo panning | `setPan()`, `setRule()` |

## DelayLine Interpolation Types

```cpp
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::None>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Linear>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Lagrange3rd>
dsp::DelayLine<float, dsp::DelayLineInterpolationTypes::Thiran>
```

## Custom Processor Pattern

Any class with `prepare()`, `process()`, and `reset()` can go in a ProcessorChain:

```cpp
class MyEffect
{
public:
    void prepare (const juce::dsp::ProcessSpec& spec)
    {
        sampleRate = spec.sampleRate;
    }

    void reset() { /* clear internal state */ }

    template <typename ProcessContext>
    void process (const ProcessContext& context)
    {
        const auto& inputBlock  = context.getInputBlock();
        auto& outputBlock       = context.getOutputBlock();
        const auto numChannels  = outputBlock.getNumChannels();
        const auto numSamples   = outputBlock.getNumSamples();

        jassert (inputBlock.getNumChannels() == numChannels);
        jassert (inputBlock.getNumSamples() == numSamples);

        if (context.isBypassed)
        {
            outputBlock.copyFrom (inputBlock);
            return;
        }

        for (size_t ch = 0; ch < numChannels; ++ch)
        {
            auto* src = inputBlock.getChannelPointer (ch);
            auto* dst = outputBlock.getChannelPointer (ch);
            for (size_t i = 0; i < numSamples; ++i)
                dst[i] = /* your DSP here */ src[i];
        }
    }

private:
    double sampleRate = 44100.0;
};
```

## Convolution Reverb Pattern

```cpp
juce::dsp::Convolution convolution;

void prepareToPlay (double sr, int blockSize) override
{
    juce::dsp::ProcessSpec spec { sr, (juce::uint32) blockSize,
                                   (juce::uint32) getTotalNumOutputChannels() };
    convolution.prepare (spec);

    convolution.loadImpulseResponse (
        BinaryData::hall_wav, BinaryData::hall_wavSize,
        juce::dsp::Convolution::Stereo::yes,
        juce::dsp::Convolution::Trim::yes,
        juce::dsp::Convolution::Normalise::yes);
}
```

## Oversampling Pattern

```cpp
juce::dsp::Oversampling<float> oversampling (
    getTotalNumOutputChannels(),
    2,  // 2^2 = 4x oversampling
    juce::dsp::Oversampling<float>::filterHalfBandPolyphaseIIR,
    true);

void prepareToPlay (double sr, int blockSize) override
{
    oversampling.initProcessing ((size_t) blockSize);
    oversampling.reset();
}

void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer&) override
{
    juce::dsp::AudioBlock<float> block (buffer);
    auto osBlock = oversampling.processSamplesUp (block);
    // ... process at higher sample rate
    oversampling.processSamplesDown (block);
}

double getLatencySamples() const override
{
    return oversampling.getLatencyInSamples();
}
```
