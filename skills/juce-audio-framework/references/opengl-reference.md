# JUCE OpenGL — Complete Reference

## OpenGLContext — The Entry Point

Attach to any Component to enable hardware-accelerated rendering:

```cpp
class MyGLComponent : public juce::Component,
                      public juce::OpenGLRenderer
{
public:
    MyGLComponent()
    {
        openGLContext.setRenderer (this);
        openGLContext.attachTo (*this);
        openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);
    }

    ~MyGLComponent() override { openGLContext.detach(); }

    void newOpenGLContextCreated() override
    {
        shaderProgram = std::make_unique<juce::OpenGLShaderProgram> (openGLContext);
        // compile shaders, create VAO/VBO
    }

    void renderOpenGL() override
    {
        jassert (juce::OpenGLHelpers::isContextActive());
        auto scale = (float) openGLContext.getRenderingScale();
        glViewport (0, 0, juce::roundToInt (getWidth() * scale),
                          juce::roundToInt (getHeight() * scale));
        glClearColor (0.1f, 0.1f, 0.1f, 1.0f);
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        shaderProgram->use();
    }

    void openGLContextClosing() override { shaderProgram.reset(); }

private:
    juce::OpenGLContext openGLContext;
    std::unique_ptr<juce::OpenGLShaderProgram> shaderProgram;
};
```

## OpenGLShaderProgram

```cpp
auto shader = std::make_unique<juce::OpenGLShaderProgram> (openGLContext);

juce::String vertexShader = R"(
    attribute vec2 position;
    attribute vec2 texCoord;
    varying vec2 vTexCoord;
    uniform mat4 projectionMatrix;
    void main()
    {
        vTexCoord = texCoord;
        gl_Position = projectionMatrix * vec4 (position, 0.0, 1.0);
    }
)";

juce::String fragmentShader = R"(
    uniform sampler2D texture0;
    uniform float opacity;
    varying vec2 vTexCoord;
    void main()
    {
        gl_FragColor = texture2D (texture0, vTexCoord) * opacity;
    }
)";

shader->addVertexShader (juce::OpenGLHelpers::translateVertexShaderToV3 (vertexShader));
shader->addFragmentShader (juce::OpenGLHelpers::translateFragmentShaderToV3 (fragmentShader));

juce::OpenGLShaderProgram::Attribute position (*shader, "position");
juce::OpenGLShaderProgram::Attribute texCoord (*shader, "texCoord");
juce::OpenGLShaderProgram::Uniform projectionMatrix (*shader, "projectionMatrix");
juce::OpenGLShaderProgram::Uniform textureUniform (*shader, "texture0");

shader->link();
shader->use();
```

## OpenGLFrameBuffer

Off-screen rendering:

```cpp
juce::OpenGLFrameBuffer fbo;
fbo.initialise (openGLContext, 512, 512);

fbo.makeCurrentRenderingTarget();
// render to FBO
openGLContext.makeActive();
fbo.drawAt (0.0f, 0.0f);
```

## OpenGLTexture

```cpp
juce::OpenGLTexture texture;
juce::Image img = juce::ImageCache::getFromFile (juce::File ("texture.png"));
texture.loadImage (img);

glActiveTexture (GL_TEXTURE0);
texture.bind();
glUniform1i (textureUniform.uniformID, 0);
```

## OpenGLAppComponent

For standalone GL applications:

```cpp
class MyApp : public juce::OpenGLAppComponent
{
public:
    void initialise() override { /* create GL resources */ }
    void shutdown() override { /* release GL resources */ }
    void render() override { /* GL draw calls */ }
};
```

## Using OpenGL as JUCE Graphics Backend

```cpp
class MyEditor : public juce::AudioProcessorEditor
{
public:
    MyEditor (MyProcessor& p) : AudioProcessorEditor (&p)
    {
        openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);
        openGLContext.attachTo (*this);
    }
    ~MyEditor() override { openGLContext.detach(); }
private:
    juce::OpenGLContext openGLContext;
};
```

## 3D Geometry Helpers

```cpp
juce::Vector3D<float> v (1.0f, 2.0f, 3.0f);
juce::Matrix3D<float> projection = juce::Matrix3D<float>::fromFrustum (l, r, b, t, n, f);
juce::Matrix3D<float> rotation = juce::Matrix3D<float>::rotation ({ angleX, angleY, angleZ });
juce::Quaternion<float> q (axis, angle);
juce::Draggable3DOrientation dragOrientation;
```

