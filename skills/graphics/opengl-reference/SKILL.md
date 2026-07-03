---
name: graphics/opengl-reference
description: >
  Comprehensive OpenGL 4.x API and GLSL reference skill backed by the Khronos
  OpenGL-Refpages repository. Covers the full OpenGL 4.x pipeline (currently 4.6),
  including core API functions, shader stages, buffer objects, textures, framebuffers,
  and GLSL built-in functions. Use this skill when answering OpenGL programming
  questions, debugging GL code, or explaining how specific functions, parameters,
  or pipeline stages work.
triggers:
  - OpenGL API questions (e.g., "how does glBufferData work?")
  - GLSL built-in functions and shader language questions
  - OpenGL pipeline setup, VAO/VBO, shaders, textures, framebuffers
  - Debugging GL errors, state management, or rendering issues
  - OpenGL version differences and feature availability
  - Buffer objects, vertex arrays, uniforms, and shader compilation/linking
---

# OpenGL Reference Skill

## Overview

This skill provides authoritative reference information for OpenGL 4.x (currently 4.6) and GLSL, sourced from the official Khronos OpenGL Reference Pages.

**Repository structure:**
- `gl4/` — OpenGL 4.x reference pages (latest, ~521 entries)
- `gl2.1/` — OpenGL 2.1 reference pages (legacy fixed-function)
- `es3/` / `es3.1/` / `es3.0/` / `es2.0/` / `es1.1/` — OpenGL ES reference pages

## OpenGL API Function Categories

### 1. Context & State Management
- **glEnable / glDisable** — Enable/disable server-side GL capabilities (blend, depth test, cull face, stencil test, scissor test, etc.)
- **glGetError** — Return error information (GL_NO_ERROR, GL_INVALID_ENUM, GL_INVALID_VALUE, GL_INVALID_OPERATION, GL_INVALID_FRAMEBUFFER_OPERATION, GL_OUT_OF_MEMORY)
- **glClear** — Clear buffers to preset values (GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_STENCIL_BUFFER_BIT)
- **glClearColor, glClearDepth, glClearStencil** — Set clear values
- **glViewport** — Set the viewport (x, y, width, height)
- **glDepthRange** — Specify mapping of depth values from NDC to window coordinates

### 2. Buffer Objects (VBOs)
- **glGenBuffers** — Generate buffer object names
- **glBindBuffer** — Bind a named buffer object to a target (GL_ARRAY_BUFFER, GL_ELEMENT_ARRAY_BUFFER, etc.)
- **glBufferData** — Create and initialize a buffer object's data store (usage: STREAM/STATIC/DYNAMIC × DRAW/READ/COPY)
- **glBufferSubData** — Update a subset of a buffer object's data store
- **glDeleteBuffers** — Delete named buffer objects
- **glMapBuffer / glUnmapBuffer** — Map/unmap a buffer object's data store

### 3. Vertex Array Objects (VAOs)
- **glGenVertexArrays** — Generate vertex array object names
- **glBindVertexArray** — Bind a vertex array object
- **glEnableVertexAttribArray / glDisableVertexAttribArray** — Enable/disable generic vertex attribute array
- **glVertexAttribPointer** — Define an array of generic vertex attribute data (index, size, type, normalized, stride, pointer)
- **glVertexAttribIPointer** — Integer variant (no normalization)
- **glVertexAttribLPointer** — Double-precision variant
- **glDeleteVertexArrays** — Delete vertex array objects

### 4. Shader Compilation & Program Linking
- **glCreateShader** — Create a shader object (GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_GEOMETRY_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_COMPUTE_SHADER)
- **glShaderSource** — Replace the source code in a shader object
- **glCompileShader** — Compile a shader object; check GL_COMPILE_STATUS
- **glCreateProgram** — Create a program object
- **glAttachShader** — Attach a shader object to a program object
- **glLinkProgram** — Link a program object; check GL_LINK_STATUS
- **glUseProgram** — Install a program object as part of current rendering state
- **glDeleteShader / glDeleteProgram** — Delete shader/program objects
- **glGetShaderInfoLog / glGetProgramInfoLog** — Retrieve compilation/linking info logs

