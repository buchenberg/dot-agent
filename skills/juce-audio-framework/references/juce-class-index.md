# JUCE Class Index

> Auto-generated from JUCE doxygen docs. Use this table to find the right class for your task.
> Each "Docs" link points to the full API reference at docs.juce.com.
> To fetch a class doc on-demand: `web_fetch("https://docs.juce.com/master/<filename>")`

**823 classes** across **18 categories**

## Audio Core

| Class | Description | Docs |
|-------|-------------|------|
| `AiffAudioFormat` | Reads and Writes AIFF format audio files | [ref](https://docs.juce.com/master/classjuce_1_1AiffAudioFormat.html) |
| `AudioBuffer` | A multi-channel buffer containing floating point audio samples | [ref](https://docs.juce.com/master/classjuce_1_1AudioBuffer.html) |
| `AudioDeviceManager` | Manages the state of some audio and midi i/o devices | [ref](https://docs.juce.com/master/classjuce_1_1AudioDeviceManager.html) |
| `AudioDeviceSelectorComponent` | A component containing controls to let the user change the audio settings of an AudioDeviceManager object | [ref](https://docs.juce.com/master/classjuce_1_1AudioDeviceSelectorComponent.html) |
| `AudioFormat` | Subclasses of AudioFormat are used to read and write different audio file formats | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormat.html) |
| `AudioFormatManager` | A class for keeping a list of available audio formats, and for deciding which one to use to open a given file | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatManager.html) |
| `AudioFormatReader` | Reads samples from an audio file stream | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatReader.html) |
| `AudioFormatReaderSource` | A type of AudioSource that will read from an AudioFormatReader | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatReaderSource.html) |
| `AudioFormatWriter` | Writes samples to an audio file stream | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatWriter.html) |
| `AudioFormatWriter::ThreadedWriter` | Provides a FIFO for an AudioFormatWriter, allowing you to push incoming data into a buffer which will be flushed to d... | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatWriter_1_1ThreadedWriter.html) |
| `AudioFormatWriter::ThreadedWriter::IncomingDataReceiver` | Receiver for incoming data | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatWriter_1_1ThreadedWriter_1_1IncomingDataReceiver.html) |
| `AudioFormatWriterOptions` | Options that affect the output data format produced by an AudioFormatWriter | [ref](https://docs.juce.com/master/classjuce_1_1AudioFormatWriterOptions.html) |
| `AudioParameterBool` | Provides a class of AudioProcessorParameter that can be used as a boolean value | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterBool.html) |
| `AudioParameterBoolAttributes` | Properties of an AudioParameterBool | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterBoolAttributes.html) |
| `AudioParameterChoice` | Provides a class of AudioProcessorParameter that can be used to select an indexed, named choice from a list | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterChoice.html) |
| `AudioParameterChoiceAttributes` | Properties of an AudioParameterChoice | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterChoiceAttributes.html) |
| `AudioParameterFloat` | A subclass of AudioProcessorParameter that provides an easy way to create a parameter which maps onto a given Normali... | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterFloat.html) |
| `AudioParameterFloatAttributes` | Properties of an AudioParameterFloat | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterFloatAttributes.html) |
| `AudioParameterInt` | Provides a class of AudioProcessorParameter that can be used as an integer value with a given range | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterInt.html) |
| `AudioParameterIntAttributes` | Properties of an AudioParameterInt | [ref](https://docs.juce.com/master/classjuce_1_1AudioParameterIntAttributes.html) |
| `AudioPlayHead` | A subclass of AudioPlayHead can supply information about the position and status of a moving play head during audio p... | [ref](https://docs.juce.com/master/classjuce_1_1AudioPlayHead.html) |
| `AudioPlayHead::FrameRate` | More descriptive frame rate type | [ref](https://docs.juce.com/master/classjuce_1_1AudioPlayHead_1_1FrameRate.html) |
| `AudioPlayHead::PositionInfo` | Describes the time at the start of the current audio callback | [ref](https://docs.juce.com/master/classjuce_1_1AudioPlayHead_1_1PositionInfo.html) |
| `AudioPluginExtensions::VSTClient::ExtraFunctions` | Base class for some extra functions that can be attached to a VST plugin instance | [ref](https://docs.juce.com/master/classjuce_1_1AudioPluginExtensions_1_1VSTClient_1_1ExtraFunctions.html) |
| `AudioPluginFormat` | The base class for a type of plugin format, such as VST, AudioUnit, LADSPA, etc | [ref](https://docs.juce.com/master/classjuce_1_1AudioPluginFormat.html) |
| `AudioPluginFormatManager` | This maintains a list of known AudioPluginFormats | [ref](https://docs.juce.com/master/classjuce_1_1AudioPluginFormatManager.html) |
| `AudioPluginInstance` | Base class for an active instance of a plugin | [ref](https://docs.juce.com/master/classjuce_1_1AudioPluginInstance.html) |
| `AudioProcessor` | Base class for audio processing classes or plugins | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessor.html) |
| `AudioProcessor::Bus` | Describes the layout and properties of an audio bus | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessor_1_1Bus.html) |
| `AudioProcessor::ParameterChangeForwarder` |  | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessor_1_1ParameterChangeForwarder.html) |
| `AudioProcessorEditor` | Base class for the component that acts as the GUI for an AudioProcessor | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorEditor.html) |
| `AudioProcessorGraph` | A type of AudioProcessor which plays back a graph of other AudioProcessors | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorGraph.html) |
| `AudioProcessorGraph::AudioGraphIOProcessor` | A special type of AudioProcessor that can live inside an AudioProcessorGraph in order to use the audio that comes int... | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorGraph_1_1AudioGraphIOProcessor.html) |
| `AudioProcessorGraph::Node` | Represents one of the nodes, or processors, in an AudioProcessorGraph | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorGraph_1_1Node.html) |
| `AudioProcessorGraph::NodeAndChannel` | Represents an input or output channel of a node in an AudioProcessorGraph | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorGraph_1_1NodeAndChannel.html) |
| `AudioProcessorListener` | Base class for listeners that want to know about changes to an AudioProcessor | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorListener.html) |
| `AudioProcessorParameter` | An abstract base class for parameter objects that can be added to an AudioProcessor | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameter.html) |
| `AudioProcessorParameter::Listener` | A base class for listeners that want to know about changes to an AudioProcessorParameter | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameter_1_1Listener.html) |
| `AudioProcessorParameterGroup` | A class encapsulating a group of AudioProcessorParameters and nested AudioProcessorParameterGroups | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameterGroup.html) |
| `AudioProcessorParameterGroup::AudioProcessorParameterNode` | A child of an AudioProcessorParameterGroup | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameterGroup_1_1AudioProcessorParameterNode.html) |
| `AudioProcessorParameterWithID` | This abstract base class is used by some AudioProcessorParameter helper classes | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameterWithID.html) |
| `AudioProcessorParameterWithIDAttributes` | An instance of this class may be passed to the constructor of an AudioProcessorParameterWithID to set optional charac... | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorParameterWithIDAttributes.html) |
| `AudioProcessorPlayer` | An AudioIODeviceCallback object which streams audio through an AudioProcessor | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorPlayer.html) |
| `AudioProcessorValueTreeState` | This class contains a ValueTree that is used to manage an AudioProcessor's entire state | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState.html) |
| `AudioProcessorValueTreeState::ButtonAttachment` | An object of this class maintains a connection between a Button and a parameter in an AudioProcessorValueTreeState | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState_1_1ButtonAttachment.html) |
| `AudioProcessorValueTreeState::ComboBoxAttachment` | An object of this class maintains a connection between a ComboBox and a parameter in an AudioProcessorValueTreeState | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState_1_1ComboBoxAttachment.html) |
| `AudioProcessorValueTreeState::Parameter` | A parameter class that maintains backwards compatibility with deprecated AudioProcessorValueTreeState functionality | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState_1_1Parameter.html) |
| `AudioProcessorValueTreeState::ParameterLayout` | A class to contain a set of RangedAudioParameters and AudioProcessorParameterGroups containing RangedAudioParameters | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState_1_1ParameterLayout.html) |
| `AudioProcessorValueTreeState::SliderAttachment` | An object of this class maintains a connection between a Slider and a parameter in an AudioProcessorValueTreeState | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeState_1_1SliderAttachment.html) |
| `AudioProcessorValueTreeStateParameterAttributes` | Advanced properties of an AudioProcessorValueTreeState::Parameter | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorValueTreeStateParameterAttributes.html) |
| `AudioSource` | Base class for objects that can produce a continuous stream of audio | [ref](https://docs.juce.com/master/classjuce_1_1AudioSource.html) |
| `AudioSourcePlayer` | Wrapper class to continuously stream audio from an audio source to an AudioIODevice | [ref](https://docs.juce.com/master/classjuce_1_1AudioSourcePlayer.html) |
| `AudioThumbnail` | Makes it easy to quickly draw scaled views of the waveform shape of an audio file | [ref](https://docs.juce.com/master/classjuce_1_1AudioThumbnail.html) |
| `AudioThumbnailBase` | Provides a base for classes that can store and draw scaled views of an audio waveform | [ref](https://docs.juce.com/master/classjuce_1_1AudioThumbnailBase.html) |
| `AudioThumbnailCache` | An instance of this class is used to manage multiple AudioThumbnail objects | [ref](https://docs.juce.com/master/classjuce_1_1AudioThumbnailCache.html) |
| `AudioTransportSource` | An AudioSource that takes a PositionableAudioSource and allows it to be played, stopped, started, etc | [ref](https://docs.juce.com/master/classjuce_1_1AudioTransportSource.html) |
| `AudioVisualiserComponent` | A simple component that can be used to show a scrolling waveform of audio data | [ref](https://docs.juce.com/master/classjuce_1_1AudioVisualiserComponent.html) |
| `AudioWorkgroup` | A handle to an audio workgroup, which is a collection of realtime threads working together to produce audio by a comm... | [ref](https://docs.juce.com/master/classjuce_1_1AudioWorkgroup.html) |
| `BufferingAudioSource` | An AudioSource which takes another source as input, and buffers it using a thread | [ref](https://docs.juce.com/master/classjuce_1_1BufferingAudioSource.html) |
| `ChannelRemappingAudioSource` | An AudioSource that takes the audio from another source, and re-maps its input and output channels to a different arr... | [ref](https://docs.juce.com/master/classjuce_1_1ChannelRemappingAudioSource.html) |
| `CoreAudioFormat` | OSX and iOS only - This uses the AudioToolbox framework to read any audio format that the system has a codec for | [ref](https://docs.juce.com/master/classjuce_1_1CoreAudioFormat.html) |
| `FlacAudioFormat` | Reads and writes the lossless-compression FLAC audio format | [ref](https://docs.juce.com/master/classjuce_1_1FlacAudioFormat.html) |
| `GenericAudioProcessorEditor` | A type of UI component that displays the parameters of an AudioProcessor as a simple list of sliders, combo boxes and... | [ref](https://docs.juce.com/master/classjuce_1_1GenericAudioProcessorEditor.html) |
| `IIRFilterAudioSource` | An AudioSource that performs an IIR filter on another source | [ref](https://docs.juce.com/master/classjuce_1_1IIRFilterAudioSource.html) |
| `LAMEEncoderAudioFormat` | An AudioFormat class which can use an installed version of the LAME mp3 encoder to encode a file | [ref](https://docs.juce.com/master/classjuce_1_1LAMEEncoderAudioFormat.html) |
| `LegacyAudioParameter` |  | [ref](https://docs.juce.com/master/classjuce_1_1LegacyAudioParameter.html) |
| `LegacyAudioParametersWrapper` |  | [ref](https://docs.juce.com/master/classjuce_1_1LegacyAudioParametersWrapper.html) |
| `MP3AudioFormat` | Software-based MP3 decoding format (doesn't currently provide an encoder) | [ref](https://docs.juce.com/master/classjuce_1_1MP3AudioFormat.html) |
| `MemoryAudioSource` | An AudioSource which takes some float audio data as an input | [ref](https://docs.juce.com/master/classjuce_1_1MemoryAudioSource.html) |
| `MemoryMappedAudioFormatReader` | A specialised type of AudioFormatReader that uses a MemoryMappedFile to read directly from an audio file | [ref](https://docs.juce.com/master/classjuce_1_1MemoryMappedAudioFormatReader.html) |
| `MixerAudioSource` | An AudioSource that mixes together the output of a set of other AudioSources | [ref](https://docs.juce.com/master/classjuce_1_1MixerAudioSource.html) |
| `OggVorbisAudioFormat` | Reads and writes the Ogg-Vorbis audio format | [ref](https://docs.juce.com/master/classjuce_1_1OggVorbisAudioFormat.html) |
| `PositionableAudioSource` | A type of AudioSource which can be repositioned | [ref](https://docs.juce.com/master/classjuce_1_1PositionableAudioSource.html) |
| `RangedAudioParameter` | This abstract base class is used by some AudioProcessorParameter helper classes | [ref](https://docs.juce.com/master/classjuce_1_1RangedAudioParameter.html) |
| `RangedAudioParameterAttributes` |  | [ref](https://docs.juce.com/master/classjuce_1_1RangedAudioParameterAttributes.html) |
| `ResamplingAudioSource` | A type of AudioSource that takes an input source and changes its sample rate | [ref](https://docs.juce.com/master/classjuce_1_1ResamplingAudioSource.html) |
| `ReverbAudioSource` | An AudioSource that uses the Reverb class to apply a reverb to another AudioSource | [ref](https://docs.juce.com/master/classjuce_1_1ReverbAudioSource.html) |
| `ToneGeneratorAudioSource` | A simple AudioSource that generates a sine wave | [ref](https://docs.juce.com/master/classjuce_1_1ToneGeneratorAudioSource.html) |
| `WavAudioFormat` | Reads and Writes WAV format audio files | [ref](https://docs.juce.com/master/classjuce_1_1WavAudioFormat.html) |
| `WindowsMediaAudioFormat` | Audio format which uses the Windows Media codecs (Windows only) | [ref](https://docs.juce.com/master/classjuce_1_1WindowsMediaAudioFormat.html) |

## DSP

| Class | Description | Docs |
|-------|-------------|------|
| `dsp::AudioBlock` | Minimal and lightweight data-structure which contains a list of pointers to channels containing some kind of sample data | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1AudioBlock.html) |
| `dsp::BallisticsFilter` | A processor to apply standard attack / release ballistics to an input signal | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1BallisticsFilter.html) |
| `dsp::Bias` | Adds a DC offset (voltage bias) to the audio samples | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Bias.html) |
| `dsp::Chorus` | A simple chorus DSP widget that modulates the delay of a delay line in order to create sweeping notches in the magnit... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Chorus.html) |
| `dsp::Compressor` | A simple compressor with standard threshold, ratio, attack time and release time controls | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Compressor.html) |
| `dsp::Convolution` | Performs stereo partitioned convolution of an input signal with an impulse response in the frequency domain, using th... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Convolution.html) |
| `dsp::ConvolutionMessageQueue` | Used by the Convolution to dispatch engine-update messages on a background thread | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1ConvolutionMessageQueue.html) |
| `dsp::DelayLine` | A delay line processor featuring several algorithms for the fractional delay calculation, block processing, and sampl... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1DelayLine.html) |
| `dsp::DryWetMixer` | A processor to handle dry/wet mixing of two audio signals, where the wet signal may have additional latency | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1DryWetMixer.html) |
| `dsp::FFT` | Performs a fast fourier transform | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1FFT.html) |
| `dsp::FIR::Filter` | A processing class that can perform FIR filtering on an audio signal, in the time domain | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1FIR_1_1Filter.html) |
| `dsp::FirstOrderTPTFilter` | A first order filter class using the TPT (Topology-Preserving Transform) structure | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1FirstOrderTPTFilter.html) |
| `dsp::Gain` | Applies a gain to audio samples as single samples or AudioBlocks | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Gain.html) |
| `dsp::IIR::Filter` | A processing class that can perform IIR filtering on an audio signal, using the Transposed Direct Form II digital str... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1IIR_1_1Filter.html) |
| `dsp::LadderFilter` | Multi-mode filter based on the Moog ladder filter | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1LadderFilter.html) |
| `dsp::Limiter` | A simple limiter with standard threshold and release time controls, featuring two compressors and a hard clipper at 0 dB | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Limiter.html) |
| `dsp::LinkwitzRileyFilter` | A filter class designed to perform multi-band separation using the TPT (Topology-Preserving Transform) structure | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1LinkwitzRileyFilter.html) |
| `dsp::LogRampedValue` | Utility class for logarithmically smoothed linear values | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1LogRampedValue.html) |
| `dsp::LookupTable` | Class for efficiently approximating expensive arithmetic operations | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1LookupTable.html) |
| `dsp::LookupTableTransform` | Class for approximating expensive arithmetic operations | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1LookupTableTransform.html) |
| `dsp::Matrix` | General matrix and vectors class, meant for classic math manipulation such as additions, multiplications, and linear ... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Matrix.html) |
| `dsp::NoiseGate` | A simple noise gate with standard threshold, ratio, attack time and release time controls | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1NoiseGate.html) |
| `dsp::Oscillator` | Generates a signal based on a user-supplied function | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Oscillator.html) |
| `dsp::Oversampling` | A processor that performs multi-channel oversampling | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Oversampling.html) |
| `dsp::Panner` | A processor to perform panning operations on stereo buffers | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Panner.html) |
| `dsp::Phaser` | A 6 stage phaser that modulates first order all-pass filters to create sweeping notches in the magnitude frequency re... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Phaser.html) |
| `dsp::Polynomial` | A class representing a polynomial | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Polynomial.html) |
| `dsp::ProcessorChain` | This variadically-templated class lets you join together any number of processor classes into a single processor whic... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1ProcessorChain.html) |
| `dsp::Reverb` | Processor wrapper around juce::Reverb for easy integration into ProcessorChain | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1Reverb.html) |
| `dsp::StateVariableFilter::Filter` | An IIR filter that can perform low, band and high-pass filtering on an audio signal, with 12 dB of attenuation per oc... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1StateVariableFilter_1_1Filter.html) |
| `dsp::StateVariableTPTFilter` | An IIR filter that can perform low, band and high-pass filtering on an audio signal, with 12 dB of attenuation per oc... | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1StateVariableTPTFilter.html) |
| `dsp::WindowingFunction` | A class which provides multiple windowing functions useful for filter design and spectrum analyzers | [ref](https://docs.juce.com/master/classjuce_1_1dsp_1_1WindowingFunction.html) |

## MIDI/Synth

| Class | Description | Docs |
|-------|-------------|------|
| `BluetoothMidiDevicePairingDialogue` | Opens a Bluetooth MIDI pairing dialogue that allows the user to view and connect to Bluetooth MIDI devices that are c... | [ref](https://docs.juce.com/master/classjuce_1_1BluetoothMidiDevicePairingDialogue.html) |
| `MPEChannelAssigner` | This class handles the assignment of new MIDI notes to member channels of an active MPE zone | [ref](https://docs.juce.com/master/classjuce_1_1MPEChannelAssigner.html) |
| `MPEChannelRemapper` | This class handles the logic for remapping MIDI note messages from multiple MPE sources onto a specified MPE zone | [ref](https://docs.juce.com/master/classjuce_1_1MPEChannelRemapper.html) |
| `MPEInstrument` | This class represents an instrument handling MPE | [ref](https://docs.juce.com/master/classjuce_1_1MPEInstrument.html) |
| `MPEInstrument::Listener` | Derive from this class to be informed about any changes in the MPE notes played by this instrument, and any changes t... | [ref](https://docs.juce.com/master/classjuce_1_1MPEInstrument_1_1Listener.html) |
| `MPEKeyboardComponent` | A component that displays an MPE-compatible keyboard, whose notes can be clicked on | [ref](https://docs.juce.com/master/classjuce_1_1MPEKeyboardComponent.html) |
| `MPEMessages` | This helper class contains the necessary helper functions to generate MIDI messages that are exclusive to MPE, such a... | [ref](https://docs.juce.com/master/classjuce_1_1MPEMessages.html) |
| `MPESynthesiser` | Base class for an MPE-compatible musical device that can play sounds | [ref](https://docs.juce.com/master/classjuce_1_1MPESynthesiser.html) |
| `MPESynthesiserVoice` | Represents an MPE voice that an MPESynthesiser can use to play a sound | [ref](https://docs.juce.com/master/classjuce_1_1MPESynthesiserVoice.html) |
| `MPEValue` | This class represents a single value for any of the MPE dimensions of control | [ref](https://docs.juce.com/master/classjuce_1_1MPEValue.html) |
| `MPEZoneLayout` | This class represents the current MPE zone layout of a device capable of handling MPE | [ref](https://docs.juce.com/master/classjuce_1_1MPEZoneLayout.html) |
| `MPEZoneLayout::Listener` | Listener class | [ref](https://docs.juce.com/master/classjuce_1_1MPEZoneLayout_1_1Listener.html) |
| `MidiBuffer` | Holds a sequence of time-stamped midi events | [ref](https://docs.juce.com/master/classjuce_1_1MidiBuffer.html) |
| `MidiBufferIterator` | An iterator to move over contiguous raw MIDI data, which Allows iterating over a MidiBuffer using C++11 range-for syntax | [ref](https://docs.juce.com/master/classjuce_1_1MidiBufferIterator.html) |
| `MidiDataConcatenator` | Helper class that takes chunks of incoming midi bytes, packages them into messages, and dispatches them to a midi cal... | [ref](https://docs.juce.com/master/classjuce_1_1MidiDataConcatenator.html) |
| `MidiDeviceListConnection` | To find out when the available MIDI devices change, call MidiDeviceListConnection::make(), passing a lambda that will... | [ref](https://docs.juce.com/master/classjuce_1_1MidiDeviceListConnection.html) |
| `MidiFile` | Reads/writes standard midi format files | [ref](https://docs.juce.com/master/classjuce_1_1MidiFile.html) |
| `MidiInput` | Represents a midi input device using the old bytestream format | [ref](https://docs.juce.com/master/classjuce_1_1MidiInput.html) |
| `MidiInputCallback` | Receives incoming messages from a physical MIDI input device | [ref](https://docs.juce.com/master/classjuce_1_1MidiInputCallback.html) |
| `MidiKeyboardComponent` | A component that displays a piano keyboard, whose notes can be clicked on | [ref](https://docs.juce.com/master/classjuce_1_1MidiKeyboardComponent.html) |
| `MidiKeyboardState` | Represents a piano keyboard, keeping track of which keys are currently pressed | [ref](https://docs.juce.com/master/classjuce_1_1MidiKeyboardState.html) |
| `MidiKeyboardState::Listener` | Receives events from a MidiKeyboardState object | [ref](https://docs.juce.com/master/classjuce_1_1MidiKeyboardState_1_1Listener.html) |
| `MidiMessage` | Encapsulates a MIDI message | [ref](https://docs.juce.com/master/classjuce_1_1MidiMessage.html) |
| `MidiMessageCollector` | Collects incoming realtime MIDI messages and turns them into blocks suitable for processing by a block-based audio ca... | [ref](https://docs.juce.com/master/classjuce_1_1MidiMessageCollector.html) |
| `MidiMessageSequence` | A sequence of timestamped midi messages | [ref](https://docs.juce.com/master/classjuce_1_1MidiMessageSequence.html) |
| `MidiMessageSequence::MidiEventHolder` | Structure used to hold midi events in the sequence | [ref](https://docs.juce.com/master/classjuce_1_1MidiMessageSequence_1_1MidiEventHolder.html) |
| `MidiOutput` | Represents a midi output device using the old bytestream format | [ref](https://docs.juce.com/master/classjuce_1_1MidiOutput.html) |
| `MidiRPNDetector` | Parses a stream of MIDI data to assemble RPN and NRPN messages from their constituent MIDI CC messages | [ref](https://docs.juce.com/master/classjuce_1_1MidiRPNDetector.html) |
| `MidiRPNGenerator` | Generates an appropriate sequence of MIDI CC messages to represent an RPN or NRPN message | [ref](https://docs.juce.com/master/classjuce_1_1MidiRPNGenerator.html) |
| `Synthesiser` | Base class for a musical device that can play sounds | [ref](https://docs.juce.com/master/classjuce_1_1Synthesiser.html) |
| `SynthesiserSound` | Describes one of the sounds that a Synthesiser can play | [ref](https://docs.juce.com/master/classjuce_1_1SynthesiserSound.html) |
| `SynthesiserVoice` | Represents a voice that a Synthesiser can use to play a SynthesiserSound | [ref](https://docs.juce.com/master/classjuce_1_1SynthesiserVoice.html) |
| `VSTMidiEventList` | Holds a set of VSTMidiEvent objects and makes it easy to add events to the list | [ref](https://docs.juce.com/master/classjuce_1_1VSTMidiEventList.html) |

## GUI Widgets

| Class | Description | Docs |
|-------|-------------|------|
| `ActiveXControlComponent` | A Windows-specific class that can create and embed an ActiveX control inside itself | [ref](https://docs.juce.com/master/classjuce_1_1ActiveXControlComponent.html) |
| `AndroidViewComponent` | An Android-specific class that can create and embed a View inside itself | [ref](https://docs.juce.com/master/classjuce_1_1AndroidViewComponent.html) |
| `AnimatedAppComponent` | A base class for writing simple one-page graphical apps | [ref](https://docs.juce.com/master/classjuce_1_1AnimatedAppComponent.html) |
| `ArrowButton` | A button with an arrow in it | [ref](https://docs.juce.com/master/classjuce_1_1ArrowButton.html) |
| `AudioAppComponent` | A base class for writing audio apps that stream from the audio i/o devices | [ref](https://docs.juce.com/master/classjuce_1_1AudioAppComponent.html) |
| `BooleanPropertyComponent` | A PropertyComponent that contains an on/off toggle button | [ref](https://docs.juce.com/master/classjuce_1_1BooleanPropertyComponent.html) |
| `BorderedComponentBoundsConstrainer` | A ComponentBoundsConstrainer that can be used to add a constant border onto another ComponentBoundsConstrainer | [ref](https://docs.juce.com/master/classjuce_1_1BorderedComponentBoundsConstrainer.html) |
| `BubbleComponent` | A component for showing a message or other graphics inside a speech-bubble-shaped outline, pointing at a location on ... | [ref](https://docs.juce.com/master/classjuce_1_1BubbleComponent.html) |
| `BubbleMessageComponent` | A speech-bubble component that displays a short message | [ref](https://docs.juce.com/master/classjuce_1_1BubbleMessageComponent.html) |
| `BurgerMenuComponent` | A component which lists all menu items and groups them into categories by their respective parent menus | [ref](https://docs.juce.com/master/classjuce_1_1BurgerMenuComponent.html) |
| `Button` | A base class for buttons | [ref](https://docs.juce.com/master/classjuce_1_1Button.html) |
| `Button::Listener` | Used to receive callbacks when a button is clicked | [ref](https://docs.juce.com/master/classjuce_1_1Button_1_1Listener.html) |
| `ButtonParameterAttachment` | An object of this class maintains a connection between a Button and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1ButtonParameterAttachment.html) |
| `ButtonPropertyComponent` | A PropertyComponent that contains a button | [ref](https://docs.juce.com/master/classjuce_1_1ButtonPropertyComponent.html) |
| `ButtonTracker` | A class that automatically sends analytics events to the Analytics singleton when a button is clicked | [ref](https://docs.juce.com/master/classjuce_1_1ButtonTracker.html) |
| `CachedComponentImage` | Base class used internally for structures that can store cached images of component state | [ref](https://docs.juce.com/master/classjuce_1_1CachedComponentImage.html) |
| `CaretComponent` |  | [ref](https://docs.juce.com/master/classjuce_1_1CaretComponent.html) |
| `ChoicePropertyComponent` | A PropertyComponent that shows its value as a combo box | [ref](https://docs.juce.com/master/classjuce_1_1ChoicePropertyComponent.html) |
| `CodeEditorComponent` | A text editor component designed specifically for source code | [ref](https://docs.juce.com/master/classjuce_1_1CodeEditorComponent.html) |
| `ColourSelector` | A component that lets the user choose a colour | [ref](https://docs.juce.com/master/classjuce_1_1ColourSelector.html) |
| `ComboBox` | A component that lets the user choose from a drop-down list of choices | [ref](https://docs.juce.com/master/classjuce_1_1ComboBox.html) |
| `ComboBox::Listener` | A class for receiving events from a ComboBox | [ref](https://docs.juce.com/master/classjuce_1_1ComboBox_1_1Listener.html) |
| `ComboBoxParameterAttachment` | An object of this class maintains a connection between a ComboBox and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1ComboBoxParameterAttachment.html) |
| `Component` | The base class for all JUCE user-interface objects | [ref](https://docs.juce.com/master/classjuce_1_1Component.html) |
| `Component::BailOutChecker` | A class to keep an eye on a component and check for it being deleted | [ref](https://docs.juce.com/master/classjuce_1_1Component_1_1BailOutChecker.html) |
| `Component::Positioner` | Base class for objects that can be used to automatically position a component according to some kind of algorithm | [ref](https://docs.juce.com/master/classjuce_1_1Component_1_1Positioner.html) |
| `Component::SafePointer` | Holds a pointer to some type of Component, which automatically becomes null if the component is deleted | [ref](https://docs.juce.com/master/classjuce_1_1Component_1_1SafePointer.html) |
| `ComponentAnimator` | This class has been superseded, it is now recommended you use the Animator class in the juce_animation module | [ref](https://docs.juce.com/master/classjuce_1_1ComponentAnimator.html) |
| `ComponentBoundsConstrainer` | A class that imposes restrictions on a Component's size or position | [ref](https://docs.juce.com/master/classjuce_1_1ComponentBoundsConstrainer.html) |
| `ComponentBuilder` | Loads and maintains a tree of Components from a ValueTree that represents them | [ref](https://docs.juce.com/master/classjuce_1_1ComponentBuilder.html) |
| `ComponentBuilder::ImageProvider` | This class is used when references to images need to be stored in ValueTrees | [ref](https://docs.juce.com/master/classjuce_1_1ComponentBuilder_1_1ImageProvider.html) |
| `ComponentBuilder::TypeHandler` | The class is a base class for objects that manage the loading of a type of component from a ValueTree | [ref](https://docs.juce.com/master/classjuce_1_1ComponentBuilder_1_1TypeHandler.html) |
| `ComponentDragger` | An object to take care of the logic for dragging components around with the mouse | [ref](https://docs.juce.com/master/classjuce_1_1ComponentDragger.html) |
| `ComponentListener` | Gets informed about changes to a component's hierarchy or position | [ref](https://docs.juce.com/master/classjuce_1_1ComponentListener.html) |
| `ComponentMovementWatcher` | An object that watches for any movement of a component or any of its parent components | [ref](https://docs.juce.com/master/classjuce_1_1ComponentMovementWatcher.html) |
| `ComponentPeer` | The Component class uses a ComponentPeer internally to create and manage a real operating-system window | [ref](https://docs.juce.com/master/classjuce_1_1ComponentPeer.html) |
| `ComponentPeer::OptionalBorderSize` | Represents the window borders around a window component | [ref](https://docs.juce.com/master/classjuce_1_1ComponentPeer_1_1OptionalBorderSize.html) |
| `ComponentTraverser` | Base class for traversing components | [ref](https://docs.juce.com/master/classjuce_1_1ComponentTraverser.html) |
| `DirectoryContentsDisplayComponent` | A base class for components that display a list of the files in a directory | [ref](https://docs.juce.com/master/classjuce_1_1DirectoryContentsDisplayComponent.html) |
| `DrawableButton` | A button that displays a Drawable | [ref](https://docs.juce.com/master/classjuce_1_1DrawableButton.html) |
| `FileBrowserComponent` | A component for browsing and selecting a file or directory to open or save | [ref](https://docs.juce.com/master/classjuce_1_1FileBrowserComponent.html) |
| `FileBrowserListener` | A listener for user selection events in a file browser | [ref](https://docs.juce.com/master/classjuce_1_1FileBrowserListener.html) |
| `FileListComponent` | A component that displays the files in a directory as a listbox | [ref](https://docs.juce.com/master/classjuce_1_1FileListComponent.html) |
| `FilePreviewComponent` | Base class for components that live inside a file chooser dialog box and show previews of the files that get selected | [ref](https://docs.juce.com/master/classjuce_1_1FilePreviewComponent.html) |
| `FileSearchPathListComponent` | Shows a set of file paths in a list, allowing them to be added, removed or re-ordered | [ref](https://docs.juce.com/master/classjuce_1_1FileSearchPathListComponent.html) |
| `FileTreeComponent` | A component that displays the files in a directory as a treeview | [ref](https://docs.juce.com/master/classjuce_1_1FileTreeComponent.html) |
| `FilenameComponent` | Shows a filename as an editable text box, with a 'browse' button and a drop-down list for recently selected files | [ref](https://docs.juce.com/master/classjuce_1_1FilenameComponent.html) |
| `FilenameComponentListener` | Listens for events happening to a FilenameComponent | [ref](https://docs.juce.com/master/classjuce_1_1FilenameComponentListener.html) |
| `GroupComponent` | A component that draws an outline around itself and has an optional title at the top, for drawing an outline around a... | [ref](https://docs.juce.com/master/classjuce_1_1GroupComponent.html) |
| `HWNDComponent` | A Windows-specific class that can create and embed a HWND inside itself | [ref](https://docs.juce.com/master/classjuce_1_1HWNDComponent.html) |
| `HyperlinkButton` | A button showing an underlined weblink, that will launch the link when it's clicked | [ref](https://docs.juce.com/master/classjuce_1_1HyperlinkButton.html) |
| `ImageButton` | As the title suggests, this is a button containing an image | [ref](https://docs.juce.com/master/classjuce_1_1ImageButton.html) |
| `ImageComponent` | A component that simply displays an image | [ref](https://docs.juce.com/master/classjuce_1_1ImageComponent.html) |
| `ImagePreviewComponent` | A simple preview component that shows thumbnails of image files | [ref](https://docs.juce.com/master/classjuce_1_1ImagePreviewComponent.html) |
| `KeyMappingEditorComponent` | A component to allow editing of the keymaps stored by a KeyPressMappingSet object | [ref](https://docs.juce.com/master/classjuce_1_1KeyMappingEditorComponent.html) |
| `KeyboardComponentBase` | A base class for drawing a custom MIDI keyboard component | [ref](https://docs.juce.com/master/classjuce_1_1KeyboardComponentBase.html) |
| `Label` | A component that displays a text string, and can optionally become a text editor when clicked | [ref](https://docs.juce.com/master/classjuce_1_1Label.html) |
| `Label::Listener` | A class for receiving events from a Label | [ref](https://docs.juce.com/master/classjuce_1_1Label_1_1Listener.html) |
| `LassoComponent` | A component that acts as a rectangular selection region, which you drag with the mouse to select groups of objects (i... | [ref](https://docs.juce.com/master/classjuce_1_1LassoComponent.html) |
| `ListBox` | A list of items that can be scrolled vertically | [ref](https://docs.juce.com/master/classjuce_1_1ListBox.html) |
| `ListBoxModel` | A subclass of this is used to drive a ListBox | [ref](https://docs.juce.com/master/classjuce_1_1ListBoxModel.html) |
| `MenuBarComponent` | A menu bar component | [ref](https://docs.juce.com/master/classjuce_1_1MenuBarComponent.html) |
| `MenuBarModel` | A class for controlling MenuBar components | [ref](https://docs.juce.com/master/classjuce_1_1MenuBarModel.html) |
| `MenuBarModel::Listener` | A class to receive callbacks when a MenuBarModel changes | [ref](https://docs.juce.com/master/classjuce_1_1MenuBarModel_1_1Listener.html) |
| `ModalComponentManager` | Manages the system's stack of modal components | [ref](https://docs.juce.com/master/classjuce_1_1ModalComponentManager.html) |
| `ModalComponentManager::Callback` | Receives callbacks when a modal component is dismissed | [ref](https://docs.juce.com/master/classjuce_1_1ModalComponentManager_1_1Callback.html) |
| `ModalComponentManager::Key` |  | [ref](https://docs.juce.com/master/classjuce_1_1ModalComponentManager_1_1Key.html) |
| `MultiChoicePropertyComponent` | A PropertyComponent that shows its value as an expandable list of ToggleButtons | [ref](https://docs.juce.com/master/classjuce_1_1MultiChoicePropertyComponent.html) |
| `NSViewComponent` | A Mac-specific class that can create and embed an NSView inside itself | [ref](https://docs.juce.com/master/classjuce_1_1NSViewComponent.html) |
| `PluginListComponent` | A component displaying a list of plugins, with options to scan for them, add, remove and sort them | [ref](https://docs.juce.com/master/classjuce_1_1PluginListComponent.html) |
| `PopupMenu` | Creates and displays a popup-menu | [ref](https://docs.juce.com/master/classjuce_1_1PopupMenu.html) |
| `PopupMenu::CustomCallback` | A user-defined callback that can be used for specific items in a popup menu | [ref](https://docs.juce.com/master/classjuce_1_1PopupMenu_1_1CustomCallback.html) |
| `PopupMenu::CustomComponent` | A user-defined component that can be used as an item in a popup menu | [ref](https://docs.juce.com/master/classjuce_1_1PopupMenu_1_1CustomComponent.html) |
| `PopupMenu::MenuItemIterator` | Allows you to iterate through the items in a pop-up menu, and examine their properties | [ref](https://docs.juce.com/master/classjuce_1_1PopupMenu_1_1MenuItemIterator.html) |
| `PopupMenu::Options` | Class used to create a set of options to pass to the show() method | [ref](https://docs.juce.com/master/classjuce_1_1PopupMenu_1_1Options.html) |
| `PropertyComponent` | A base class for a component that goes in a PropertyPanel and displays one of an item's properties | [ref](https://docs.juce.com/master/classjuce_1_1PropertyComponent.html) |
| `PropertyPanel` | A panel that holds a list of PropertyComponent objects | [ref](https://docs.juce.com/master/classjuce_1_1PropertyPanel.html) |
| `RelativeCoordinatePositionerBase::ComponentScope` | Used for resolving a RelativeCoordinate expression in the context of a component | [ref](https://docs.juce.com/master/classjuce_1_1RelativeCoordinatePositionerBase_1_1ComponentScope.html) |
| `ResizableBorderComponent` | A component that resizes its parent component when dragged | [ref](https://docs.juce.com/master/classjuce_1_1ResizableBorderComponent.html) |
| `ResizableBorderComponent::Zone` | Represents the different sections of a resizable border, which allow it to resized in different ways | [ref](https://docs.juce.com/master/classjuce_1_1ResizableBorderComponent_1_1Zone.html) |
| `ResizableCornerComponent` | A component that resizes a parent component when dragged | [ref](https://docs.juce.com/master/classjuce_1_1ResizableCornerComponent.html) |
| `ResizableEdgeComponent` | A component that resizes its parent component when dragged | [ref](https://docs.juce.com/master/classjuce_1_1ResizableEdgeComponent.html) |
| `ScrollBar` | A scrollbar component | [ref](https://docs.juce.com/master/classjuce_1_1ScrollBar.html) |
| `ScrollBar::Listener` | A class for receiving events from a ScrollBar | [ref](https://docs.juce.com/master/classjuce_1_1ScrollBar_1_1Listener.html) |
| `ShapeButton` | A button that contains a filled shape | [ref](https://docs.juce.com/master/classjuce_1_1ShapeButton.html) |
| `Slider` | A slider control for changing a value | [ref](https://docs.juce.com/master/classjuce_1_1Slider.html) |
| `Slider::ScopedDragNotification` | An RAII class for sending slider listener drag messages | [ref](https://docs.juce.com/master/classjuce_1_1Slider_1_1ScopedDragNotification.html) |
| `SliderListener` | A class for receiving callbacks from a Slider or WebSliderRelay | [ref](https://docs.juce.com/master/classjuce_1_1SliderListener.html) |
| `SliderParameterAttachment` | An object of this class maintains a connection between a Slider and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1SliderParameterAttachment.html) |
| `SliderPropertyComponent` | A PropertyComponent that shows its value as a slider | [ref](https://docs.juce.com/master/classjuce_1_1SliderPropertyComponent.html) |
| `SystemTrayIconComponent` | This component sits in the taskbar tray as a small icon | [ref](https://docs.juce.com/master/classjuce_1_1SystemTrayIconComponent.html) |
| `TabBarButton` | In a TabbedButtonBar, this component is used for each of the buttons | [ref](https://docs.juce.com/master/classjuce_1_1TabBarButton.html) |
| `TabbedButtonBar` | A vertical or horizontal bar containing tabs that you can select | [ref](https://docs.juce.com/master/classjuce_1_1TabbedButtonBar.html) |
| `TabbedComponent` | A component with a TabbedButtonBar along one of its sides | [ref](https://docs.juce.com/master/classjuce_1_1TabbedComponent.html) |
| `TableHeaderComponent` | A component that displays a strip of column headings for a table, and allows these to be resized, dragged around, etc | [ref](https://docs.juce.com/master/classjuce_1_1TableHeaderComponent.html) |
| `TableHeaderComponent::Listener` | Receives events from a TableHeaderComponent when columns are resized, moved, etc | [ref](https://docs.juce.com/master/classjuce_1_1TableHeaderComponent_1_1Listener.html) |
| `TableListBox` | A table of cells, using a TableHeaderComponent as its header | [ref](https://docs.juce.com/master/classjuce_1_1TableListBox.html) |
| `TableListBoxModel` | One of these is used by a TableListBox as the data model for the table's contents | [ref](https://docs.juce.com/master/classjuce_1_1TableListBoxModel.html) |
| `TextButton` | A button that uses the standard lozenge-shaped background with a line of text on it | [ref](https://docs.juce.com/master/classjuce_1_1TextButton.html) |
| `TextEditor` | An editable text box | [ref](https://docs.juce.com/master/classjuce_1_1TextEditor.html) |
| `TextEditor::InputFilter` | Base class for input filters that can be applied to a TextEditor to restrict the text that can be entered | [ref](https://docs.juce.com/master/classjuce_1_1TextEditor_1_1InputFilter.html) |
| `TextEditor::LengthAndCharacterRestriction` | An input filter for a TextEditor that limits the length of text and/or the characters that it may contain | [ref](https://docs.juce.com/master/classjuce_1_1TextEditor_1_1LengthAndCharacterRestriction.html) |
| `TextEditor::Listener` | Receives callbacks from a TextEditor component when it changes | [ref](https://docs.juce.com/master/classjuce_1_1TextEditor_1_1Listener.html) |
| `TextPropertyComponent` | A PropertyComponent that shows its value as editable text | [ref](https://docs.juce.com/master/classjuce_1_1TextPropertyComponent.html) |
| `TextPropertyComponent::Listener` | Used to receive callbacks for text changes | [ref](https://docs.juce.com/master/classjuce_1_1TextPropertyComponent_1_1Listener.html) |
| `ToggleButton` | A button that can be toggled on/off | [ref](https://docs.juce.com/master/classjuce_1_1ToggleButton.html) |
| `Toolbar` | A toolbar component | [ref](https://docs.juce.com/master/classjuce_1_1Toolbar.html) |
| `ToolbarButton` | A type of button designed to go on a toolbar | [ref](https://docs.juce.com/master/classjuce_1_1ToolbarButton.html) |
| `ToolbarItemComponent` | A component that can be used as one of the items in a Toolbar | [ref](https://docs.juce.com/master/classjuce_1_1ToolbarItemComponent.html) |
| `ToolbarItemFactory` | A factory object which can create ToolbarItemComponent objects | [ref](https://docs.juce.com/master/classjuce_1_1ToolbarItemFactory.html) |
| `ToolbarItemPalette` | A component containing a list of toolbar items, which the user can drag onto a toolbar to add them | [ref](https://docs.juce.com/master/classjuce_1_1ToolbarItemPalette.html) |
| `TreeView` | A tree-view component | [ref](https://docs.juce.com/master/classjuce_1_1TreeView.html) |
| `TreeViewItem` | An item in a TreeView | [ref](https://docs.juce.com/master/classjuce_1_1TreeViewItem.html) |
| `TreeViewItem::OpennessRestorer` | This handy class takes a copy of a TreeViewItem's openness when you create it, and restores that openness state when ... | [ref](https://docs.juce.com/master/classjuce_1_1TreeViewItem_1_1OpennessRestorer.html) |
| `UIViewComponent` | An iOS-specific class that can create and embed an UIView inside itself | [ref](https://docs.juce.com/master/classjuce_1_1UIViewComponent.html) |
| `VideoComponent` | A component that can play a movie | [ref](https://docs.juce.com/master/classjuce_1_1VideoComponent.html) |
| `WebBrowserComponent` | A component that displays an embedded web browser | [ref](https://docs.juce.com/master/classjuce_1_1WebBrowserComponent.html) |
| `WebBrowserComponent::EvaluationResult` | On MacOS, iOS and Linux getResult will return a nullptr if the evaluation failed | [ref](https://docs.juce.com/master/classjuce_1_1WebBrowserComponent_1_1EvaluationResult.html) |
| `WebBrowserComponent::Options` | Options to configure WebBrowserComponent | [ref](https://docs.juce.com/master/classjuce_1_1WebBrowserComponent_1_1Options.html) |
| `WebBrowserComponent::Options::AppleWkWebView` | Options specific to the WkWebView backend used on Apple systems | [ref](https://docs.juce.com/master/classjuce_1_1WebBrowserComponent_1_1Options_1_1AppleWkWebView.html) |
| `WebBrowserComponent::Options::WinWebView2` | Options specific to the WebView2 backend | [ref](https://docs.juce.com/master/classjuce_1_1WebBrowserComponent_1_1Options_1_1WinWebView2.html) |
| `WebComboBoxParameterAttachment` | An object of this class maintains a connection between a WebComboBoxRelay and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1WebComboBoxParameterAttachment.html) |
| `WebComboBoxRelay` | Helper class that relays audio parameter information to an object inside a WebBrowserComponent | [ref](https://docs.juce.com/master/classjuce_1_1WebComboBoxRelay.html) |
| `WebSliderParameterAttachment` | An object of this class maintains a connection between a WebSliderRelay and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1WebSliderParameterAttachment.html) |
| `WebSliderRelay` | Helper class that relays audio parameter information to an object inside a WebBrowserComponent | [ref](https://docs.juce.com/master/classjuce_1_1WebSliderRelay.html) |
| `WebToggleButtonParameterAttachment` | An object of this class maintains a connection between a WebToggleButtonRelay and a plug-in parameter | [ref](https://docs.juce.com/master/classjuce_1_1WebToggleButtonParameterAttachment.html) |
| `WebToggleButtonRelay` | Helper class that relays audio parameter information to an object inside a WebBrowserComponent | [ref](https://docs.juce.com/master/classjuce_1_1WebToggleButtonRelay.html) |
| `XEmbedComponent` | A Linux-specific class that can embed a foreign X11 widget | [ref](https://docs.juce.com/master/classjuce_1_1XEmbedComponent.html) |
| `XEmbedComponentOptions` | Options for constructing an XEmbedComponent | [ref](https://docs.juce.com/master/classjuce_1_1XEmbedComponentOptions.html) |

## LookAndFeel

| Class | Description | Docs |
|-------|-------------|------|
| `LookAndFeel` | LookAndFeel objects define the appearance of all the JUCE widgets, and subclasses can be used to apply different 'ski... | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel.html) |
| `LookAndFeel__V1` | The original JUCE look-and-feel, as used back from 2002 to about 2007ish | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel__V1.html) |
| `LookAndFeel__V2` | This LookAndFeel subclass implements the juce style from around 2008-12 | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel__V2.html) |
| `LookAndFeel__V3` | The latest JUCE look-and-feel style, as introduced in 2013 | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel__V3.html) |
| `LookAndFeel__V4` | The latest JUCE look-and-feel style, as introduced in 2017 | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel__V4.html) |

## Graphics

| Class | Description | Docs |
|-------|-------------|------|
| `Colour` | Represents a colour, also including a transparency value | [ref](https://docs.juce.com/master/classjuce_1_1Colour.html) |
| `ColourGradient` | Describes the layout and colours that should be used to paint a colour gradient | [ref](https://docs.juce.com/master/classjuce_1_1ColourGradient.html) |
| `DrawableImage` | A drawable object which is a bitmap image | [ref](https://docs.juce.com/master/classjuce_1_1DrawableImage.html) |
| `DrawablePath` | A drawable object which renders a filled or outlined shape | [ref](https://docs.juce.com/master/classjuce_1_1DrawablePath.html) |
| `DropShadowEffect` | An effect filter that adds a drop-shadow behind the image's content | [ref](https://docs.juce.com/master/classjuce_1_1DropShadowEffect.html) |
| `DropShadower` | Adds a drop-shadow to a component | [ref](https://docs.juce.com/master/classjuce_1_1DropShadower.html) |
| `FileSearchPath` | Represents a set of folders that make up a search path | [ref](https://docs.juce.com/master/classjuce_1_1FileSearchPath.html) |
| `Font` | Represents a particular font, including its size, style, etc | [ref](https://docs.juce.com/master/classjuce_1_1Font.html) |
| `FontFeatureSetting` | Represents a single OpenType font feature setting | [ref](https://docs.juce.com/master/classjuce_1_1FontFeatureSetting.html) |
| `FontFeatureTag` | Represents a single OpenType font feature | [ref](https://docs.juce.com/master/classjuce_1_1FontFeatureTag.html) |
| `FontOptions` | Options that describe a particular font | [ref](https://docs.juce.com/master/classjuce_1_1FontOptions.html) |
| `GIFImageFormat` | A subclass of ImageFileFormat for reading GIF files | [ref](https://docs.juce.com/master/classjuce_1_1GIFImageFormat.html) |
| `GlyphArrangement` | A set of glyphs, each with a position | [ref](https://docs.juce.com/master/classjuce_1_1GlyphArrangement.html) |
| `GlyphArrangementOptions` | Options that can be used to affect the layout produced by GlyphArrangement::addFittedText | [ref](https://docs.juce.com/master/classjuce_1_1GlyphArrangementOptions.html) |
| `Graphics` | A graphics context, used for drawing a component or image | [ref](https://docs.juce.com/master/classjuce_1_1Graphics.html) |
| `Graphics::ScopedSaveState` | Uses RAII to save and restore the state of a graphics context | [ref](https://docs.juce.com/master/classjuce_1_1Graphics_1_1ScopedSaveState.html) |
| `Image` | Holds a fixed-size bitmap | [ref](https://docs.juce.com/master/classjuce_1_1Image.html) |
| `Image::BitmapData` | Retrieves a section of an image as raw pixel data, so it can be read or written to | [ref](https://docs.juce.com/master/classjuce_1_1Image_1_1BitmapData.html) |
| `Image::BitmapData::BitmapDataReleaser` | Used internally by custom image types to manage pixel data lifetime | [ref](https://docs.juce.com/master/classjuce_1_1Image_1_1BitmapData_1_1BitmapDataReleaser.html) |
| `ImageCache` | A global cache of images that have been loaded from files or memory | [ref](https://docs.juce.com/master/classjuce_1_1ImageCache.html) |
| `ImageConvolutionKernel` | Represents a filter kernel to use in convoluting an image | [ref](https://docs.juce.com/master/classjuce_1_1ImageConvolutionKernel.html) |
| `ImageEffectFilter` | A graphical effect filter that can be applied to components | [ref](https://docs.juce.com/master/classjuce_1_1ImageEffectFilter.html) |
| `ImageFileFormat` | Base-class for codecs that can read and write image file formats such as PNG, JPEG, etc | [ref](https://docs.juce.com/master/classjuce_1_1ImageFileFormat.html) |
| `ImagePixelData` | This is a base class for holding image data in implementation-specific ways | [ref](https://docs.juce.com/master/classjuce_1_1ImagePixelData.html) |
| `ImagePixelDataBackupExtensions` | The methods on this interface allow clients of ImagePixelData to query and control the automatic-backup process from ... | [ref](https://docs.juce.com/master/classjuce_1_1ImagePixelDataBackupExtensions.html) |
| `ImagePixelDataNativeExtensions` |  | [ref](https://docs.juce.com/master/classjuce_1_1ImagePixelDataNativeExtensions.html) |
| `ImageType` | This base class is for handlers that control a type of image manipulation format, e.g | [ref](https://docs.juce.com/master/classjuce_1_1ImageType.html) |
| `JPEGImageFormat` | A subclass of ImageFileFormat for reading and writing JPEG files | [ref](https://docs.juce.com/master/classjuce_1_1JPEGImageFormat.html) |
| `Justification` | Represents a type of justification to be used when positioning graphical items | [ref](https://docs.juce.com/master/classjuce_1_1Justification.html) |
| `LookAndFeel__V4::ColourScheme` | A struct containing the set of colours to apply to the GUI | [ref](https://docs.juce.com/master/classjuce_1_1LookAndFeel__V4_1_1ColourScheme.html) |
| `LowLevelGraphicsContext` | Interface class for graphics context objects, used internally by the Graphics class | [ref](https://docs.juce.com/master/classjuce_1_1LowLevelGraphicsContext.html) |
| `LowLevelGraphicsSoftwareRenderer` | A lowest-common-denominator implementation of LowLevelGraphicsContext that does all its rendering in memory | [ref](https://docs.juce.com/master/classjuce_1_1LowLevelGraphicsSoftwareRenderer.html) |
| `NativeImageType` | An image storage type which holds the pixels using whatever is the default storage format on the current platform | [ref](https://docs.juce.com/master/classjuce_1_1NativeImageType.html) |
| `PNGImageFormat` | A subclass of ImageFileFormat for reading and writing PNG files | [ref](https://docs.juce.com/master/classjuce_1_1PNGImageFormat.html) |
| `Path` | A path is a sequence of lines and curves that may either form a closed shape or be open-ended | [ref](https://docs.juce.com/master/classjuce_1_1Path.html) |
| `Path::Iterator` | Iterates the lines and curves that a path contains | [ref](https://docs.juce.com/master/classjuce_1_1Path_1_1Iterator.html) |
| `PathFlatteningIterator` | Flattens a Path object into a series of straight-line sections | [ref](https://docs.juce.com/master/classjuce_1_1PathFlatteningIterator.html) |
| `PathStrokeType` | Describes a type of stroke used to render a solid outline along a path | [ref](https://docs.juce.com/master/classjuce_1_1PathStrokeType.html) |
| `PositionedGlyph` | A glyph from a particular font, with a particular size, style, typeface and position | [ref](https://docs.juce.com/master/classjuce_1_1PositionedGlyph.html) |
| `RelativePointPath` | A path object that consists of RelativePoint coordinates rather than the normal fixed ones | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath.html) |
| `RelativePointPath::CloseSubPath` | Class for the close sub path element | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1CloseSubPath.html) |
| `RelativePointPath::CubicTo` | Class for the cubic to element | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1CubicTo.html) |
| `RelativePointPath::ElementBase` | Base class for the elements that make up a RelativePointPath | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1ElementBase.html) |
| `RelativePointPath::LineTo` | Class for the line to element | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1LineTo.html) |
| `RelativePointPath::QuadraticTo` | Class for the quadratic to element | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1QuadraticTo.html) |
| `RelativePointPath::StartSubPath` | Class for the start sub path element | [ref](https://docs.juce.com/master/classjuce_1_1RelativePointPath_1_1StartSubPath.html) |
| `ScaledImage` | An image that will be resampled before it is drawn | [ref](https://docs.juce.com/master/classjuce_1_1ScaledImage.html) |
| `SoftwareImageType` | An image storage type which holds the pixels in-memory as a simple block of values | [ref](https://docs.juce.com/master/classjuce_1_1SoftwareImageType.html) |
| `TextLayout::Glyph` | A positioned glyph | [ref](https://docs.juce.com/master/classjuce_1_1TextLayout_1_1Glyph.html) |
| `Typeface` | A typeface represents a size-independent font | [ref](https://docs.juce.com/master/classjuce_1_1Typeface.html) |

## Layout/Geometry

| Class | Description | Docs |
|-------|-------------|------|
| `AffineTransform` | Represents a 2D affine-transformation matrix | [ref](https://docs.juce.com/master/classjuce_1_1AffineTransform.html) |
| `AudioData::Pointer` | Used as a template parameter for AudioData::Pointer | [ref](https://docs.juce.com/master/classjuce_1_1AudioData_1_1Pointer.html) |
| `BorderSize` | Specifies a set of gaps to be left around the sides of a rectangle | [ref](https://docs.juce.com/master/classjuce_1_1BorderSize.html) |
| `CharPointer__ASCII` | Wraps a pointer to a null-terminated ASCII character string, and provides various methods to operate on the data | [ref](https://docs.juce.com/master/classjuce_1_1CharPointer__ASCII.html) |
| `CharPointer__UTF16` | Wraps a pointer to a null-terminated UTF-16 character string, and provides various methods to operate on the data | [ref](https://docs.juce.com/master/classjuce_1_1CharPointer__UTF16.html) |
| `CharPointer__UTF32` | Wraps a pointer to a null-terminated UTF-32 character string, and provides various methods to operate on the data | [ref](https://docs.juce.com/master/classjuce_1_1CharPointer__UTF32.html) |
| `CharPointer__UTF8` | Wraps a pointer to a null-terminated UTF-8 character string, and provides various methods to operate on the data | [ref](https://docs.juce.com/master/classjuce_1_1CharPointer__UTF8.html) |
| `DrawableRectangle` | A Drawable object which draws a rectangle | [ref](https://docs.juce.com/master/classjuce_1_1DrawableRectangle.html) |
| `FlexBox` | Represents a FlexBox container, which contains and manages the layout of a set of FlexItem objects | [ref](https://docs.juce.com/master/classjuce_1_1FlexBox.html) |
| `FlexItem` | Describes the properties of an item inside a FlexBox container | [ref](https://docs.juce.com/master/classjuce_1_1FlexItem.html) |
| `Grid` | Container that handles geometry for grid layouts (fixed columns and rows) using a set of declarative rules | [ref](https://docs.juce.com/master/classjuce_1_1Grid.html) |
| `GridItem` | Defines an item in a Grid | [ref](https://docs.juce.com/master/classjuce_1_1GridItem.html) |
| `Line` | Represents a line | [ref](https://docs.juce.com/master/classjuce_1_1Line.html) |
| `LinkedListPointer` | Helps to manipulate singly-linked lists of objects | [ref](https://docs.juce.com/master/classjuce_1_1LinkedListPointer.html) |
| `LinkedListPointer::Appender` | Allows efficient repeated insertions into a list | [ref](https://docs.juce.com/master/classjuce_1_1LinkedListPointer_1_1Appender.html) |
| `NewLine` | This class is used for represent a new-line character sequence | [ref](https://docs.juce.com/master/classjuce_1_1NewLine.html) |
| `NormalisableRange` | Represents a mapping between an arbitrary range of values and a normalised 0->1 range | [ref](https://docs.juce.com/master/classjuce_1_1NormalisableRange.html) |
| `OptionalScopedPointer` | Holds a pointer to an object which can optionally be deleted when this pointer goes out of scope | [ref](https://docs.juce.com/master/classjuce_1_1OptionalScopedPointer.html) |
| `Point` | A pair of (x, y) coordinates | [ref](https://docs.juce.com/master/classjuce_1_1Point.html) |
| `Range` | A general-purpose range object, that simply represents any linear range with a start and end point | [ref](https://docs.juce.com/master/classjuce_1_1Range.html) |
| `RangedDirectoryIterator` | Allows iterating over files and folders using C++11 range-for syntax | [ref](https://docs.juce.com/master/classjuce_1_1RangedDirectoryIterator.html) |
| `Rectangle` | Manages a rectangle and allows geometric operations to be performed on it | [ref](https://docs.juce.com/master/classjuce_1_1Rectangle.html) |
| `RectangleList` | Maintains a set of rectangles as a complex region | [ref](https://docs.juce.com/master/classjuce_1_1RectangleList.html) |
| `RectanglePlacement` | Defines the method used to position some kind of rectangular object within a rectangular viewport | [ref](https://docs.juce.com/master/classjuce_1_1RectanglePlacement.html) |
| `RelativePoint` | An X-Y position stored as a pair of RelativeCoordinate values | [ref](https://docs.juce.com/master/classjuce_1_1RelativePoint.html) |
| `RelativeRectangle` | A rectangle stored as a set of RelativeCoordinate values | [ref](https://docs.juce.com/master/classjuce_1_1RelativeRectangle.html) |
| `SharedResourcePointer` | A smart-pointer that automatically creates and manages the lifetime of a shared static instance of a class | [ref](https://docs.juce.com/master/classjuce_1_1SharedResourcePointer.html) |
| `TextLayout::Line` | A line containing a sequence of glyph-runs | [ref](https://docs.juce.com/master/classjuce_1_1TextLayout_1_1Line.html) |
| `WeakReference::SharedPointer` | This class is used internally by the WeakReference class - don't use it directly in your code! | [ref](https://docs.juce.com/master/classjuce_1_1WeakReference_1_1SharedPointer.html) |

## OpenGL

| Class | Description | Docs |
|-------|-------------|------|
| `OpenGLAppComponent` | A base class for writing simple one-page graphical apps | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLAppComponent.html) |
| `OpenGLContext` | Creates an OpenGL context, which can be attached to a component | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLContext.html) |
| `OpenGLFrameBuffer` | Creates an openGL frame buffer | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLFrameBuffer.html) |
| `OpenGLHelpers` | A set of miscellaneous openGL helper functions | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLHelpers.html) |
| `OpenGLImageType` | A type of ImagePixelData that stores its image data in an OpenGL framebuffer, allowing a JUCE Image object to wrap a ... | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLImageType.html) |
| `OpenGLPixelFormat` | Represents the various properties of an OpenGL pixel format | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLPixelFormat.html) |
| `OpenGLRenderer` | A base class that should be implemented by classes which want to render openGL on a background thread | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLRenderer.html) |
| `OpenGLShaderProgram` | Manages an OpenGL shader program | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLShaderProgram.html) |
| `OpenGLTexture` | Creates an openGL texture from an Image | [ref](https://docs.juce.com/master/classjuce_1_1OpenGLTexture.html) |

## Events & Messaging

| Class | Description | Docs |
|-------|-------------|------|
| `ActionBroadcaster` | Manages a list of ActionListeners, and can send them messages | [ref](https://docs.juce.com/master/classjuce_1_1ActionBroadcaster.html) |
| `ActionListener` | Interface class for delivery of events that are sent by an ActionBroadcaster | [ref](https://docs.juce.com/master/classjuce_1_1ActionListener.html) |
| `AsyncUpdater` | Has a callback method that is triggered asynchronously | [ref](https://docs.juce.com/master/classjuce_1_1AsyncUpdater.html) |
| `ChangeBroadcaster` | Holds a list of ChangeListeners, and sends messages to them when instructed | [ref](https://docs.juce.com/master/classjuce_1_1ChangeBroadcaster.html) |
| `ChangeListener` | Receives change event callbacks that are sent out by a ChangeBroadcaster | [ref](https://docs.juce.com/master/classjuce_1_1ChangeListener.html) |
| `FocusChangeListener` | Classes can implement this interface and register themselves with the Desktop class to receive callbacks when the cur... | [ref](https://docs.juce.com/master/classjuce_1_1FocusChangeListener.html) |
| `HighResolutionTimer` | A high-resolution periodic timer | [ref](https://docs.juce.com/master/classjuce_1_1HighResolutionTimer.html) |
| `LockingAsyncUpdater` | A bit like an AsyncUpdater, but guarantees that after cancelPendingUpdate() returns, the async function will never be... | [ref](https://docs.juce.com/master/classjuce_1_1LockingAsyncUpdater.html) |
| `MessageManager` | This class is in charge of the application's event-dispatch loop | [ref](https://docs.juce.com/master/classjuce_1_1MessageManager.html) |
| `MessageManager::Lock` | A lock you can use to lock the message manager | [ref](https://docs.juce.com/master/classjuce_1_1MessageManager_1_1Lock.html) |
| `MessageManager::MessageBase` | Internal class used as the base class for all message objects | [ref](https://docs.juce.com/master/classjuce_1_1MessageManager_1_1MessageBase.html) |
| `MessageManagerLock` | Used to make sure that the calling thread has exclusive access to the message loop | [ref](https://docs.juce.com/master/classjuce_1_1MessageManagerLock.html) |
| `MultiTimer` | A type of timer class that can run multiple timers with different frequencies, all of which share a single callback | [ref](https://docs.juce.com/master/classjuce_1_1MultiTimer.html) |
| `Timer` | Makes repeated callbacks to a virtual method at a specified time interval | [ref](https://docs.juce.com/master/classjuce_1_1Timer.html) |

## Threading

| Class | Description | Docs |
|-------|-------------|------|
| `AbstractFifo` | Encapsulates the logic required to implement a lock-free FIFO | [ref](https://docs.juce.com/master/classjuce_1_1AbstractFifo.html) |
| `AbstractFifo::ScopedReadWrite` | Class for a scoped reader/writer | [ref](https://docs.juce.com/master/classjuce_1_1AbstractFifo_1_1ScopedReadWrite.html) |
| `CriticalSection` | A re-entrant mutex | [ref](https://docs.juce.com/master/classjuce_1_1CriticalSection.html) |
| `DummyCriticalSection` | A class that can be used in place of a real CriticalSection object, but which doesn't perform any locking | [ref](https://docs.juce.com/master/classjuce_1_1DummyCriticalSection.html) |
| `ReadWriteLock` | A critical section that allows multiple simultaneous readers | [ref](https://docs.juce.com/master/classjuce_1_1ReadWriteLock.html) |
| `ScheduledEventThread` |  | [ref](https://docs.juce.com/master/classjuce_1_1ScheduledEventThread.html) |
| `SingleThreadedAbstractFifo` | Encapsulates the logic for a single-threaded FIFO | [ref](https://docs.juce.com/master/classjuce_1_1SingleThreadedAbstractFifo.html) |
| `SingleThreadedIIRFilter` | An IIR filter that can perform low, high, or band-pass filtering on an audio signal, with no thread-safety guarantees | [ref](https://docs.juce.com/master/classjuce_1_1SingleThreadedIIRFilter.html) |
| `SingleThreadedReferenceCountedObject` | Adds reference-counting to an object | [ref](https://docs.juce.com/master/classjuce_1_1SingleThreadedReferenceCountedObject.html) |
| `SpinLock` | A simple spin-lock class that can be used as a simple, low-overhead mutex for uncontended situations | [ref](https://docs.juce.com/master/classjuce_1_1SpinLock.html) |
| `Thread` | Encapsulates a thread | [ref](https://docs.juce.com/master/classjuce_1_1Thread.html) |
| `Thread::Listener` | Used to receive callbacks for thread exit calls | [ref](https://docs.juce.com/master/classjuce_1_1Thread_1_1Listener.html) |
| `ThreadLocalValue` | Provides cross-platform support for thread-local objects | [ref](https://docs.juce.com/master/classjuce_1_1ThreadLocalValue.html) |
| `ThreadPool` | A set of threads that will run a list of jobs | [ref](https://docs.juce.com/master/classjuce_1_1ThreadPool.html) |
| `ThreadPool::JobSelector` | A callback class used when you need to select which ThreadPoolJob objects are suitable for some kind of operation | [ref](https://docs.juce.com/master/classjuce_1_1ThreadPool_1_1JobSelector.html) |
| `ThreadPoolJob` | A task that is executed by a ThreadPool object | [ref](https://docs.juce.com/master/classjuce_1_1ThreadPoolJob.html) |
| `ThreadWithProgressWindow` | A thread that automatically pops up a modal dialog box with a progress bar and cancel button while it's busy running | [ref](https://docs.juce.com/master/classjuce_1_1ThreadWithProgressWindow.html) |
| `ThreadedAnalyticsDestination` | A base class for dispatching analytics events on a dedicated thread | [ref](https://docs.juce.com/master/classjuce_1_1ThreadedAnalyticsDestination.html) |
| `TimeSliceThread` | A thread that keeps a list of clients, and calls each one in turn, giving them all a chance to run some sort of short... | [ref](https://docs.juce.com/master/classjuce_1_1TimeSliceThread.html) |
| `WaitableEvent` | Allows threads to wait for events triggered by other threads | [ref](https://docs.juce.com/master/classjuce_1_1WaitableEvent.html) |

## Data Structures

| Class | Description | Docs |
|-------|-------------|------|
| `Array` | Holds a resizable array of primitive or copy-by-value objects | [ref](https://docs.juce.com/master/classjuce_1_1Array.html) |
| `ArrayAllocationBase` | Implements some basic array storage allocation functions | [ref](https://docs.juce.com/master/classjuce_1_1ArrayAllocationBase.html) |
| `ArrayBase` | A basic object container | [ref](https://docs.juce.com/master/classjuce_1_1ArrayBase.html) |
| `CachedValue` | This class acts as a typed wrapper around a property inside a ValueTree | [ref](https://docs.juce.com/master/classjuce_1_1CachedValue.html) |
| `HashMap` | Holds a set of mappings between some key/value pairs | [ref](https://docs.juce.com/master/classjuce_1_1HashMap.html) |
| `Identifier` | Represents a string identifier, designed for accessing properties by name | [ref](https://docs.juce.com/master/classjuce_1_1Identifier.html) |
| `MarkerList::ValueTreeWrapper` | Forms a wrapper around a ValueTree that can be used for storing a MarkerList | [ref](https://docs.juce.com/master/classjuce_1_1MarkerList_1_1ValueTreeWrapper.html) |
| `NamedValue` | Structure for a named var object, used as an element of a NamedValueSet | [ref](https://docs.juce.com/master/classjuce_1_1NamedValue.html) |
| `NamedValueSet` | Holds a set of named var objects | [ref](https://docs.juce.com/master/classjuce_1_1NamedValueSet.html) |
| `OwnedArray` | An array designed for holding objects | [ref](https://docs.juce.com/master/classjuce_1_1OwnedArray.html) |
| `ReferenceCountedArray` | Holds a list of objects derived from ReferenceCountedObject, or which implement basic reference-count handling methods | [ref](https://docs.juce.com/master/classjuce_1_1ReferenceCountedArray.html) |
| `ReferenceCountedObject` | A base class which provides methods for reference-counting | [ref](https://docs.juce.com/master/classjuce_1_1ReferenceCountedObject.html) |
| `ReferenceCountedObjectPtr` | A smart-pointer class which points to a reference-counted object | [ref](https://docs.juce.com/master/classjuce_1_1ReferenceCountedObjectPtr.html) |
| `ScopedValueSetter` | Helper class providing an RAII-based mechanism for temporarily setting and then re-setting a value | [ref](https://docs.juce.com/master/classjuce_1_1ScopedValueSetter.html) |
| `SmoothedValue` | A utility class for values that need smoothing to avoid audio glitches | [ref](https://docs.juce.com/master/classjuce_1_1SmoothedValue.html) |
| `SmoothedValueBase` | A base class for the smoothed value classes | [ref](https://docs.juce.com/master/classjuce_1_1SmoothedValueBase.html) |
| `StringArray` | A special array for holding a list of strings | [ref](https://docs.juce.com/master/classjuce_1_1StringArray.html) |
| `StringPairArray` | A container for holding a set of strings which are keyed by another string | [ref](https://docs.juce.com/master/classjuce_1_1StringPairArray.html) |
| `UndoManager` | Manages a list of undo/redo commands | [ref](https://docs.juce.com/master/classjuce_1_1UndoManager.html) |
| `Value` | Represents a shared variant value | [ref](https://docs.juce.com/master/classjuce_1_1Value.html) |
| `Value::Listener` | Receives callbacks when a Value object changes | [ref](https://docs.juce.com/master/classjuce_1_1Value_1_1Listener.html) |
| `Value::ValueSource` | Used internally by the Value class as the base class for its shared value objects | [ref](https://docs.juce.com/master/classjuce_1_1Value_1_1ValueSource.html) |
| `ValueAnimatorBuilder` | A builder class that can be used to construct an Animator wrapping a ValueAnimator implementation | [ref](https://docs.juce.com/master/classjuce_1_1ValueAnimatorBuilder.html) |
| `ValueTree` | A powerful tree structure that can be used to hold free-form data, and which can handle its own undo and redo behaviour | [ref](https://docs.juce.com/master/classjuce_1_1ValueTree.html) |
| `ValueTree::Listener` | Listener class for events that happen to a ValueTree | [ref](https://docs.juce.com/master/classjuce_1_1ValueTree_1_1Listener.html) |
| `ValueTreePropertyWithDefault` | This class acts as a wrapper around a property inside a ValueTree | [ref](https://docs.juce.com/master/classjuce_1_1ValueTreePropertyWithDefault.html) |
| `ValueTreeSynchroniser` | This class can be used to watch for all changes to the state of a ValueTree, and to convert them to a transmittable b... | [ref](https://docs.juce.com/master/classjuce_1_1ValueTreeSynchroniser.html) |

## I/O & Storage

| Class | Description | Docs |
|-------|-------------|------|
| `BufferedInputStream` | Wraps another input stream, and reads from it using an intermediate buffer | [ref](https://docs.juce.com/master/classjuce_1_1BufferedInputStream.html) |
| `File` | Represents a local file or directory | [ref](https://docs.juce.com/master/classjuce_1_1File.html) |
| `FileBasedDocument` | A class to take care of the logic involved with the loading/saving of some kind of document | [ref](https://docs.juce.com/master/classjuce_1_1FileBasedDocument.html) |
| `FileChooser` | Creates a dialog box to choose a file or directory to load or save | [ref](https://docs.juce.com/master/classjuce_1_1FileChooser.html) |
| `FileChooserDialogBox` | A file open/save dialog box | [ref](https://docs.juce.com/master/classjuce_1_1FileChooserDialogBox.html) |
| `FileDragAndDropTarget` | Components derived from this class can have files dropped onto them by an external application | [ref](https://docs.juce.com/master/classjuce_1_1FileDragAndDropTarget.html) |
| `FileFilter` | Interface for deciding which files are suitable for something | [ref](https://docs.juce.com/master/classjuce_1_1FileFilter.html) |
| `FileInputSource` | A type of InputSource that represents a normal file | [ref](https://docs.juce.com/master/classjuce_1_1FileInputSource.html) |
| `FileInputStream` | An input stream that reads from a local file | [ref](https://docs.juce.com/master/classjuce_1_1FileInputStream.html) |
| `FileLogger` | A simple implementation of a Logger that writes to a file | [ref](https://docs.juce.com/master/classjuce_1_1FileLogger.html) |
| `FileOutputStream` | An output stream that writes into a local file | [ref](https://docs.juce.com/master/classjuce_1_1FileOutputStream.html) |
| `GZIPCompressorOutputStream` | A stream which uses zlib to compress the data written into it | [ref](https://docs.juce.com/master/classjuce_1_1GZIPCompressorOutputStream.html) |
| `GZIPDecompressorInputStream` | This stream will decompress a source-stream using zlib | [ref](https://docs.juce.com/master/classjuce_1_1GZIPDecompressorInputStream.html) |
| `InputStream` | The base class for streams that read data | [ref](https://docs.juce.com/master/classjuce_1_1InputStream.html) |
| `MemoryBlock` | A class to hold a resizable block of raw data | [ref](https://docs.juce.com/master/classjuce_1_1MemoryBlock.html) |
| `MemoryInputStream` | Allows a block of data to be accessed as a stream | [ref](https://docs.juce.com/master/classjuce_1_1MemoryInputStream.html) |
| `MemoryMappedFile` | Maps a file into virtual memory for easy reading and/or writing | [ref](https://docs.juce.com/master/classjuce_1_1MemoryMappedFile.html) |
| `MemoryOutputStream` | Writes data to an internal memory buffer, which grows as required | [ref](https://docs.juce.com/master/classjuce_1_1MemoryOutputStream.html) |
| `OutputStream` | The base class for streams that write data to some kind of destination | [ref](https://docs.juce.com/master/classjuce_1_1OutputStream.html) |
| `PropertiesFile` | Wrapper on a file that stores a list of key/value data pairs | [ref](https://docs.juce.com/master/classjuce_1_1PropertiesFile.html) |
| `RecentlyOpenedFilesList` | Manages a set of files for use as a list of recently-opened documents | [ref](https://docs.juce.com/master/classjuce_1_1RecentlyOpenedFilesList.html) |
| `TemporaryFile` | Manages a temporary file, which will be deleted when this object is deleted | [ref](https://docs.juce.com/master/classjuce_1_1TemporaryFile.html) |
| `URL` | Represents a URL and has a bunch of useful functions to manipulate it | [ref](https://docs.juce.com/master/classjuce_1_1URL.html) |
| `URL::DownloadTask` | Represents a download task | [ref](https://docs.juce.com/master/classjuce_1_1URL_1_1DownloadTask.html) |
| `URL::DownloadTaskOptions` | Holds options that can be specified when starting a new download with downloadToFile() | [ref](https://docs.juce.com/master/classjuce_1_1URL_1_1DownloadTaskOptions.html) |
| `URL::InputStreamOptions` | Class used to create a set of options to pass to the createInputStream() method | [ref](https://docs.juce.com/master/classjuce_1_1URL_1_1InputStreamOptions.html) |
| `URLInputSource` | A type of InputSource that represents a URL | [ref](https://docs.juce.com/master/classjuce_1_1URLInputSource.html) |
| `WebInputStream` | An InputStream which can be used to read from a given URL | [ref](https://docs.juce.com/master/classjuce_1_1WebInputStream.html) |
| `WebInputStream::Listener` | Used to receive callbacks for POST data send progress | [ref](https://docs.juce.com/master/classjuce_1_1WebInputStream_1_1Listener.html) |
| `WildcardFileFilter` | A type of FileFilter that works by wildcard pattern matching | [ref](https://docs.juce.com/master/classjuce_1_1WildcardFileFilter.html) |
| `ZipFile` | Decodes a ZIP file from a stream | [ref](https://docs.juce.com/master/classjuce_1_1ZipFile.html) |
| `ZipFile::Builder` | Used to create a new zip file | [ref](https://docs.juce.com/master/classjuce_1_1ZipFile_1_1Builder.html) |

## Network/Web

| Class | Description | Docs |
|-------|-------------|------|
| `OSCAddress` | An OSC address | [ref](https://docs.juce.com/master/classjuce_1_1OSCAddress.html) |
| `OSCAddressPattern` | An OSC address pattern | [ref](https://docs.juce.com/master/classjuce_1_1OSCAddressPattern.html) |
| `OSCArgument` | An OSC argument | [ref](https://docs.juce.com/master/classjuce_1_1OSCArgument.html) |
| `OSCBundle` | An OSC bundle | [ref](https://docs.juce.com/master/classjuce_1_1OSCBundle.html) |
| `OSCBundle::Element` | An OSC bundle element | [ref](https://docs.juce.com/master/classjuce_1_1OSCBundle_1_1Element.html) |
| `OSCMessage` | An OSC Message | [ref](https://docs.juce.com/master/classjuce_1_1OSCMessage.html) |
| `OSCReceiver` | A class for receiving OSC data | [ref](https://docs.juce.com/master/classjuce_1_1OSCReceiver.html) |
| `OSCReceiver::Listener` | A class for receiving OSC data from an OSCReceiver | [ref](https://docs.juce.com/master/classjuce_1_1OSCReceiver_1_1Listener.html) |
| `OSCReceiver::ListenerWithOSCAddress` | A class for receiving only those OSC messages from an OSCReceiver that match a given OSC address | [ref](https://docs.juce.com/master/classjuce_1_1OSCReceiver_1_1ListenerWithOSCAddress.html) |
| `OSCSender` | An OSC message sender | [ref](https://docs.juce.com/master/classjuce_1_1OSCSender.html) |
| `OSCTimeTag` | An OSC time tag | [ref](https://docs.juce.com/master/classjuce_1_1OSCTimeTag.html) |
| `OSCTypes` | The definitions of supported OSC types and their associated OSC type tags, as defined in the OpenSoundControl 1.0 spe... | [ref](https://docs.juce.com/master/classjuce_1_1OSCTypes.html) |
| `WebControlParameterIndexReceiver` | This is a helper class for implementing AudioProcessorEditor::getControlParameterIndex with GUIs using a WebBrowserCo... | [ref](https://docs.juce.com/master/classjuce_1_1WebControlParameterIndexReceiver.html) |
| `WebViewLifetimeListener` | Type for a listener registered with WebBrowserComponent::Options::withWebViewLifetimeListener | [ref](https://docs.juce.com/master/classjuce_1_1WebViewLifetimeListener.html) |

## Accessibility

| Class | Description | Docs |
|-------|-------------|------|
| `AccessibilityActions` | A simple wrapper for building a collection of supported accessibility actions and corresponding callbacks for a UI el... | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityActions.html) |
| `AccessibilityCellInterface` | An abstract interface which represents a UI element that supports a cell interface | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityCellInterface.html) |
| `AccessibilityHandler` | Base class for accessible Components | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityHandler.html) |
| `AccessibilityNumericValueInterface` | A value interface that represents a non-ranged numeric value | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityNumericValueInterface.html) |
| `AccessibilityRangedNumericValueInterface` | A value interface that represents a ranged numeric value | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityRangedNumericValueInterface.html) |
| `AccessibilityTableInterface` | An abstract interface which represents a UI element that supports a table interface | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityTableInterface.html) |
| `AccessibilityTextInterface` | An abstract interface which represents a UI element that supports a text interface | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityTextInterface.html) |
| `AccessibilityTextValueInterface` | A value interface that represents a text value | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityTextValueInterface.html) |
| `AccessibilityValueInterface` | An abstract interface representing the value of an accessibility element | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityValueInterface.html) |
| `AccessibilityValueInterface::AccessibleValueRange` | Represents the range of this value, if supported | [ref](https://docs.juce.com/master/classjuce_1_1AccessibilityValueInterface_1_1AccessibleValueRange.html) |
| `AccessibleState` | Represents the state of an accessible UI element | [ref](https://docs.juce.com/master/classjuce_1_1AccessibleState.html) |

## ARA

| Class | Description | Docs |
|-------|-------------|------|
| `ARAAudioModification` | Base class representing an ARA audio modification | [ref](https://docs.juce.com/master/classjuce_1_1ARAAudioModification.html) |
| `ARAAudioModificationListener` | A base class for listeners that want to know about changes to an ARAAudioModification object | [ref](https://docs.juce.com/master/classjuce_1_1ARAAudioModificationListener.html) |
| `ARAAudioSource` | Base class representing an ARA audio source | [ref](https://docs.juce.com/master/classjuce_1_1ARAAudioSource.html) |
| `ARAAudioSourceListener` | A base class for listeners that want to know about changes to an ARAAudioSource object | [ref](https://docs.juce.com/master/classjuce_1_1ARAAudioSourceListener.html) |
| `ARAAudioSourceReader` | Subclass of AudioFormatReader that reads samples from a single ARA audio source | [ref](https://docs.juce.com/master/classjuce_1_1ARAAudioSourceReader.html) |
| `ARADocument` | Base class representing an ARA document | [ref](https://docs.juce.com/master/classjuce_1_1ARADocument.html) |
| `ARADocumentController` |  | [ref](https://docs.juce.com/master/classjuce_1_1ARADocumentController.html) |
| `ARADocumentControllerSpecialisation` | This class contains the customisation points for the JUCE provided ARA document controller implementation | [ref](https://docs.juce.com/master/classjuce_1_1ARADocumentControllerSpecialisation.html) |
| `ARADocumentListener` | A base class for listeners that want to know about changes to an ARADocument object | [ref](https://docs.juce.com/master/classjuce_1_1ARADocumentListener.html) |
| `ARAEditGuard` | Reference counting helper class to ensure that the DocumentController is in editable state | [ref](https://docs.juce.com/master/classjuce_1_1ARAEditGuard.html) |
| `ARAEditorRenderer` | Base class for a renderer fulfilling the ARAEditorRenderer role as described in the ARA SDK | [ref](https://docs.juce.com/master/classjuce_1_1ARAEditorRenderer.html) |
| `ARAEditorView` | Base class for fulfilling the ARAEditorView role as described in the ARA SDK | [ref](https://docs.juce.com/master/classjuce_1_1ARAEditorView.html) |
| `ARAEditorView::Listener` | A base class for listeners that want to know about changes to an ARAEditorView object | [ref](https://docs.juce.com/master/classjuce_1_1ARAEditorView_1_1Listener.html) |
| `ARAFactoryWrapper` | Encapsulates an ARAFactory pointer and makes sure that it remains in a valid state for the lifetime of the ARAFactory... | [ref](https://docs.juce.com/master/classjuce_1_1ARAFactoryWrapper.html) |
| `ARAHostDocumentController` | Wrapper class for ARA::Host::DocumentController | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostDocumentController.html) |
| `ARAHostModel::AudioModification` | Helper class for the host side implementation of the ARA AudioModification model object | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1AudioModification.html) |
| `ARAHostModel::AudioSource` | Helper class for the host side implementation of the ARA AudioSource model object | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1AudioSource.html) |
| `ARAHostModel::ManagedARAHandle` | This class is used by the various ARA model object helper classes, such as MusicalContext, AudioSource etc | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1ManagedARAHandle.html) |
| `ARAHostModel::MusicalContext` | Helper class for the host side implementation of the ARA MusicalContext model object | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1MusicalContext.html) |
| `ARAHostModel::PlaybackRegionRegistry` | Base class used by the ::PlaybackRendererInterface and ::EditorRendererInterface plugin extension interfaces | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1PlaybackRegionRegistry.html) |
| `ARAHostModel::PlugInExtensionInstance` | Wrapper class for ARA::ARAPlugInExtensionInstance* | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1PlugInExtensionInstance.html) |
| `ARAHostModel::RegionSequence` | Helper class for the host side implementation of the ARA RegionSequence model object | [ref](https://docs.juce.com/master/classjuce_1_1ARAHostModel_1_1RegionSequence.html) |
| `ARAInputStream` | Used to read persisted ARA archives - see doRestoreObjectsFromStream() for details | [ref](https://docs.juce.com/master/classjuce_1_1ARAInputStream.html) |
| `ARAListenableModelClass` | Base class used by the JUCE ARA model objects to provide listenable interfaces | [ref](https://docs.juce.com/master/classjuce_1_1ARAListenableModelClass.html) |
| `ARAMusicalContext` | Base class representing an ARA musical context | [ref](https://docs.juce.com/master/classjuce_1_1ARAMusicalContext.html) |
| `ARAMusicalContextListener` | A base class for listeners that want to know about changes to an ARAMusicalContext object | [ref](https://docs.juce.com/master/classjuce_1_1ARAMusicalContextListener.html) |
| `ARAObject` | Common base class for all JUCE ARA model objects to aid with the discovery and traversal of the entire ARA model graph | [ref](https://docs.juce.com/master/classjuce_1_1ARAObject.html) |
| `ARAObjectVisitor` | Create a derived implementation of this class and pass it to ARAObject::visit() to retrieve the concrete type of a mo... | [ref](https://docs.juce.com/master/classjuce_1_1ARAObjectVisitor.html) |
| `ARAOutputStream` | Used to write persistent ARA archives - see doStoreObjectsToStream() for details | [ref](https://docs.juce.com/master/classjuce_1_1ARAOutputStream.html) |
| `ARAPlaybackRegion` | Base class representing an ARA playback region | [ref](https://docs.juce.com/master/classjuce_1_1ARAPlaybackRegion.html) |
| `ARAPlaybackRegionListener` | A base class for listeners that want to know about changes to an ARAPlaybackRegion object | [ref](https://docs.juce.com/master/classjuce_1_1ARAPlaybackRegionListener.html) |
| `ARAPlaybackRegionReader` | Subclass of AudioFormatReader that reads samples from a group of playback regions | [ref](https://docs.juce.com/master/classjuce_1_1ARAPlaybackRegionReader.html) |
| `ARAPlaybackRenderer` | Base class for a renderer fulfilling the ARAPlaybackRenderer role as described in the ARA SDK | [ref](https://docs.juce.com/master/classjuce_1_1ARAPlaybackRenderer.html) |
| `ARARegionSequence` | Base class representing an ARA region sequence | [ref](https://docs.juce.com/master/classjuce_1_1ARARegionSequence.html) |
| `ARARegionSequenceListener` | A base class for listeners that want to know about changes to an ARARegionSequence object | [ref](https://docs.juce.com/master/classjuce_1_1ARARegionSequenceListener.html) |
| `ARARenderer` | Base class for a renderer fulfilling either the ARAPlaybackRenderer or the ARAEditorRenderer role | [ref](https://docs.juce.com/master/classjuce_1_1ARARenderer.html) |
| `AudioProcessorARAExtension` | Extension class meant to be subclassed by the plugin's implementation of | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorARAExtension.html) |
| `AudioProcessorEditorARAExtension` | Extension class meant to be subclassed by the plugin's implementation of | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessorEditorARAExtension.html) |

## Math/DSP Utilities

| Class | Description | Docs |
|-------|-------------|------|
| `Decibels` | This class contains some helpful static methods for dealing with decibel values | [ref](https://docs.juce.com/master/classjuce_1_1Decibels.html) |
| `FloatVectorOperations` | A collection of simple vector operations on arrays of floating point numbers, accelerated with SIMD instructions wher... | [ref](https://docs.juce.com/master/classjuce_1_1FloatVectorOperations.html) |
| `GenericInterpolator` | An interpolator base class for resampling streams of floats | [ref](https://docs.juce.com/master/classjuce_1_1GenericInterpolator.html) |
| `Interpolators` | A collection of different interpolators for resampling streams of floats | [ref](https://docs.juce.com/master/classjuce_1_1Interpolators.html) |

## Testing

| Class | Description | Docs |
|-------|-------------|------|
| `UnitTest` | This is a base class for classes that perform a unit test | [ref](https://docs.juce.com/master/classjuce_1_1UnitTest.html) |
| `UnitTestRunner` | Runs a set of unit tests | [ref](https://docs.juce.com/master/classjuce_1_1UnitTestRunner.html) |

## Other

| Class | Description | Docs |
|-------|-------------|------|
| `ADSR` | A very simple ADSR envelope class | [ref](https://docs.juce.com/master/classjuce_1_1ADSR.html) |
| `AlertWindow` | A window that displays a message and has buttons for the user to react to it | [ref](https://docs.juce.com/master/classjuce_1_1AlertWindow.html) |
| `Analytics` | A singleton class to manage analytics data | [ref](https://docs.juce.com/master/classjuce_1_1Analytics.html) |
| `AndroidDocument` | Provides access to a document on Android devices | [ref](https://docs.juce.com/master/classjuce_1_1AndroidDocument.html) |
| `AndroidDocumentInfo` | Some information about a document | [ref](https://docs.juce.com/master/classjuce_1_1AndroidDocumentInfo.html) |
| `AndroidDocumentInputSource` | An InputSource backed by an AndroidDocument | [ref](https://docs.juce.com/master/classjuce_1_1AndroidDocumentInputSource.html) |
| `AndroidDocumentIterator` | An iterator that visits child documents in a directory | [ref](https://docs.juce.com/master/classjuce_1_1AndroidDocumentIterator.html) |
| `AndroidDocumentPermission` | Represents a permission granted to an application to read and/or write to a particular document or tree | [ref](https://docs.juce.com/master/classjuce_1_1AndroidDocumentPermission.html) |
| `AnimatedPosition` | Models a 1-dimensional position that can be dragged around by the user, and which will then continue moving with a cu... | [ref](https://docs.juce.com/master/classjuce_1_1AnimatedPosition.html) |
| `AnimatedPosition::Listener` | Implement this class if you need to receive callbacks when the value of an AnimatedPosition changes | [ref](https://docs.juce.com/master/classjuce_1_1AnimatedPosition_1_1Listener.html) |
| `Animator` | Wrapper class for managing the lifetime of all the different animator kinds created through the builder classes | [ref](https://docs.juce.com/master/classjuce_1_1Animator.html) |
| `Animator::Weak` |  | [ref](https://docs.juce.com/master/classjuce_1_1Animator_1_1Weak.html) |
| `AnimatorSetBuilder` | A builder class that can be used to construct an Animator wrapping an AnimatorSet implementation | [ref](https://docs.juce.com/master/classjuce_1_1AnimatorSetBuilder.html) |
| `AnimatorUpdater` | Helper class to update several animators at once, without owning or otherwise extending the lifetimes of those animators | [ref](https://docs.juce.com/master/classjuce_1_1AnimatorUpdater.html) |
| `AppleRemoteDevice` | Receives events from an Apple IR remote control device (Only available in OSX!) | [ref](https://docs.juce.com/master/classjuce_1_1AppleRemoteDevice.html) |
| `ApplicationCommandManager` | One of these objects holds a list of all the commands your app can perform, and despatches these commands when needed | [ref](https://docs.juce.com/master/classjuce_1_1ApplicationCommandManager.html) |
| `ApplicationCommandManagerListener` | A listener that receives callbacks from an ApplicationCommandManager when commands are invoked or the command list is... | [ref](https://docs.juce.com/master/classjuce_1_1ApplicationCommandManagerListener.html) |
| `ApplicationCommandTarget` | A command target publishes a list of command IDs that it can perform | [ref](https://docs.juce.com/master/classjuce_1_1ApplicationCommandTarget.html) |
| `ApplicationProperties` | Manages a collection of properties | [ref](https://docs.juce.com/master/classjuce_1_1ApplicationProperties.html) |
| `AttributedString` | A text string with a set of colour/font settings that are associated with sub-ranges of the text | [ref](https://docs.juce.com/master/classjuce_1_1AttributedString.html) |
| `AttributedString::Attribute` | An attribute that has been applied to a range of characters in an AttributedString | [ref](https://docs.juce.com/master/classjuce_1_1AttributedString_1_1Attribute.html) |
| `AudioCDBurner` |  | [ref](https://docs.juce.com/master/classjuce_1_1AudioCDBurner.html) |
| `AudioCDBurner::BurnProgressListener` | Receives progress callbacks during a cd-burn operation | [ref](https://docs.juce.com/master/classjuce_1_1AudioCDBurner_1_1BurnProgressListener.html) |
| `AudioCDReader` | A type of AudioFormatReader that reads from an audio CD | [ref](https://docs.juce.com/master/classjuce_1_1AudioCDReader.html) |
| `AudioChannelSet` | Represents a set of audio channel types | [ref](https://docs.juce.com/master/classjuce_1_1AudioChannelSet.html) |
| `AudioData` | This class a container which holds all the classes pertaining to the AudioData::Pointer audio sample format class | [ref](https://docs.juce.com/master/classjuce_1_1AudioData.html) |
| `AudioData::Converter` | A base class for objects that are used to convert between two different sample formats | [ref](https://docs.juce.com/master/classjuce_1_1AudioData_1_1Converter.html) |
| `AudioData::ConverterInstance` | A class that converts between two templated AudioData::Pointer types, and which implements the AudioData::Converter i... | [ref](https://docs.juce.com/master/classjuce_1_1AudioData_1_1ConverterInstance.html) |
| `AudioIODevice` | Base class for an audio device with synchronised input and output channels | [ref](https://docs.juce.com/master/classjuce_1_1AudioIODevice.html) |
| `AudioIODeviceCallback` | One of these is passed to an AudioIODevice object to stream the audio data in and out | [ref](https://docs.juce.com/master/classjuce_1_1AudioIODeviceCallback.html) |
| `AudioIODeviceType` | Represents a type of audio driver, such as DirectSound, ASIO, CoreAudio, etc | [ref](https://docs.juce.com/master/classjuce_1_1AudioIODeviceType.html) |
| `AudioIODeviceType::Listener` | A class for receiving events when audio devices are inserted or removed | [ref](https://docs.juce.com/master/classjuce_1_1AudioIODeviceType_1_1Listener.html) |
| `AudioProcessLoadMeasurer` | Maintains an ongoing measurement of the proportion of time which is being spent inside an audio callback | [ref](https://docs.juce.com/master/classjuce_1_1AudioProcessLoadMeasurer.html) |
| `AudioSubsectionReader` | This class is used to wrap an AudioFormatReader and only read from a subsection of the file | [ref](https://docs.juce.com/master/classjuce_1_1AudioSubsectionReader.html) |
| `AudioUnitPluginFormat` | Implements a plugin format manager for AudioUnits | [ref](https://docs.juce.com/master/classjuce_1_1AudioUnitPluginFormat.html) |
| `AudioUnitPluginFormatHeadless` | Implements a plugin format manager for AudioUnits | [ref](https://docs.juce.com/master/classjuce_1_1AudioUnitPluginFormatHeadless.html) |
| `BigInteger` | An arbitrarily large integer class | [ref](https://docs.juce.com/master/classjuce_1_1BigInteger.html) |
| `BlowFish` | BlowFish encryption class | [ref](https://docs.juce.com/master/classjuce_1_1BlowFish.html) |
| `Box2DRenderer` | A simple implementation of the b2Draw class, used to draw a Box2D world | [ref](https://docs.juce.com/master/classjuce_1_1Box2DRenderer.html) |
| `BufferingAudioReader` | An AudioFormatReader that uses a background thread to pre-read data from another reader | [ref](https://docs.juce.com/master/classjuce_1_1BufferingAudioReader.html) |
| `ByteOrder` | Contains static methods for converting the byte order between different endiannesses | [ref](https://docs.juce.com/master/classjuce_1_1ByteOrder.html) |
| `BytestreamSysexExtractor` |  | [ref](https://docs.juce.com/master/classjuce_1_1BytestreamSysexExtractor.html) |
| `CPlusPlusCodeTokeniser` | A simple lexical analyser for syntax colouring of C++ code | [ref](https://docs.juce.com/master/classjuce_1_1CPlusPlusCodeTokeniser.html) |
| `CallOutBox` | A box with a small arrow that can be used as a temporary pop-up window to show extra controls when a button or other ... | [ref](https://docs.juce.com/master/classjuce_1_1CallOutBox.html) |
| `CallbackMessage` | A message that invokes a callback method when it gets delivered | [ref](https://docs.juce.com/master/classjuce_1_1CallbackMessage.html) |
| `CameraDevice` | Controls any video capture devices that might be available | [ref](https://docs.juce.com/master/classjuce_1_1CameraDevice.html) |
| `CameraDevice::Listener` | Receives callbacks with individual frames from a CameraDevice | [ref](https://docs.juce.com/master/classjuce_1_1CameraDevice_1_1Listener.html) |
| `CharacterFunctions` | A collection of functions for manipulating characters and character strings | [ref](https://docs.juce.com/master/classjuce_1_1CharacterFunctions.html) |
| `ChildProcess` | Launches and monitors a child process | [ref](https://docs.juce.com/master/classjuce_1_1ChildProcess.html) |
| `ChildProcessCoordinator` | Acts as the coordinator in a coordinator/worker pair of connected processes | [ref](https://docs.juce.com/master/classjuce_1_1ChildProcessCoordinator.html) |
| `ChildProcessManager` | Manages a set of ChildProcesses and periodically checks their return value | [ref](https://docs.juce.com/master/classjuce_1_1ChildProcessManager.html) |
| `ChildProcessWorker` | Acts as the worker end of a coordinator/worker pair of connected processes | [ref](https://docs.juce.com/master/classjuce_1_1ChildProcessWorker.html) |
| `CodeDocument` | A class for storing and manipulating a source code file | [ref](https://docs.juce.com/master/classjuce_1_1CodeDocument.html) |
| `CodeDocument::Iterator` | Iterates the text in a CodeDocument | [ref](https://docs.juce.com/master/classjuce_1_1CodeDocument_1_1Iterator.html) |
| `CodeDocument::Listener` | An object that receives callbacks from the CodeDocument when its text changes | [ref](https://docs.juce.com/master/classjuce_1_1CodeDocument_1_1Listener.html) |
| `CodeDocument::Position` | A position in a code document | [ref](https://docs.juce.com/master/classjuce_1_1CodeDocument_1_1Position.html) |
| `CodeTokeniser` | A base class for tokenising code so that the syntax can be displayed in a code editor | [ref](https://docs.juce.com/master/classjuce_1_1CodeTokeniser.html) |
| `ConcertinaPanel` | A panel which holds a vertical stack of components which can be expanded and contracted | [ref](https://docs.juce.com/master/classjuce_1_1ConcertinaPanel.html) |
| `ContentSharer` | Functions that allow sharing content between apps and devices | [ref](https://docs.juce.com/master/classjuce_1_1ContentSharer.html) |
| `CopyableHeapBlock` | Wraps a HeapBlock, but additionally provides a copy constructor and remembers its size | [ref](https://docs.juce.com/master/classjuce_1_1CopyableHeapBlock.html) |
| `DarkModeSettingListener` | Classes can implement this interface and register themselves with the Desktop class to receive callbacks when the ope... | [ref](https://docs.juce.com/master/classjuce_1_1DarkModeSettingListener.html) |
| `DatagramSocket` | A wrapper for a datagram (UDP) socket | [ref](https://docs.juce.com/master/classjuce_1_1DatagramSocket.html) |
| `DefaultElementComparator` | A simple ElementComparator class that can be used to sort an array of objects that support the '<' operator | [ref](https://docs.juce.com/master/classjuce_1_1DefaultElementComparator.html) |
| `DeletedAtShutdown` | Classes derived from this will be automatically deleted when the application exits | [ref](https://docs.juce.com/master/classjuce_1_1DeletedAtShutdown.html) |
| `Desktop` | Describes and controls aspects of the computer's desktop | [ref](https://docs.juce.com/master/classjuce_1_1Desktop.html) |
| `DialogWindow` | A dialog-box style window | [ref](https://docs.juce.com/master/classjuce_1_1DialogWindow.html) |
| `DirectoryContentsList` | A class to asynchronously scan for details about the files in a directory | [ref](https://docs.juce.com/master/classjuce_1_1DirectoryContentsList.html) |
| `DirectoryEntry` | Describes the attributes of a file or folder | [ref](https://docs.juce.com/master/classjuce_1_1DirectoryEntry.html) |
| `Displays` | Manages details about connected display devices | [ref](https://docs.juce.com/master/classjuce_1_1Displays.html) |
| `DocumentWindow` | A resizable window with a title bar and maximise, minimise and close buttons | [ref](https://docs.juce.com/master/classjuce_1_1DocumentWindow.html) |
| `DragAndDropContainer` | Enables drag-and-drop behaviour for a component and all its sub-components | [ref](https://docs.juce.com/master/classjuce_1_1DragAndDropContainer.html) |
| `DragAndDropTarget` | Components derived from this class can have things dropped onto them by a DragAndDropContainer | [ref](https://docs.juce.com/master/classjuce_1_1DragAndDropTarget.html) |
| `DragAndDropTarget::SourceDetails` | Contains details about the source of a drag-and-drop operation | [ref](https://docs.juce.com/master/classjuce_1_1DragAndDropTarget_1_1SourceDetails.html) |
| `Draggable3DOrientation` | Stores a 3D orientation, which can be rotated by dragging with the mouse | [ref](https://docs.juce.com/master/classjuce_1_1Draggable3DOrientation.html) |
| `Drawable` | The base class for objects which can draw themselves, e.g | [ref](https://docs.juce.com/master/classjuce_1_1Drawable.html) |
| `DrawableComposite` | A drawable object which acts as a container for a set of other Drawables | [ref](https://docs.juce.com/master/classjuce_1_1DrawableComposite.html) |
| `DrawableShape` | A base class implementing common functionality for Drawable classes which consist of some kind of filled and stroked ... | [ref](https://docs.juce.com/master/classjuce_1_1DrawableShape.html) |
| `DrawableText` | A drawable object which renders a line of text | [ref](https://docs.juce.com/master/classjuce_1_1DrawableText.html) |
| `DynamicLibrary` | Handles the opening and closing of DLLs | [ref](https://docs.juce.com/master/classjuce_1_1DynamicLibrary.html) |
| `DynamicObject` | Represents a dynamically implemented object | [ref](https://docs.juce.com/master/classjuce_1_1DynamicObject.html) |
| `EdgeTable` | A table of horizontal scan-line segments - used for rasterising Paths | [ref](https://docs.juce.com/master/classjuce_1_1EdgeTable.html) |
| `EnumerateIterator` | An iterator that wraps some other iterator, keeping track of the relative position of that iterator based on calls to... | [ref](https://docs.juce.com/master/classjuce_1_1EnumerateIterator.html) |
| `ErasedScopeGuard` | A ScopeGuard that uses a std::function internally to allow type erasure | [ref](https://docs.juce.com/master/classjuce_1_1ErasedScopeGuard.html) |
| `Expression` | A class for dynamically evaluating simple numeric expressions | [ref](https://docs.juce.com/master/classjuce_1_1Expression.html) |
| `Expression::Scope` | When evaluating an Expression object, this class is used to resolve symbols and perform functions that the expression... | [ref](https://docs.juce.com/master/classjuce_1_1Expression_1_1Scope.html) |
| `Expression::Scope::Visitor` | Used as a callback by the Scope::visitRelativeScope() method | [ref](https://docs.juce.com/master/classjuce_1_1Expression_1_1Scope_1_1Visitor.html) |
| `FillType` | Represents a colour or fill pattern to use for rendering paths | [ref](https://docs.juce.com/master/classjuce_1_1FillType.html) |
| `FixedSizeFunction_3_01len_00_01Ret_07Args_8_8_8_08_4` | A type similar to std::function that holds a callable object | [ref](https://docs.juce.com/master/classjuce_1_1FixedSizeFunction_3_01len_00_01Ret_07Args_8_8_8_08_4.html) |
| `FocusOutline` | Adds a focus outline to a component | [ref](https://docs.juce.com/master/classjuce_1_1FocusOutline.html) |
| `FocusTraverser` | Controls the order in which focus moves between components | [ref](https://docs.juce.com/master/classjuce_1_1FocusTraverser.html) |
| `FromVar` | Allows converting a var to an object of arbitrary type | [ref](https://docs.juce.com/master/classjuce_1_1FromVar.html) |
| `GenericScopedLock` | Automatically locks and unlocks a mutex object | [ref](https://docs.juce.com/master/classjuce_1_1GenericScopedLock.html) |
| `GenericScopedTryLock` | Automatically locks and unlocks a mutex object | [ref](https://docs.juce.com/master/classjuce_1_1GenericScopedTryLock.html) |
| `GenericScopedUnlock` | Automatically unlocks and re-locks a mutex object | [ref](https://docs.juce.com/master/classjuce_1_1GenericScopedUnlock.html) |
| `GlowEffect` | A component effect that adds a coloured blur around the component's contents | [ref](https://docs.juce.com/master/classjuce_1_1GlowEffect.html) |
| `HeapBlock` | Very simple container class to hold a pointer to some data on the heap | [ref](https://docs.juce.com/master/classjuce_1_1HeapBlock.html) |
| `HeavyweightLeakedObjectDetector` | This class is a useful way of tracking down hard to find memory leaks when the regular LeakedObjectDetector isn't enough | [ref](https://docs.juce.com/master/classjuce_1_1HeavyweightLeakedObjectDetector.html) |
| `IIRCoefficients` | A set of coefficients for use in an IIRFilter object | [ref](https://docs.juce.com/master/classjuce_1_1IIRCoefficients.html) |
| `IIRFilter` | An IIR filter that can perform low, high, or band-pass filtering on an audio signal, and which attempts to implement ... | [ref](https://docs.juce.com/master/classjuce_1_1IIRFilter.html) |
| `IIRFilterBase` | An IIR filter that can perform low, high, or band-pass filtering on an audio signal | [ref](https://docs.juce.com/master/classjuce_1_1IIRFilterBase.html) |
| `IPAddress` | Represents an IP address | [ref](https://docs.juce.com/master/classjuce_1_1IPAddress.html) |
| `InAppPurchases` | Provides in-app purchase functionality | [ref](https://docs.juce.com/master/classjuce_1_1InAppPurchases.html) |
| `InputSource` | A lightweight object that can create a stream to read some kind of resource | [ref](https://docs.juce.com/master/classjuce_1_1InputSource.html) |
| `InterProcessLock` | Acts as a critical section which processes can use to block each other | [ref](https://docs.juce.com/master/classjuce_1_1InterProcessLock.html) |
| `InterProcessLock::ScopedLockType` | Automatically locks and unlocks an InterProcessLock object | [ref](https://docs.juce.com/master/classjuce_1_1InterProcessLock_1_1ScopedLockType.html) |
| `InterprocessConnection` | Manages a simple two-way messaging connection to another process, using either a socket or a named pipe as the transp... | [ref](https://docs.juce.com/master/classjuce_1_1InterprocessConnection.html) |
| `InterprocessConnectionServer` | An object that waits for client sockets to connect to a port on this host, and creates InterprocessConnection objects... | [ref](https://docs.juce.com/master/classjuce_1_1InterprocessConnectionServer.html) |
| `IteratorPair` | Wraps a pair of iterators, providing member begin() and end() functions that return those iterators | [ref](https://docs.juce.com/master/classjuce_1_1IteratorPair.html) |
| `JSCursor` | A high-level wrapper around an owning root JSObject and a hierarchical path relative to it | [ref](https://docs.juce.com/master/classjuce_1_1JSCursor.html) |
| `JSON` | Contains static methods for converting JSON-formatted text to and from var objects | [ref](https://docs.juce.com/master/classjuce_1_1JSON.html) |
| `JSON::FormatOptions` | Allows formatting var objects as JSON with various configurable options | [ref](https://docs.juce.com/master/classjuce_1_1JSON_1_1FormatOptions.html) |
| `JSObject` | A JSObject represents an owning reference to the underlying JS object, meaning it will remain valid even if a subsequ... | [ref](https://docs.juce.com/master/classjuce_1_1JSObject.html) |
| `JUCEApplication` | An instance of this class is used to specify initialisation and shutdown code for the application | [ref](https://docs.juce.com/master/classjuce_1_1JUCEApplication.html) |
| `JUCEApplicationBase` | Abstract base class for application classes | [ref](https://docs.juce.com/master/classjuce_1_1JUCEApplicationBase.html) |
| `JavascriptEngine` | This class is a wrapper around QuickJS, an ES2023 compliant, embeddable javascript engine | [ref](https://docs.juce.com/master/classjuce_1_1JavascriptEngine.html) |
| `KeyGeneration` | Contains static utilities for generating key-files that can be unlocked by the OnlineUnlockStatus class | [ref](https://docs.juce.com/master/classjuce_1_1KeyGeneration.html) |
| `KeyListener` | Receives callbacks when keys are pressed | [ref](https://docs.juce.com/master/classjuce_1_1KeyListener.html) |
| `KeyPress` | Represents a key press, including any modifier keys that are needed | [ref](https://docs.juce.com/master/classjuce_1_1KeyPress.html) |
| `KeyPressMappingSet` | Manages and edits a list of keypresses, which it uses to invoke the appropriate command in an ApplicationCommandManager | [ref](https://docs.juce.com/master/classjuce_1_1KeyPressMappingSet.html) |
| `KeyboardFocusTraverser` | Controls the order in which keyboard focus moves between components | [ref](https://docs.juce.com/master/classjuce_1_1KeyboardFocusTraverser.html) |
| `KnownPluginList` | Manages a list of plugin types | [ref](https://docs.juce.com/master/classjuce_1_1KnownPluginList.html) |
| `KnownPluginList::CustomScanner` | Class to define a custom plugin scanner | [ref](https://docs.juce.com/master/classjuce_1_1KnownPluginList_1_1CustomScanner.html) |
| `LADSPAPluginFormat` | Provided for backwards compatibility; LADSPA plugins are always headless | [ref](https://docs.juce.com/master/classjuce_1_1LADSPAPluginFormat.html) |
| `LADSPAPluginFormatHeadless` | Implements a plugin format manager for LADSPA plugins | [ref](https://docs.juce.com/master/classjuce_1_1LADSPAPluginFormatHeadless.html) |
| `LV2PluginFormat` | Implements a plugin format for LV2 plugins | [ref](https://docs.juce.com/master/classjuce_1_1LV2PluginFormat.html) |
| `LV2PluginFormatHeadless` | Implements a plugin format for LV2 plugins | [ref](https://docs.juce.com/master/classjuce_1_1LV2PluginFormatHeadless.html) |
| `LassoSource` | A class used by the LassoComponent to manage the things that it selects | [ref](https://docs.juce.com/master/classjuce_1_1LassoSource.html) |
| `LeakedObjectDetector` | Embedding an instance of this class inside another class can be used as a low-overhead way of detecting leaked instances | [ref](https://docs.juce.com/master/classjuce_1_1LeakedObjectDetector.html) |
| `LightweightListenerList` | A lightweight version of the ListenerList that doesn't provide any guarantees when mutating the list from a callback,... | [ref](https://docs.juce.com/master/classjuce_1_1LightweightListenerList.html) |
| `ListenerList` | Holds a set of objects and can invoke a member function callback on each object in the set with a single call | [ref](https://docs.juce.com/master/classjuce_1_1ListenerList.html) |
| `LocalisedStrings` | Used to convert strings to localised foreign-language versions | [ref](https://docs.juce.com/master/classjuce_1_1LocalisedStrings.html) |
| `Logger` | Acts as an application-wide logging class | [ref](https://docs.juce.com/master/classjuce_1_1Logger.html) |
| `LuaTokeniser` |  | [ref](https://docs.juce.com/master/classjuce_1_1LuaTokeniser.html) |
| `MACAddress` | Represents a MAC network card adapter address ID | [ref](https://docs.juce.com/master/classjuce_1_1MACAddress.html) |
| `MD5` | MD5 checksum class | [ref](https://docs.juce.com/master/classjuce_1_1MD5.html) |
| `MarkerList` | Holds a set of named marker points along a one-dimensional axis | [ref](https://docs.juce.com/master/classjuce_1_1MarkerList.html) |
| `MarkerList::Listener` | A class for receiving events when changes are made to a MarkerList | [ref](https://docs.juce.com/master/classjuce_1_1MarkerList_1_1Listener.html) |
| `MarkerList::Marker` | Represents a marker in a MarkerList | [ref](https://docs.juce.com/master/classjuce_1_1MarkerList_1_1Marker.html) |
| `Matrix3D` | A 4x4 3D transformation matrix | [ref](https://docs.juce.com/master/classjuce_1_1Matrix3D.html) |
| `Message` | The base class for objects that can be sent to a MessageListener | [ref](https://docs.juce.com/master/classjuce_1_1Message.html) |
| `MessageBoxOptions` | Class used to create a set of options to pass to the AlertWindow and NativeMessageBox methods for showing dialog boxes | [ref](https://docs.juce.com/master/classjuce_1_1MessageBoxOptions.html) |
| `MessageListener` | MessageListener subclasses can post and receive Message objects | [ref](https://docs.juce.com/master/classjuce_1_1MessageListener.html) |
| `ModalCallbackFunction` | This class provides some handy utility methods for creating ModalComponentManager::Callback objects that will invoke ... | [ref](https://docs.juce.com/master/classjuce_1_1ModalCallbackFunction.html) |
| `ModifierKeys` | Represents the state of the mouse buttons and modifier keys | [ref](https://docs.juce.com/master/classjuce_1_1ModifierKeys.html) |
| `MountedVolumeListChangeDetector` | An instance of this class will provide callbacks when drives are mounted or unmounted on the system | [ref](https://docs.juce.com/master/classjuce_1_1MountedVolumeListChangeDetector.html) |
| `MouseCursor` | Represents a mouse cursor image | [ref](https://docs.juce.com/master/classjuce_1_1MouseCursor.html) |
| `MouseEvent` | Contains position and status information about a mouse event | [ref](https://docs.juce.com/master/classjuce_1_1MouseEvent.html) |
| `MouseInactivityDetector` | This object watches for mouse-events happening within a component, and if the mouse remains still for long enough, tr... | [ref](https://docs.juce.com/master/classjuce_1_1MouseInactivityDetector.html) |
| `MouseInactivityDetector::Listener` | Classes should implement this to receive callbacks from a MouseInactivityDetector when the mouse becomes active or in... | [ref](https://docs.juce.com/master/classjuce_1_1MouseInactivityDetector_1_1Listener.html) |
| `MouseInputSource` | Represents a linear source of mouse events from a mouse device or individual finger in a multi-touch environment | [ref](https://docs.juce.com/master/classjuce_1_1MouseInputSource.html) |
| `MouseListener` | A MouseListener can be registered with a component to receive callbacks about mouse events that happen to that component | [ref](https://docs.juce.com/master/classjuce_1_1MouseListener.html) |
| `MultiDocumentPanel` | A component that contains a set of other components either in floating windows or tabs | [ref](https://docs.juce.com/master/classjuce_1_1MultiDocumentPanel.html) |
| `MultiDocumentPanelWindow` | This is a derivative of DocumentWindow that is used inside a MultiDocumentPanel component | [ref](https://docs.juce.com/master/classjuce_1_1MultiDocumentPanelWindow.html) |
| `NamedPipe` | A cross-process pipe that can have data written to and read from it | [ref](https://docs.juce.com/master/classjuce_1_1NamedPipe.html) |
| `NativeMessageBox` | This class contains some static methods for showing native alert windows | [ref](https://docs.juce.com/master/classjuce_1_1NativeMessageBox.html) |
| `NativeScaleFactorNotifier` | Calls a function every time the native scale factor of a component's peer changes | [ref](https://docs.juce.com/master/classjuce_1_1NativeScaleFactorNotifier.html) |
| `OnlineUnlockForm` | Acts as a GUI which asks the user for their details, and calls the appropriate methods on your OnlineUnlockStatus obj... | [ref](https://docs.juce.com/master/classjuce_1_1OnlineUnlockForm.html) |
| `OnlineUnlockStatus` | A base class for online unlocking systems | [ref](https://docs.juce.com/master/classjuce_1_1OnlineUnlockStatus.html) |
| `Optional` | A simple optional type | [ref](https://docs.juce.com/master/classjuce_1_1Optional.html) |
| `OptionsBuilder` | A base class for building Options | [ref](https://docs.juce.com/master/classjuce_1_1OptionsBuilder.html) |
| `Parallelogram` | Represents a parallelogram that is defined by 3 points | [ref](https://docs.juce.com/master/classjuce_1_1Parallelogram.html) |
| `ParameterAttachment` | Used to implement 'attachments' or 'controllers' that link a plug-in parameter to a UI element | [ref](https://docs.juce.com/master/classjuce_1_1ParameterAttachment.html) |
| `ParameterID` | Combines a parameter ID and a version hint | [ref](https://docs.juce.com/master/classjuce_1_1ParameterID.html) |
| `PerformanceCounter` | A timer for measuring performance of code and dumping the results to a file | [ref](https://docs.juce.com/master/classjuce_1_1PerformanceCounter.html) |
| `PixelARGB` | Represents a 32-bit INTERNAL pixel with premultiplied alpha, and can perform compositing operations with it | [ref](https://docs.juce.com/master/classjuce_1_1PixelARGB.html) |
| `PixelAlpha` | Represents an 8-bit single-channel pixel, and can perform compositing operations on it | [ref](https://docs.juce.com/master/classjuce_1_1PixelAlpha.html) |
| `PixelRGB` | Represents a 24-bit RGB pixel, and can perform compositing operations on it | [ref](https://docs.juce.com/master/classjuce_1_1PixelRGB.html) |
| `PluginDescription` | A small class to represent some facts about a particular type of plug-in | [ref](https://docs.juce.com/master/classjuce_1_1PluginDescription.html) |
| `PluginDirectoryScanner` | Scans a directory for plugins, and adds them to a KnownPluginList | [ref](https://docs.juce.com/master/classjuce_1_1PluginDirectoryScanner.html) |
| `PluginHostType` | A useful utility class to determine the host or DAW in which your plugin is loaded | [ref](https://docs.juce.com/master/classjuce_1_1PluginHostType.html) |
| `PreferencesPanel` | A component with a set of buttons at the top for changing between pages of preferences | [ref](https://docs.juce.com/master/classjuce_1_1PreferencesPanel.html) |
| `Primes` | Prime number creation class | [ref](https://docs.juce.com/master/classjuce_1_1Primes.html) |
| `Process` | Represents the current executable's process | [ref](https://docs.juce.com/master/classjuce_1_1Process.html) |
| `ProgressBar` | A progress bar component | [ref](https://docs.juce.com/master/classjuce_1_1ProgressBar.html) |
| `PropertySet` | A set of named property values, which can be strings, integers, floating point, etc | [ref](https://docs.juce.com/master/classjuce_1_1PropertySet.html) |
| `PushNotifications` | Singleton class responsible for push notifications functionality | [ref](https://docs.juce.com/master/classjuce_1_1PushNotifications.html) |
| `Quaternion` | Holds a quaternion (a 3D vector and a scalar value) | [ref](https://docs.juce.com/master/classjuce_1_1Quaternion.html) |
| `RSAKey` | RSA public/private key-pair encryption class | [ref](https://docs.juce.com/master/classjuce_1_1RSAKey.html) |
| `Random` | A random number generator | [ref](https://docs.juce.com/master/classjuce_1_1Random.html) |
| `RelativeCoordinate` | Expresses a coordinate as a dynamically evaluated expression | [ref](https://docs.juce.com/master/classjuce_1_1RelativeCoordinate.html) |
| `RelativeCoordinatePositionerBase` | Base class for Component::Positioners that are based upon relative coordinates | [ref](https://docs.juce.com/master/classjuce_1_1RelativeCoordinatePositionerBase.html) |
| `RelativeParallelogram` | A parallelogram defined by three RelativePoint positions | [ref](https://docs.juce.com/master/classjuce_1_1RelativeParallelogram.html) |
| `RelativeTime` | A relative measure of time | [ref](https://docs.juce.com/master/classjuce_1_1RelativeTime.html) |
| `ResizableWindow` | A base class for top-level windows that can be dragged around and resized | [ref](https://docs.juce.com/master/classjuce_1_1ResizableWindow.html) |
| `Result` | Represents the 'success' or 'failure' of an operation, and holds an associated error message to describe the error wh... | [ref](https://docs.juce.com/master/classjuce_1_1Result.html) |
| `Reverb` | Performs a simple reverb effect on a stream of audio data | [ref](https://docs.juce.com/master/classjuce_1_1Reverb.html) |
| `RuntimePermissions` |  | [ref](https://docs.juce.com/master/classjuce_1_1RuntimePermissions.html) |
| `SHA256` | SHA-256 secure hash generator | [ref](https://docs.juce.com/master/classjuce_1_1SHA256.html) |
| `SamplerSound` | A subclass of SynthesiserSound that represents a sampled audio clip | [ref](https://docs.juce.com/master/classjuce_1_1SamplerSound.html) |
| `SamplerVoice` | A subclass of SynthesiserVoice that can play a SamplerSound | [ref](https://docs.juce.com/master/classjuce_1_1SamplerVoice.html) |
| `ScopedAutoReleasePool` | A handy C++ wrapper that creates and deletes an NSAutoreleasePool object using RAII | [ref](https://docs.juce.com/master/classjuce_1_1ScopedAutoReleasePool.html) |
| `ScopedJuceInitialiser__GUI` | A utility object that helps you initialise and shutdown JUCE correctly using an RAII pattern | [ref](https://docs.juce.com/master/classjuce_1_1ScopedJuceInitialiser__GUI.html) |
| `ScopedMessageBox` | Objects of this type can be used to programmatically close message boxes | [ref](https://docs.juce.com/master/classjuce_1_1ScopedMessageBox.html) |
| `ScopedNoDenormals` | Helper class providing an RAII-based mechanism for temporarily disabling denormals on your CPU | [ref](https://docs.juce.com/master/classjuce_1_1ScopedNoDenormals.html) |
| `ScopedReadLock` | Automatically locks and unlocks a ReadWriteLock object | [ref](https://docs.juce.com/master/classjuce_1_1ScopedReadLock.html) |
| `ScopedTimeMeasurement` | Simple RAII class for measuring the time spent in a scope | [ref](https://docs.juce.com/master/classjuce_1_1ScopedTimeMeasurement.html) |
| `ScopedTryReadLock` | Automatically locks and unlocks a ReadWriteLock object | [ref](https://docs.juce.com/master/classjuce_1_1ScopedTryReadLock.html) |
| `ScopedTryWriteLock` | Automatically locks and unlocks a ReadWriteLock object | [ref](https://docs.juce.com/master/classjuce_1_1ScopedTryWriteLock.html) |
| `ScopedWriteLock` | Automatically locks and unlocks a ReadWriteLock object | [ref](https://docs.juce.com/master/classjuce_1_1ScopedWriteLock.html) |
| `SelectedItemSet` | Manages a list of selectable items | [ref](https://docs.juce.com/master/classjuce_1_1SelectedItemSet.html) |
| `SettableTooltipClient` | An implementation of TooltipClient that stores the tooltip string and a method for changing it | [ref](https://docs.juce.com/master/classjuce_1_1SettableTooltipClient.html) |
| `SidePanel` | A component that is positioned on either the left- or right-hand side of its parent, containing a header and some con... | [ref](https://docs.juce.com/master/classjuce_1_1SidePanel.html) |
| `SocketOptions` | Options used for the configuration of the underlying system socket in the StreamingSocket and DatagramSocket classes | [ref](https://docs.juce.com/master/classjuce_1_1SocketOptions.html) |
| `SortedSet` | Holds a set of unique primitive objects, such as ints or doubles | [ref](https://docs.juce.com/master/classjuce_1_1SortedSet.html) |
| `SoundPlayer` | A simple sound player that you can add to the AudioDeviceManager to play simple sounds | [ref](https://docs.juce.com/master/classjuce_1_1SoundPlayer.html) |
| `Span` | A non-owning view over contiguous objects stored in an Array or vector or other similar container | [ref](https://docs.juce.com/master/classjuce_1_1Span.html) |
| `SparseSet` | Holds a set of primitive values, storing them as a set of ranges | [ref](https://docs.juce.com/master/classjuce_1_1SparseSet.html) |
| `SpeakerMappings::VstSpeakerConfigurationHolder` | Class to hold a speaker configuration | [ref](https://docs.juce.com/master/classjuce_1_1SpeakerMappings_1_1VstSpeakerConfigurationHolder.html) |
| `SplashScreen` | A component for showing a splash screen while your app starts up | [ref](https://docs.juce.com/master/classjuce_1_1SplashScreen.html) |
| `SpringEasingOptions` | A selection of options available for customising a spring style easing function | [ref](https://docs.juce.com/master/classjuce_1_1SpringEasingOptions.html) |
| `StandaloneFilterWindow` | A class that can be used to run a simple standalone application containing your filter | [ref](https://docs.juce.com/master/classjuce_1_1StandaloneFilterWindow.html) |
| `StandalonePluginHolder` | An object that creates and plays a standalone instance of an AudioProcessor | [ref](https://docs.juce.com/master/classjuce_1_1StandalonePluginHolder.html) |
| `StaticAnimationLimits` | Helper class for using linear interpolation between a begin and an end value | [ref](https://docs.juce.com/master/classjuce_1_1StaticAnimationLimits.html) |
| `StatisticsAccumulator` | A class that measures various statistics about a series of floating point values that it is given | [ref](https://docs.juce.com/master/classjuce_1_1StatisticsAccumulator.html) |
| `StreamingSocket` | A wrapper for a streaming (TCP) socket | [ref](https://docs.juce.com/master/classjuce_1_1StreamingSocket.html) |
| `StretchableLayoutManager` | For laying out a set of components, where the components have preferred sizes and size limits, but where they are all... | [ref](https://docs.juce.com/master/classjuce_1_1StretchableLayoutManager.html) |
| `StretchableLayoutResizerBar` | A component that acts as one of the vertical or horizontal bars you see being used to resize panels in a window | [ref](https://docs.juce.com/master/classjuce_1_1StretchableLayoutResizerBar.html) |
| `StretchableObjectResizer` | A utility class for fitting a set of objects whose sizes can vary between a minimum and maximum size, into a space | [ref](https://docs.juce.com/master/classjuce_1_1StretchableObjectResizer.html) |
| `String` | The JUCE String class! | [ref](https://docs.juce.com/master/classjuce_1_1String.html) |
| `StringPool` | A StringPool holds a set of shared strings, which reduces storage overheads and improves comparison speed when dealin... | [ref](https://docs.juce.com/master/classjuce_1_1StringPool.html) |
| `StringRef` | A simple class for holding temporary references to a string literal or String | [ref](https://docs.juce.com/master/classjuce_1_1StringRef.html) |
| `SubregionStream` | Wraps another input stream, and reads from a specific part of it | [ref](https://docs.juce.com/master/classjuce_1_1SubregionStream.html) |
| `SystemAudioVolume` | Contains functions to control the system's master volume | [ref](https://docs.juce.com/master/classjuce_1_1SystemAudioVolume.html) |
| `SystemClipboard` | Handles reading/writing to the system's clipboard | [ref](https://docs.juce.com/master/classjuce_1_1SystemClipboard.html) |
| `SystemStats` | Contains methods for finding out about the current hardware and OS configuration | [ref](https://docs.juce.com/master/classjuce_1_1SystemStats.html) |
| `TextDiff` | Calculates and applies a sequence of changes to convert one text string into another | [ref](https://docs.juce.com/master/classjuce_1_1TextDiff.html) |
| `TextDragAndDropTarget` | Components derived from this class can have text dropped onto them by an external application | [ref](https://docs.juce.com/master/classjuce_1_1TextDragAndDropTarget.html) |
| `TextInputTarget` | An abstract base class which can be implemented by components that function as text editors | [ref](https://docs.juce.com/master/classjuce_1_1TextInputTarget.html) |
| `TextLayout` | A Pre-formatted piece of text, which may contain multiple fonts and colours | [ref](https://docs.juce.com/master/classjuce_1_1TextLayout.html) |
| `TextLayout::Run` | A sequence of glyphs with a common font and colour | [ref](https://docs.juce.com/master/classjuce_1_1TextLayout_1_1Run.html) |
| `Time` | Holds an absolute date and time | [ref](https://docs.juce.com/master/classjuce_1_1Time.html) |
| `TimeSliceClient` | Used by the TimeSliceThread class | [ref](https://docs.juce.com/master/classjuce_1_1TimeSliceClient.html) |
| `TimedCallback` | Utility class wrapping a single non-null callback called by a Timer | [ref](https://docs.juce.com/master/classjuce_1_1TimedCallback.html) |
| `TimedDiagnostic` | An object for storing and measuring durations for diagnostic purposes | [ref](https://docs.juce.com/master/classjuce_1_1TimedDiagnostic.html) |
| `ToVar` | Allows converting an object of arbitrary type to var | [ref](https://docs.juce.com/master/classjuce_1_1ToVar.html) |
| `ToVarOptions` | Options that control conversion from arbitrary types to juce::var | [ref](https://docs.juce.com/master/classjuce_1_1ToVarOptions.html) |
| `Tolerance` | A class encapsulating both relative and absolute tolerances for use in floating-point comparisons | [ref](https://docs.juce.com/master/classjuce_1_1Tolerance.html) |
| `TooltipClient` | Components that want to use pop-up tooltips should implement this interface | [ref](https://docs.juce.com/master/classjuce_1_1TooltipClient.html) |
| `TooltipWindow` | A window that displays a pop-up tooltip when the mouse hovers over another component | [ref](https://docs.juce.com/master/classjuce_1_1TooltipWindow.html) |
| `TopLevelWindow` | A base class for top-level windows | [ref](https://docs.juce.com/master/classjuce_1_1TopLevelWindow.html) |
| `TracktionMarketplaceStatus` | An implementation of the OnlineUnlockStatus class which talks to the Tracktion Marketplace server | [ref](https://docs.juce.com/master/classjuce_1_1TracktionMarketplaceStatus.html) |
| `UndoableAction` | Used by the UndoManager class to store an action which can be done and undone | [ref](https://docs.juce.com/master/classjuce_1_1UndoableAction.html) |
| `Uuid` | A universally unique 128-bit identifier | [ref](https://docs.juce.com/master/classjuce_1_1Uuid.html) |
| `VBlankAnimatorUpdater` | Similar to AnimatorUpdater, but automatically calls update() whenever the screen refreshes | [ref](https://docs.juce.com/master/classjuce_1_1VBlankAnimatorUpdater.html) |
| `VBlankAttachment` | Helper class to synchronise Component updates to the vertical blank event of the display that the Component is presen... | [ref](https://docs.juce.com/master/classjuce_1_1VBlankAttachment.html) |
| `VST3PluginFormatHeadless` | Implements a plugin format for VST3s | [ref](https://docs.juce.com/master/classjuce_1_1VST3PluginFormatHeadless.html) |
| `VSTPluginFormat` | Implements a plugin format manager for VSTs | [ref](https://docs.juce.com/master/classjuce_1_1VSTPluginFormat.html) |
| `VSTPluginFormatHeadless` | Implements a plugin format manager for VSTs | [ref](https://docs.juce.com/master/classjuce_1_1VSTPluginFormatHeadless.html) |
| `Vector3D` | A three-coordinate vector | [ref](https://docs.juce.com/master/classjuce_1_1Vector3D.html) |
| `Viewport` | A Viewport is used to contain a larger child component, and allows the child to be automatically scrolled around | [ref](https://docs.juce.com/master/classjuce_1_1Viewport.html) |
| `WaitFreeListeners` |  | [ref](https://docs.juce.com/master/classjuce_1_1WaitFreeListeners.html) |
| `WeakReference` | This class acts as a pointer which will automatically become null if the object to which it points is deleted | [ref](https://docs.juce.com/master/classjuce_1_1WeakReference.html) |
| `WeakReference::Master` | This class is embedded inside an object to which you want to attach WeakReference pointers | [ref](https://docs.juce.com/master/classjuce_1_1WeakReference_1_1Master.html) |
| `Whirlpool` | Whirlpool hash class | [ref](https://docs.juce.com/master/classjuce_1_1Whirlpool.html) |
| `WindowsRegistry` | Contains some static helper functions for manipulating the MS Windows registry (Only available on Windows, of course!) | [ref](https://docs.juce.com/master/classjuce_1_1WindowsRegistry.html) |
| `WorkgroupToken` | Created by AudioWorkgroup to join the calling thread to a workgroup | [ref](https://docs.juce.com/master/classjuce_1_1WorkgroupToken.html) |
| `XmlDocument` | Parses a text-based XML document and creates an XmlElement object from it | [ref](https://docs.juce.com/master/classjuce_1_1XmlDocument.html) |
| `XmlElement` | Used to build a tree of elements representing an XML document | [ref](https://docs.juce.com/master/classjuce_1_1XmlElement.html) |
| `XmlTokeniser` |  | [ref](https://docs.juce.com/master/classjuce_1_1XmlTokeniser.html) |
| `midi__ci::BlockProfileStates` | Contains profile states for each group and channel in a function block, along with the state of profiles that apply t... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1BlockProfileStates.html) |
| `midi__ci::BufferOutput` | Represents a destination into which MIDI-CI messages can be written | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1BufferOutput.html) |
| `midi__ci::CacheProvider` | An interface for objects that provide resources for property exchange transactions | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1CacheProvider.html) |
| `midi__ci::ChannelAddress` | Identifies a channel or set of channels in a multi-group MIDI endpoint | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ChannelAddress.html) |
| `midi__ci::ChannelProfileStates` | Holds the number of channels that are supported and activated for all profiles at a particular channel address | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ChannelProfileStates.html) |
| `midi__ci::Device` | Instances of this type are responsible for parsing and interpreting incoming MIDI-CI messages, and for sending MIDI-C... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1Device.html) |
| `midi__ci::DeviceFeatures` | Flags indicating the features that are supported by a given CI device | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1DeviceFeatures.html) |
| `midi__ci::DeviceOptions` | Configuration options for a Device | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1DeviceOptions.html) |
| `midi__ci::GroupProfileStates` | Contains profile states for each channel in a group, along with the state of profiles that apply to the group itself | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1GroupProfileStates.html) |
| `midi__ci::InitiatorPropertyExchangeCache` | Accumulates message chunks that have been sent by another device in response to a transaction initiated by a local de... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1InitiatorPropertyExchangeCache.html) |
| `midi__ci::MUID` | A 28-bit ID that uniquely identifies a device taking part in a series of MIDI-CI transactions | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1MUID.html) |
| `midi__ci::Parser` | Parses CI messages | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1Parser.html) |
| `midi__ci::ProfileAtAddress` | Holds a profile ID, and the address of a group/channel | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ProfileAtAddress.html) |
| `midi__ci::ProfileHost` | Acting as a ResponderListener, instances of this class can formulate appropriate replies to profile transactions init... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ProfileHost.html) |
| `midi__ci::PropertyExchangeResult` | Contains data returned by a responder in response to a request | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1PropertyExchangeResult.html) |
| `midi__ci::PropertyHost` | Acting as a ResponderListener, instances of this class can formulate appropriate replies to property transactions ini... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1PropertyHost.html) |
| `midi__ci::RequestID` | A strongly-typed identifier for a 7-bit request ID with a nullable state | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1RequestID.html) |
| `midi__ci::RequestKey` | A key used to uniquely identify ongoing transactions initiated by a ci::Device | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1RequestKey.html) |
| `midi__ci::ResponderDelegate` | An interface for types that implement responses for certain message types | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ResponderDelegate.html) |
| `midi__ci::ResponderOutput` | A buffer output that additionally provides information about an incoming message, so that an appropriate reply can be... | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ResponderOutput.html) |
| `midi__ci::ResponderPropertyExchangeCache` | Accumulates message chunks that form a request initiated by a remote device | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1ResponderPropertyExchangeCache.html) |
| `midi__ci::SubscriptionKey` | A key used to uniquely identify ongoing property subscriptions initiated by a ci::Device | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1SubscriptionKey.html) |
| `midi__ci::SubscriptionManager` | Manages subscriptions to properties on remote devices | [ref](https://docs.juce.com/master/classjuce_1_1midi__ci_1_1SubscriptionManager.html) |
| `universal__midi__packets::Block` | Represents a Function Block (FB) or Group Terminal Block (GTB) | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Block.html) |
| `universal__midi__packets::Endpoint` | Represents a single MIDI endpoint, which may have up to one input and up to one output | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Endpoint.html) |
| `universal__midi__packets::EndpointId` | Identifies a MIDI endpoint | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1EndpointId.html) |
| `universal__midi__packets::Endpoints` | Endpoints known to the system | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Endpoints.html) |
| `universal__midi__packets::Input` | An input (from the JUCE project's perspective) that receives messages sent by an endpoint | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Input.html) |
| `universal__midi__packets::LegacyVirtualInput` | Represents a virtual MIDI 1.0 input port | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1LegacyVirtualInput.html) |
| `universal__midi__packets::LegacyVirtualOutput` | Represents a virtual MIDI 1.0 output port | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1LegacyVirtualOutput.html) |
| `universal__midi__packets::Output` | An output (from the JUCE project's perspective) that sends messages to an endpoint | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Output.html) |
| `universal__midi__packets::Session` | Allows creating new connections to endpoints, and also creating new virtual endpoints | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1Session.html) |
| `universal__midi__packets::StaticDeviceInfo` | Static information about a particular MIDI device that can be queried without opening a connection to the device | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1StaticDeviceInfo.html) |
| `universal__midi__packets::VirtualEndpoint` | Represents a virtual device that allows this program to advertise itself to other MIDI-aware applications on the system | [ref](https://docs.juce.com/master/classjuce_1_1universal__midi__packets_1_1VirtualEndpoint.html) |
| `var` | A variant class, that can be used to hold a range of primitive values | [ref](https://docs.juce.com/master/classjuce_1_1var.html) |
