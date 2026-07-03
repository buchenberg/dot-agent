# OpenGL 4.x API Quick Reference

## Buffer Object Targets
| Target | Description |
|--------|-------------|
| `GL_ARRAY_BUFFER` | Vertex attributes |
| `GL_ELEMENT_ARRAY_BUFFER` | Vertex array indices |
| `GL_UNIFORM_BUFFER` | Uniform block storage |
| `GL_SHADER_STORAGE_BUFFER` | Read-write shader storage (GL 4.3+) |
| `GL_PIXEL_UNPACK_BUFFER` | Pixel data source (unpack) |
| `GL_PIXEL_PACK_BUFFER` | Pixel data destination (pack) |
| `GL_TEXTURE_BUFFER` | Texture data source |
| `GL_COPY_READ_BUFFER` | Buffer copy source |
| `GL_COPY_WRITE_BUFFER` | Buffer copy destination |
| `GL_DRAW_INDIRECT_BUFFER` | Indirect draw commands |
| `GL_DISPATCH_INDIRECT_BUFFER` | Indirect compute dispatch (GL 4.3+) |
| `GL_QUERY_BUFFER` | Query result buffer (GL 4.4+) |
| `GL_ATOMIC_COUNTER_BUFFER` | Atomic counter storage (GL 4.2+) |

## Buffer Usage Hints
| Frequency | Nature | Constant |
|-----------|--------|----------|
| Stream (modified once, used few times) | Draw | `GL_STREAM_DRAW` |
| Stream | Read | `GL_STREAM_READ` |
| Stream | Copy | `GL_STREAM_COPY` |
| Static (modified once, used many times) | Draw | `GL_STATIC_DRAW` |
| Static | Read | `GL_STATIC_READ` |
| Static | Copy | `GL_STATIC_COPY` |
| Dynamic (modified repeatedly) | Draw | `GL_DYNAMIC_DRAW` |
| Dynamic | Read | `GL_DYNAMIC_READ` |
| Dynamic | Copy | `GL_DYNAMIC_COPY` |

## Texture Targets
| Target | Description |
|--------|-------------|
| `GL_TEXTURE_1D` | 1D texture |
| `GL_TEXTURE_2D` | 2D texture |
| `GL_TEXTURE_3D` | 3D texture |
| `GL_TEXTURE_1D_ARRAY` | 1D texture array |
| `GL_TEXTURE_2D_ARRAY` | 2D texture array |
| `GL_TEXTURE_RECTANGLE` | Rectangle texture (no mipmaps) |
| `GL_TEXTURE_CUBE_MAP` | Cube map texture |
| `GL_TEXTURE_CUBE_MAP_POSITIVE_X` | +X face |
| `GL_TEXTURE_CUBE_MAP_NEGATIVE_X` | -X face |
| `GL_TEXTURE_CUBE_MAP_POSITIVE_Y` | +Y face |
| `GL_TEXTURE_CUBE_MAP_NEGATIVE_Y` | -Y face |
| `GL_TEXTURE_CUBE_MAP_POSITIVE_Z` | +Z face |
| `GL_TEXTURE_CUBE_MAP_NEGATIVE_Z` | -Z face |
| `GL_TEXTURE_BUFFER` | Buffer texture |
| `GL_TEXTURE_2D_MULTISAMPLE` | Multisampled 2D texture |
| `GL_TEXTURE_2D_MULTISAMPLE_ARRAY` | Multisampled 2D array |

## Texture Format Types
| Format | Description |
|--------|-------------|
| `GL_RED`, `GL_RG`, `GL_RGB`, `GL_RGBA` | Base formats |
| `GL_BGR`, `GL_BGRA` | BGR variants |
| `GL_RED_INTEGER`, `GL_RG_INTEGER`, `GL_RGB_INTEGER`, `GL_RGBA_INTEGER` | Integer formats |
| `GL_DEPTH_COMPONENT` | Depth texture |
| `GL_DEPTH_STENCIL` | Depth/stencil combined |
| `GL_STENCIL_INDEX` | Stencil texture (GL 4.4+) |

