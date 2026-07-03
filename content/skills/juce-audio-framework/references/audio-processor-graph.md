# AudioProcessorGraph — Plugin Hosting & Routing

`AudioProcessorGraph` is an `AudioProcessor` that plays back a graph of other AudioProcessors. Use it to build plugin hosts, audio routers, or modular processing chains.

## Key Types

| Type | Purpose |
|------|---------|
| `NodeID` | Unique ID for each node in the graph |
| `Node` | Represents one processor in the graph |
| `Node::Ptr` | Reference-counted pointer to a Node |
| `Connection` | Links a channel of one node to a channel of another |
| `AudioGraphIOProcessor` | Special processor for graph audio/MIDI I/O |
| `UpdateKind` | `sync`, `async`, or `none` — controls graph rebuild behavior |

## Basic Host Setup

```cpp
#include <juce_audio_processors/juce_audio_processors.h>

class PluginHostProcessor : public juce::AudioProcessor
{
public:
    PluginHostProcessor()
        : AudioProcessor (BusesProperties()
            .withInput  ("Input",  juce::AudioChannelSet::stereo(), true)
            .withOutput ("Output", juce::AudioChannelSet::stereo(), true))
    {}

    void prepareToPlay (double sampleRate, int blockSize) override
    {
        graph.setPlayConfigDetails (getTotalNumInputChannels(),
                                    getTotalNumOutputChannels(),
                                    sampleRate, blockSize);
        graph.prepareToPlay (sampleRate, blockSize);

        // Add I/O nodes
        auto* inputNode  = graph.addNode (std::make_unique<juce::AudioGraphIOProcessor>
                              (juce::AudioGraphIOProcessor::audioInputNode));
        auto* outputNode = graph.addNode (std::make_unique<juce::AudioGraphIOProcessor>
                              (juce::AudioGraphIOProcessor::audioOutputNode));

        // Add a plugin node (loaded from file/descriptor)
        juce::AudioPluginFormatManager formatManager;
        formatManager.addDefaultFormats();

        juce::OwnedArray<juce::PluginDescription> descriptions;
        // ... scan/find plugin

        if (auto plugin = formatManager.createPluginInstance (*descriptions[0], sampleRate, blockSize, errorMsg))
        {
            auto* effectNode = graph.addNode (std::move (plugin));
            graph.addConnection ({ { inputNode->nodeID,  0 }, { effectNode->nodeID, 0 } });
            graph.addConnection ({ { inputNode->nodeID,  1 }, { effectNode->nodeID, 1 } });
            graph.addConnection ({ { effectNode->nodeID, 0 }, { outputNode->nodeID, 0 } });
            graph.addConnection ({ { effectNode->nodeID, 1 }, { outputNode->nodeID, 1 } });
        }
    }

    void processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midi) override
    {
        graph.processBlock (buffer, midi);
    }

    // ... other AudioProcessor overrides

private:
    juce::AudioProcessorGraph graph;
    juce::String errorMsg;
};
```

## Node Management

```cpp
// Add a node (returns Node::Ptr)
auto node = graph.addNode (std::make_unique<MyProcessor>(), std::nullopt, UpdateKind::sync);

// Remove a node
graph.removeNode (node->nodeID, UpdateKind::sync);
graph.removeNode (node.get(), UpdateKind::sync);

// Find a node
auto* found = graph.getNodeForId (nodeId);

// Get all nodes
auto& nodes = graph.getNodes();  // ReferenceCountedArray<Node>

// Clear everything
graph.clear (UpdateKind::sync);
```

## Connection Management

```cpp
// Connection: { source nodeID + channel, dest nodeID + channel }
juce::AudioProcessorGraph::Connection conn {
    { sourceNode->nodeID, 0 },   // source: channel 0
    { destNode->nodeID,   0 }    // dest: channel 0
};

// Add connection
bool success = graph.addConnection (conn, UpdateKind::sync);

// Remove connection
graph.removeConnection (conn, UpdateKind::sync);

// Query
bool canConnect = graph.canConnect (conn);
bool connected  = graph.isConnected (conn);
bool isInputTo  = graph.isAnInputTo (*sourceNode, *destNode);  // recursive

// Get all connections
auto connections = graph.getConnections();  // std::vector<Connection>

// Remove invalid connections (e.g., after removing a node)
graph.removeIllegalConnections (UpdateKind::sync);

// Disconnect all connections from a node
graph.disconnectNode (nodeId, UpdateKind::sync);
```

## AudioGraphIOProcessor Types

```cpp
// Graph inputs (microphone/external audio)
auto* inputNode = graph.addNode (
    std::make_unique<juce::AudioGraphIOProcessor> (
        juce::AudioGraphIOProcessor::audioInputNode));

// Graph outputs (speakers)
auto* outputNode = graph.addNode (
    std::make_unique<juce::AudioGraphIOProcessor> (
        juce::AudioGraphIOProcessor::audioOutputNode));

// MIDI input
auto* midiInNode = graph.addNode (
    std::make_unique<juce::AudioGraphIOProcessor> (
        juce::AudioGraphIOProcessor::midiInputNode));
```

## UpdateKind

| Value | Behavior |
|-------|----------|
| `sync` | Graph rebuilds immediately (call from message thread only) |
| `async` | Graph rebuilds on next processBlock call (safe from any thread) |
| `none` | No automatic rebuild; call `graph.rebuild()` manually |

## Key Node Properties

```cpp
node->nodeID;           // NodeID
node->getProcessor();   // AudioProcessor*
node->isBypassed();     // bool
node->setBypassed (true);
node->getTotalNumInputChannels();   // int
node->getTotalNumOutputChannels();  // int
```

## Plugin Loading with AudioPluginFormatManager

```cpp
juce::AudioPluginFormatManager formatManager;
formatManager.addDefaultFormats();  // VST3, AU, etc.

// Scan for plugins
juce::KnownPluginList pluginList;
juce::FileSearchPath searchPath;
searchPath.add (juce::File ("/path/to/plugins"));
juce::PluginDirectoryScanner scanner (pluginList,
    *formatManager.getFormat (0), searchPath, true, {}, false);

// Create instance
juce::String error;
auto description = pluginList.getTypes()[0];
auto plugin = formatManager.createPluginInstance (
    description, sampleRate, blockSize, error);
```

## References

- JUCE AudioProcessorGraph header: `modules/juce_audio_processors/processors/juce_AudioProcessorGraph.h`
- AudioPluginHost example: `JUCE/extras/AudioPluginHost/`