### 5. Uniforms
- **glGetUniformLocation** — Get the location of a uniform variable
- **glUniform1f/2f/3f/4f, glUniform1i/2i/3i/4i, glUniform1ui/2ui/3ui/4ui** — Set scalar uniform values
- **glUniform1fv/2fv/3fv/4fv, glUniform1iv/2iv/3iv/4iv, glUniform1uiv/...** — Set vector uniform values
- **glUniformMatrix2fv/3fv/4fv, glUniformMatrix2x3fv/3x2fv/2x4fv/4x2fv/3x4fv/4x3fv** — Set matrix uniform values (column-major by default)

### 6. Textures
- **glGenTextures** — Generate texture names
- **glBindTexture** — Bind a named texture to a target
- **glTexImage2D** — Specify a 2D texture image (target, level, internalformat, width, height, border, format, type, data)
- **glTexImage3D** — Specify a 3D texture image
- **glTexSubImage2D / glTexSubImage3D** — Specify a texture subimage
- **glTexParameter** — Set texture parameters (wrap, filter, etc.)
- **glActiveTexture** — Select active texture unit
- **glGenerateMipmap** — Generate mipmaps for a specified texture target
- **glDeleteTextures** — Delete named textures

### 7. Framebuffers
- **glGenFramebuffers** — Generate framebuffer object names
- **glBindFramebuffer** — Bind a framebuffer to a target (GL_FRAMEBUFFER, GL_DRAW_FRAMEBUFFER, GL_READ_FRAMEBUFFER)
- **glFramebufferTexture2D** — Attach a texture image to a framebuffer
- **glFramebufferRenderbuffer** — Attach a renderbuffer object to a framebuffer
- **glCheckFramebufferStatus** — Check framebuffer completeness
- **glDeleteFramebuffers** — Delete framebuffer objects

### 8. Drawing Commands
- **glDrawArrays** — Render primitives from array data (mode, first, count)
- **glDrawElements** — Render primitives from indexed array data (mode, count, type, indices)
- **glDrawArraysInstanced** — Render multiple instances of primitives from array data
- **glDrawElementsInstanced** — Render multiple instances of primitives from indexed data
- **glMultiDrawArrays / glMultiDrawElements** — Render multiple sets of primitives

### 9. GLSL Built-in Functions (Shader Stage)
- **Trigonometric**: sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh
- **Exponential**: pow, exp, exp2, log, log2, sqrt, inversesqrt
- **Common**: abs, sign, floor, trunc, round, roundEven, ceil, fract, mod, min, max, clamp, mix, step, smoothstep
- **Geometric**: length, distance, dot, cross, normalize, faceforward, reflect, refract
- **Matrix**: matrixCompMult, outerProduct, transpose, determinant, inverse
- **Vector Relational**: lessThan, lessThanEqual, greaterThan, greaterThanEqual, equal, notEqual, any, all, not
- **Integer**: bitCount, findLSB, findMSB, bitfieldExtract, bitfieldInsert, bitfieldReverse, uaddCarry, usubBorrow, umulExtended, imulExtended
- **Atomic**: atomicAdd, atomicAnd, atomicOr, atomicXor, atomicMin, atomicMax, atomicExchange, atomicCompSwap, atomicCounterIncrement, atomicCounterDecrement