## OpenGL Versions and Profiles

| Version | Year | Notes |
|---------|------|-------|
| 2.1 | 2006 | Last with fixed-function pipeline |
| 3.0 | 2008 | Deprecation model, VAOs, FBOs core |
| 3.2 | 2009 | **JUCE default** — Core Profile, geometry shaders |
| 3.3 | 2010 | Compute shaders, sampler objects |
| 4.0-4.6 | 2010-2017 | Tessellation, indirect drawing, SPIR-V |

**Core Profile** (JUCE 8 default): Removes deprecated fixed-function pipeline. Forces modern practices.
**Compatibility Profile**: Retains legacy functions. Not recommended.

```cpp
openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL3_2);
openGLContext.setOpenGLVersionRequired (juce::OpenGLContext::OpenGLVersion::openGL4_1);
```

**Platform notes:**
- macOS: Only Core Profile. Max 4.1. Deprecated in 10.14 but still works.
- Windows: Both Core and Compatibility. Version depends on GPU driver.
- Linux: Mesa/NVIDIA. Up to 4.6 on modern hardware.

## Modern OpenGL Pipeline

1. **Vertex Specification**: VBOs with positions, colors, texcoords
2. **Vertex Shader**: Model → View → Projection transform
3. **Primitive Assembly**: Connect vertices into triangles
4. **Rasterization**: Primitives to fragments
5. **Fragment Shader**: Compute color per fragment
6. **Output Merging**: Depth test, blending, framebuffer write

### VAO (Required in Core Profile)

```cpp
GLuint vao;
glGenVertexArrays (1, &vao);
glBindVertexArray (vao);

GLuint vbo;
glGenBuffers (1, &vbo);
glBindBuffer (GL_ARRAY_BUFFER, vbo);
glBufferData (GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

glEnableVertexAttribArray (0);
glVertexAttribPointer (0, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (void*) 0);

glBindVertexArray (0);

// In render:
glBindVertexArray (vao);
glDrawArrays (GL_TRIANGLES, 0, 3);
glBindVertexArray (0);

// Cleanup:
glDeleteVertexArrays (1, &vao);
glDeleteBuffers (1, &vbo);
```

### EBO (Indexed Drawing)

```cpp
GLuint ebo;
glGenBuffers (1, &ebo);
glBindBuffer (GL_ELEMENT_ARRAY_BUFFER, ebo);
glBufferData (GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
glDrawElements (GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```

## Performance Best Practices

**Do:**
- Batch draw calls, minimize state changes
- Use VAOs (required in Core Profile)
- Use VBOs with `GL_STATIC_DRAW` / `GL_DYNAMIC_DRAW`
- Use UBOs for shared uniforms
- Use instancing for many similar objects
- Profile with RenderDoc, Nsight, AMD GPU PerfStudio

**Don't:**
- Never use `glBegin/glEnd` (deprecated)
- Never create/destroy GL objects in render loop
- Never `glReadPixels` (stalls pipeline)
- Never use fixed-function pipeline

## Platform-Specific

**macOS:** Only Core Profile. Max 4.1. Use `getRenderingScale()` for Retina.
**Windows:** WGL context. Multi-GPU uses default. Version from driver.
**Linux:** GLX or EGL. Mesa 4.5-4.6, NVIDIA 4.6. Wayland via XWayland.

## Debugging

```cpp
glEnable (GL_DEBUG_OUTPUT);
glEnable (GL_DEBUG_OUTPUT_SYNCHRONOUS);
glDebugMessageCallback ([](GLenum source, GLenum type, GLuint id, GLenum severity,
                            GLsizei length, const GLchar* message, const void* userParam) {
    if (severity == GL_DEBUG_SEVERITY_HIGH)
        juce::Logger::writeToLog ("GL ERROR: " + juce::String (message));
}, nullptr);
```

**Tools:** RenderDoc, NVIDIA Nsight, AMD Radeon GPU Profiler, apitrace, glslangValidator

## References

- OpenGL Registry: https://www.khronos.org/registry/OpenGL/
- OpenGL 4.6 Reference: https://docs.gl/gl4/
- Learn OpenGL: https://learnopengl.com/
- JUCE OpenGL examples: `JUCE/examples/GUI/OpenGLAppDemo`
