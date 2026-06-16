# OpenGL Debugging & Troubleshooting Guide

## Common Error Patterns

### GL_INVALID_ENUM
**Cause**: Passed an invalid enum value to a function.

**Common scenarios**:
- Using a texture format constant with a buffer function
- Passing an unsupported primitive type to `glDrawArrays`
- Using a shader type constant where a buffer target is expected

**Fix**: Double-check the parameter type against the function signature.

---

### GL_INVALID_VALUE
**Cause**: A numeric parameter is out of range.

**Common scenarios**:
- Negative buffer size passed to `glBufferData`
- `count` < 0 in `glDrawArrays`
- `level` < 0 or too large in `glTexImage2D`
- `stride` < 0 in `glVertexAttribPointer`
- `width` or `height` < 0 in `glViewport`

**Fix**: Validate numeric parameters before calling GL functions.

---

### GL_INVALID_OPERATION
**Cause**: The operation is not allowed in the current state.

**Common scenarios**:
- Calling `glUniform` without an active program (`glUseProgram`)
- Calling `glBufferData` on buffer 0 (no buffer bound)
- Calling `glDrawArrays` with a mapped buffer bound to an enabled array
- Calling `glTexImage2D` with `GL_TEXTURE_RECTANGLE` and `level != 0`
- Calling `glUseProgram` during transform feedback
- Calling `glLinkProgram` when a shader hasn't been compiled
- Calling `glVertexAttribPointer` with `pointer != NULL` and no VBO bound to `GL_ARRAY_BUFFER`

**Fix**: Check GL state before operations. Use `glGetError` to identify the failing call.

---

### GL_INVALID_FRAMEBUFFER_OPERATION
**Cause**: The framebuffer is incomplete.

**Common scenarios**:
- Missing attachment (no color/depth/stencil buffer attached)
- Mismatched attachment sizes
- Incomplete mipmaps on a mipmapped texture attachment
- Using a texture format that isn't color-renderable

**Fix**: Always check `glCheckFramebufferStatus` after setup:
```c
GLenum status = glCheckFramebufferStatus(GL_FRAMEBUFFER);
if (status != GL_FRAMEBUFFER_COMPLETE) {
    // Handle error
}
```

---

### GL_OUT_OF_MEMORY
**Cause**: GPU ran out of memory.

**Common scenarios**:
- Allocating very large textures or buffers
- Memory leak from not deleting textures/buffers/shaders
- Too many FBOs with large attachments

**Fix**: Profile memory usage, delete unused objects, use texture compression.

---

## Shader Compilation Debugging

### Check Compile Status
```c
GLint success;
glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
if (!success) {
    GLchar infoLog[512];
    glGetShaderInfoLog(shader, 512, NULL, infoLog);
    std::cerr << "Shader compilation failed:\n" << infoLog << std::endl;
}
```

### Check Link Status
```c
GLint success;
glGetProgramiv(program, GL_LINK_STATUS, &success);
if (!success) {
    GLchar infoLog[512];
    glGetProgramInfoLog(program, 512, NULL, infoLog);
    std::cerr << "Program linking failed:\n" << infoLog << std::endl;
}
```

### Common Shader Errors
| Error | Cause |
|-------|-------|
| `version` not first | `#version` must be the first line (after comments) |
| Missing `main()` | Every shader stage needs a `main()` function |
| Type mismatch in assignment | Assigning `vec3` to `vec4`, etc. |
| Undefined variable | Typo or missing declaration |
| `gl_Position` not written | Vertex shader must write `gl_Position` |
| Precision mismatch | `highp`/`mediump`/`lowp` conflicts |
| Out-of-bounds array access | Accessing array index beyond declared size |

---

## Performance Tips

### Buffer Usage Hints
- **Static geometry**: `GL_STATIC_DRAW` — upload once, draw many times
- **Dynamic geometry**: `GL_DYNAMIC_DRAW` — update frequently, draw frequently
- **Streaming data**: `GL_STREAM_DRAW` — upload once per frame, draw once
- **Readback**: `GL_*_READ` for GPU→CPU transfer (avoid if possible)

### Texture Optimization
- Use `GL_TEXTURE_2D_ARRAY` instead of texture atlases for sprite sheets
- Generate mipmaps with `glGenerateMipmap` for minification quality
- Use compressed texture formats (DXT/BC, ASTC) to reduce memory bandwidth
- Batch draw calls with the same texture to minimize state changes

### Draw Call Batching
- Combine multiple objects into a single VBO when possible
- Use `glMultiDrawArrays` or `glMultiDrawElements` for multiple similar draws
- Use instanced rendering (`glDrawArraysInstanced`) for repeated geometry
- Use `GL_ELEMENT_ARRAY_BUFFER` with indexed geometry to reduce vertex duplication

### State Change Minimization
- Sort draws by shader program, then by texture, then by VAO
- Avoid redundant `glUseProgram`, `glBindTexture`, and `glBindVertexArray` calls
- Use uniform buffer objects (UBOs) to update many uniforms in a single call
- Use `glProgramUniform` (direct state access) to avoid `glUseProgram` switching

---

## Common Pitfalls

1. **Forgetting to bind VAO before drawing**: The VAO stores all vertex attribute state. Always bind it.
2. **Not unmapping buffers**: `glMapBuffer` must be paired with `glUnmapBuffer`.
3. **Texture coordinates flipped**: OpenGL's origin is bottom-left for textures; many image loaders give top-left origin.
4. **Depth buffer not cleared**: Always clear depth with `glClear(GL_DEPTH_BUFFER_BIT)` when using depth testing.
5. **Blending without alpha channel**: Ensure the framebuffer has an alpha channel if using `GL_SRC_ALPHA` blending.
6. **Mipmapping without generating mipmaps**: Set `GL_TEXTURE_MIN_FILTER` to `GL_LINEAR` or call `glGenerateMipmap`.
7. **Integer uniforms with `glUniform1f`**: Use `glUniform1i` for sampler uniforms, not `glUniform1f`.
8. **Forgetting `glEnable(GL_DEPTH_TEST)`**: Depth testing is disabled by default.
9. **VAO 0 behavior**: In core profile, VAO 0 is not a valid VAO. Always create and bind your own VAO.
10. **Shader attribute location mismatch**: Ensure `layout(location = N)` in shader matches the index in `glVertexAttribPointer`.