## Common Sized Internal Formats
| Format | Bits |
|--------|------|
| `GL_R8`, `GL_RG8`, `GL_RGB8`, `GL_RGBA8` | 8-bit unsigned normalized |
| `GL_R16`, `GL_RG16`, `GL_RGB16`, `GL_RGBA16` | 16-bit unsigned normalized |
| `GL_R8I`, `GL_RG8I`, `GL_RGB8I`, `GL_RGBA8I` | 8-bit signed integer |
| `GL_R8UI`, `GL_RG8UI`, `GL_RGB8UI`, `GL_RGBA8UI` | 8-bit unsigned integer |
| `GL_R16F`, `GL_RG16F`, `GL_RGB16F`, `GL_RGBA16F` | 16-bit float |
| `GL_R32F`, `GL_RG32F`, `GL_RGB32F`, `GL_RGBA32F` | 32-bit float |
| `GL_DEPTH_COMPONENT16`, `GL_DEPTH_COMPONENT24`, `GL_DEPTH_COMPONENT32F` | Depth formats |
| `GL_DEPTH24_STENCIL8`, `GL_DEPTH32F_STENCIL8` | Depth/stencil combined |
| `GL_SRGB8`, `GL_SRGB8_ALPHA8` | sRGB formats |
| `GL_COMPRESSED_RGB_S3TC_DXT1_EXT` | DXT1 compression |
| `GL_COMPRESSED_RGBA_S3TC_DXT5_EXT` | DXT5 compression |

## Primitive Types
| Constant | Description |
|----------|-------------|
| `GL_POINTS` | Individual points |
| `GL_LINE_STRIP` | Connected line segments |
| `GL_LINE_LOOP` | Closed loop of lines |
| `GL_LINES` | Pairs of vertices as lines |
| `GL_TRIANGLE_STRIP` | Connected triangles |
| `GL_TRIANGLE_FAN` | Fan of triangles |
| `GL_TRIANGLES` | Triples of vertices as triangles |
| `GL_LINES_ADJACENCY` | Lines with adjacency (GS) |
| `GL_LINE_STRIP_ADJACENCY` | Line strip with adjacency (GS) |
| `GL_TRIANGLES_ADJACENCY` | Triangles with adjacency (GS) |
| `GL_TRIANGLE_STRIP_ADJACENCY` | Triangle strip with adjacency (GS) |
| `GL_PATCHES` | Patches for tessellation |

## Blend Factors
| Factor | Description |
|--------|-------------|
| `GL_ZERO`, `GL_ONE` | 0, 1 |
| `GL_SRC_COLOR`, `GL_ONE_MINUS_SRC_COLOR` | Source RGB, 1-srcRGB |
| `GL_DST_COLOR`, `GL_ONE_MINUS_DST_COLOR` | Dest RGB, 1-dstRGB |
| `GL_SRC_ALPHA`, `GL_ONE_MINUS_SRC_ALPHA` | Source alpha, 1-srcA |
| `GL_DST_ALPHA`, `GL_ONE_MINUS_DST_ALPHA` | Dest alpha, 1-dstA |
| `GL_CONSTANT_COLOR`, `GL_ONE_MINUS_CONSTANT_COLOR` | Constant color |
| `GL_CONSTANT_ALPHA`, `GL_ONE_MINUS_CONSTANT_ALPHA` | Constant alpha |
| `GL_SRC_ALPHA_SATURATE` | min(srcA, 1-dstA) |

## Depth Functions
| Function | Description |
|----------|-------------|
| `GL_NEVER` | Always fail |
| `GL_LESS` | Pass if incoming < stored |
| `GL_EQUAL` | Pass if incoming == stored |
| `GL_LEQUAL` | Pass if incoming <= stored |
| `GL_GREATER` | Pass if incoming > stored |
| `GL_NOTEQUAL` | Pass if incoming != stored |
| `GL_GEQUAL` | Pass if incoming >= stored |
| `GL_ALWAYS` | Always pass |

## Stencil Operations
| Operation | Description |
|-----------|-------------|
| `GL_KEEP` | Keep current value |
| `GL_ZERO` | Set to 0 |
| `GL_REPLACE` | Replace with reference value |
| `GL_INCR` | Increment (saturate at max) |
| `GL_INCR_WRAP` | Increment (wrap around) |
| `GL_DECR` | Decrement (saturate at 0) |
| `GL_DECR_WRAP` | Decrement (wrap around) |
| `GL_INVERT` | Bitwise invert |

## Framebuffer Status
| Status | Description |
|--------|-------------|
| `GL_FRAMEBUFFER_COMPLETE` | Framebuffer is complete |
| `GL_FRAMEBUFFER_UNDEFINED` | Default framebuffer is undefined |
| `GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT` | Attachment is incomplete |
| `GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT` | No attachments |
| `GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER` | Draw buffer incomplete |
| `GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER` | Read buffer incomplete |
| `GL_FRAMEBUFFER_UNSUPPORTED` | Unsupported format combination |
| `GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE` | Multisample mismatch |
| `GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS` | Layer target mismatch |