### 10. Common OpenGL Constants
- **Primitive types**: GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_PATCHES
- **Buffer targets**: GL_ARRAY_BUFFER, GL_ELEMENT_ARRAY_BUFFER, GL_UNIFORM_BUFFER, GL_SHADER_STORAGE_BUFFER, GL_PIXEL_UNPACK_BUFFER
- **Texture targets**: GL_TEXTURE_2D, GL_TEXTURE_3D, GL_TEXTURE_CUBE_MAP, GL_TEXTURE_1D_ARRAY, GL_TEXTURE_2D_ARRAY, GL_TEXTURE_RECTANGLE
- **Framebuffer targets**: GL_FRAMEBUFFER, GL_DRAW_FRAMEBUFFER, GL_READ_FRAMEBUFFER
- **Shader types**: GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_GEOMETRY_SHADER, GL_TESS_CONTROL_SHADER, GL_TESS_EVALUATION_SHADER, GL_COMPUTE_SHADER
- **Draw modes (geometry shader adjacency)**: GL_LINE_STRIP_ADJACENCY, GL_LINES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY, GL_TRIANGLES_ADJACENCY

## Typical OpenGL 4.x Render Loop

```c
// 1. Create and bind VAO
glGenVertexArrays(1, &vao);
glBindVertexArray(vao);

// 2. Create and fill VBO
glGenBuffers(1, &vbo);
glBindBuffer(GL_ARRAY_BUFFER, vbo);
glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW);

// 3. Configure vertex attributes
glEnableVertexAttribArray(0);
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);

// 4. Create shader program
GLuint vs = glCreateShader(GL_VERTEX_SHADER);
glShaderSource(vs, 1, &vsSource, NULL);
glCompileShader(vs);

GLuint fs = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fs, 1, &fsSource, NULL);
glCompileShader(fs);

GLuint program = glCreateProgram();
glAttachShader(program, vs);
glAttachShader(program, fs);
glLinkProgram(program);
glUseProgram(program);

// 5. Set uniforms
GLint loc = glGetUniformLocation(program, "uModelViewProj");
glUniformMatrix4fv(loc, 1, GL_FALSE, matrix);

// 6. Render loop
glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
glDrawArrays(GL_TRIANGLES, 0, vertexCount);
```

## Key Pitfalls & Notes

1. **VAO binding is sticky**: Vertex attribute state is captured in the currently bound VAO. Always bind the VAO before configuring attributes.
2. **Shader compilation vs linking**: Compile individual shaders first, then link the program. Check `GL_COMPILE_STATUS` and `GL_LINK_STATUS` separately.
3. **Buffer object 0 is reserved**: Binding buffer 0 unbinds the current buffer. Operations on buffer 0 generate `GL_INVALID_OPERATION`.
4. **glGetError should be called in a loop**: There may be multiple error flags; loop until `GL_NO_ERROR` is returned.
5. **Uniform location -1 is valid for glUniform**: If a uniform is not used in the shader, its location may be -1. `glUniform*` with location -1 silently ignores the call.
6. **Texture internalformat matters**: Use sized internal formats (e.g., `GL_RGBA8`) for predictable behavior. Generic formats (e.g., `GL_RGBA`) let the driver choose.
7. **Framebuffer completeness**: Always check `glCheckFramebufferStatus` before using a framebuffer. Common issues: missing attachment, mismatched sizes, incomplete mipmap.
8. **glTexImage2D border must be 0**: The border parameter is deprecated and must be 0.

## Version Availability

- OpenGL 4.6 is the latest version covered by `gl4/`
- Functions are annotated with version support tables in the XML source
- Some features require specific versions:
  - Geometry shaders: 3.2+
  - Tessellation shaders: 4.0+
  - Compute shaders: 4.3+
  - Shader storage buffers: 4.3+
  - Atomic counters: 4.2+
  - Separate shader objects / program pipelines: 4.1+

## Error Handling Reference

| Error Code | Meaning |
|------------|---------|
| GL_NO_ERROR | No error (value = 0) |
| GL_INVALID_ENUM | Unacceptable value for enumerated argument |
| GL_INVALID_VALUE | Numeric argument out of range |
| GL_INVALID_OPERATION | Operation not allowed in current state |
| GL_INVALID_FRAMEBUFFER_OPERATION | Framebuffer object is not complete |
| GL_OUT_OF_MEMORY | Not enough memory to execute command |
| GL_STACK_UNDERFLOW | Internal stack underflow (deprecated) |
| GL_STACK_OVERFLOW | Internal stack overflow (deprecated) |
