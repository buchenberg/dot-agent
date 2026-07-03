# GLSL Built-in Functions Quick Reference

## Trigonometric
| Function | Description |
|----------|-------------|
| `radians(degrees)` | Convert degrees to radians |
| `degrees(radians)` | Convert radians to degrees |
| `sin(x)`, `cos(x)`, `tan(x)` | Standard trig functions |
| `asin(x)`, `acos(x)`, `atan(y,x)`, `atan(y/x)` | Inverse trig functions |
| `sinh(x)`, `cosh(x)`, `tanh(x)` | Hyperbolic trig |
| `asinh(x)`, `acosh(x)`, `atanh(x)` | Inverse hyperbolic |

## Exponential
| Function | Description |
|----------|-------------|
| `pow(x,y)` | x raised to the power y |
| `exp(x)`, `exp2(x)` | e^x, 2^x |
| `log(x)`, `log2(x)` | Natural log, base-2 log |
| `sqrt(x)`, `inversesqrt(x)` | Square root, 1/sqrt(x) |

## Common
| Function | Description |
|----------|-------------|
| `abs(x)`, `sign(x)` | Absolute value, sign (-1, 0, 1) |
| `floor(x)`, `trunc(x)`, `round(x)`, `roundEven(x)`, `ceil(x)` | Rounding |
| `fract(x)` | Fractional part |
| `mod(x,y)`, `modf(x, out i)` | Modulo, split into int/fraction |
| `min(x,y)`, `max(x,y)`, `clamp(x, min, max)` | Min/max/clamp |
| `mix(x,y,a)`, `step(edge,x)`, `smoothstep(edge0,edge1,x)` | Interpolation |
| `isnan(x)`, `isinf(x)` | Check for NaN/Inf |
| `fma(a,b,c)` | Fused multiply-add: a*b+c |
| `frexp(x, out exp)`, `ldexp(x, exp)` | Extract/significand, x*2^exp |

## Geometric (Vector)
| Function | Description |
|----------|-------------|
| `length(v)`, `distance(p0,p1)` | Vector length, distance between points |
| `dot(a,b)`, `cross(a,b)` | Dot product, cross product |
| `normalize(v)` | Normalize vector |
| `faceforward(N,I,Nref)` | Flip N if dot(I,Nref)<0 |
| `reflect(I,N)` | Reflection vector |
| `refract(I,N,eta)` | Refraction vector (Snell's law) |

## Matrix
| Function | Description |
|----------|-------------|
| `matrixCompMult(x,y)` | Component-wise matrix multiply |
| `outerProduct(c,r)` | Outer product of vectors |
| `transpose(m)` | Transpose matrix |
| `determinant(m)` | Matrix determinant |
| `inverse(m)` | Matrix inverse |

## Vector Relational
| Function | Description |
|----------|-------------|
| `lessThan(a,b)`, `lessThanEqual(a,b)` | Component-wise comparison |
| `greaterThan(a,b)`, `greaterThanEqual(a,b)` | Component-wise comparison |
| `equal(a,b)`, `notEqual(a,b)` | Component-wise equality |
| `any(bvec)`, `all(bvec)`, `not(bvec)` | Boolean reduction |

## Integer
| Function | Description |
|----------|-------------|
| `bitCount(x)`, `findLSB(x)`, `findMSB(x)` | Bit manipulation |
| `bitfieldExtract(value, offset, bits)` | Extract bitfield |
| `bitfieldInsert(base, insert, offset, bits)` | Insert bitfield |
| `bitfieldReverse(x)` | Reverse bits |
| `uaddCarry(a,b,out carry)`, `usubBorrow(a,b,out borrow)` | Add/sub with carry/borrow |
| `umulExtended(a,b,out msb, out lsb)`, `imulExtended(a,b,out msb, out lsb)` | Extended multiply |

## Atomic (SSBO/Shared Memory)
| Function | Description |
|----------|-------------|
| `atomicAdd(mem, data)` | Atomic addition |
| `atomicAnd(mem, data)`, `atomicOr(mem, data)`, `atomicXor(mem, data)` | Atomic bitwise |
| `atomicMin(mem, data)`, `atomicMax(mem, data)` | Atomic min/max |
| `atomicExchange(mem, data)` | Atomic exchange |
| `atomicCompSwap(mem, compare, data)` | Atomic compare-and-swap |
| `atomicCounterIncrement(counter)`, `atomicCounterDecrement(counter)` | Atomic counter ops |

## Derivatives (Fragment Shader Only)
| Function | Description |
|----------|-------------|
| `dFdx(p)`, `dFdy(p)` | Partial derivative in x/y |
| `fwidth(p)` | abs(dFdx(p)) + abs(dFdy(p)) |

## Noise (Deprecated in core, but available)
| Function | Description |
|----------|-------------|
| `noise1(x)`, `noise2(x)`, `noise3(x)`, `noise4(x)` | Perlin noise (deprecated) |

## Built-in Variables
| Variable | Stage | Description |
|----------|-------|-------------|
| `gl_Position` | Vertex/Tess/Geo | Clip-space output position |
| `gl_PointSize` | Vertex | Point sprite size |
| `gl_FragCoord` | Fragment | Fragment window coordinates (x,y,z,1/w) |
| `gl_FragDepth` | Fragment | Output fragment depth |
| `gl_FrontFacing` | Fragment | True if front-facing primitive |
| `gl_PointCoord` | Fragment | Point sprite texture coordinates |
| `gl_VertexID` | Vertex | Index of current vertex |
| `gl_InstanceID` | Vertex | Current instance ID |
| `gl_PrimitiveID` | Fragment/Geo | Primitive ID |
| `gl_GlobalInvocationID` | Compute | Global work-item ID |
| `gl_LocalInvocationID` | Compute | Local work-group ID |
| `gl_WorkGroupID` | Compute | Work group ID |
| `gl_NumWorkGroups` | Compute | Total number of work groups |
| `gl_ClipDistance[]` | Vertex/Tess/Geo | Per-vertex clip distances |
| `gl_CullDistance[]` | Vertex/Tess/Geo | Per-vertex cull distances |
