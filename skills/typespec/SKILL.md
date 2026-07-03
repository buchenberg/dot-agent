---
name: typespec
description: "TypeSpec API definition language — models, operations, interfaces, templates, decorators, HTTP/REST bindings, OpenAPI emission, server/client code generation, and best practices. Use when authoring, reviewing, or compiling TypeSpec (.tsp) files or designing APIs with TypeSpec. WHEN: TypeSpec, typespec, tsp, .tsp, API design, API definition, OpenAPI, openapi3, model, operation, interface, decorator, emitter, JSON Schema, Protobuf, gRPC, HTTP API, REST API, @typespec, tspconfig, tsp compile, tsp init, tsp format."
---

# TypeSpec — Complete API Design & Development Reference

## What is TypeSpec?

TypeSpec is an extensible, domain-specific language (DSL) by Microsoft for **defining cloud service APIs and data schemas**. It is a single-source-of-truth approach: describe APIs once in TypeSpec, then generate OpenAPI specs, JSON Schema, Protobuf, client SDKs, server stubs, and documentation from the same definition.

- **License**: MIT
- **Repository**: https://github.com/microsoft/typespec
- **Package**: `@typespec/compiler` (v1.x)
- **Prerequisite**: Node.js >= 22.0.0

---

## 1. Installation & Project Setup

```bash
npm install -g @typespec/compiler@latest
tsp --version

# New project
tsp init
tsp install
tsp compile .              # compile once
tsp compile . --watch      # watch mode
```

### Project structure

```
myproject/
├── main.tsp               # Entry point
├── tspconfig.yaml         # Compiler & emitter config
├── package.json           # Dependencies
├── node_modules/
└── tsp-output/            # Generated output
```

### tspconfig.yaml

```yaml
emit:
  - "@typespec/openapi3"
options:
  "@typespec/openapi3":
    emitter-output-dir: "{output-dir}/schema"
    openapi-versions:
      - 3.1.0
```

### package.json

```json
{
  "name": "my-api",
  "version": "0.1.0",
  "type": "module",
  "peerDependencies": {
    "@typespec/compiler": "latest",
    "@typespec/http": "latest",
    "@typespec/openapi3": "latest"
  },
  "devDependencies": {
    "@typespec/compiler": "latest",
    "@typespec/http": "latest",
    "@typespec/openapi3": "latest"
  },
  "private": true
}
```

---

## 2. Core Language Reference

### 2.1 Built-in Types

#### Numeric

| Type | Range |
|------|-------|
| `numeric` | Supertype for all numbers |
| `integer` | Whole-number supertype |
| `float` | Binary floating-point supertype |
| `decimal` | Decimal supertype |
| `int8` | -128 to 127 |
| `int16` | -32,768 to 32,767 |
| `int32` | -2,147,483,648 to 2,147,483,647 |
| `int64` | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `safeint` | -(2^53 - 1) to 2^53 - 1 (JSON-safe) |
| `uint8` | 0 to 255 |
| `uint16` | 0 to 65,535 |
| `uint32` | 0 to 4,294,967,295 |
| `uint64` | 0 to 18,446,744,073,709,551,615 |
| `float32` | 32-bit IEEE 754 |
| `float64` | 64-bit IEEE 754 |
| `decimal128` | 34 decimal digits, exponent -6143 to 6144 |

#### Temporal

| Type | Description |
|------|-------------|
| `plainDate` | Calendar date (no time/timezone) |
| `plainTime` | Clock time (no date/timezone) |
| `utcDateTime` | Instant in UTC |
| `offsetDateTime` | Date/time with UTC offset |
| `duration` | Time period (e.g., 5s, 10h) |
| `unixTimestamp32` | 32-bit seconds since epoch |

#### Other Primitives

| Type | Description |
|------|-------------|
| `string` | Text sequence |
| `boolean` | `true` or `false` |
| `bytes` | Byte sequence |
| `url` | URL string (WHATWG spec) |
| `null` | Null value |
| `void` | No return value |
| `never` | Type that never occurs |
| `unknown` | Top type — all types assignable |

#### Generic Models

| Type | Signature | Purpose |
|------|-----------|---------|
| `Array<Element>` | model Array\<Element\> | Homogeneous array, shorthand: `Element[]` |
| `Record<Element>` | model Record\<Element\> | String-keyed model, values of type Element |

---

### 2.2 Models

Models define structured data schemas.

```tsp
model Dog {
  id: int32;
  name: string;
  age: uint8 = 0;
  address?: string;             // optional
  address?: string = "wild";    // optional with default
}
```

#### Composition operators

| Operator | Meaning | Copies decorators? |
|----------|---------|--------------------|
| `extends` | Inheritance relationship | No |
| `is` | Exact copy + additions | **Yes** |
| `...` (spread) | Merge properties inline | No |

```tsp
model Animal { species: string; }
model Pet { name: string; }

model Dog extends Animal {}           // inheritance
model StringThing is Thing<string>;   // copy with decorators
model Dog { ...Animal; ...Pet; }      // spread — no nominal relationship
```

#### Template models

```tsp
model Page<Item> {
  size: int32;
  item: Item[];
}

model DogPage {
  ...Page<Dog>;
}
```

#### Property metadata access

```tsp
model Pet { name: string; }
// Pet.name::type  => references the type of 'name'
```

---

### 2.3 Operations

Operations represent service endpoints. Declared with `op`:

```tsp
op ping(): void;
op upload(filename: string, data: bytes): void;
op health(): HealthStatus;
```

#### Union return types

```tsp
op getDog(name: string): Dog | DogNotFound;
```

#### Parameter spread

```tsp
op feedDog(...CommonParams, name: string): void;
```

#### Reuse with `is`

```tsp
op Delete(id: string): void;
op deletePet is Delete;  // inherits parameters, return type, and decorators
```

#### Templates

```tsp
op ReadResource<T>(id: string): T;
op readPet is ReadResource<Pet>;
```

#### Meta type references

```tsp
readPet::parameters   // the parameters model
readPet::returnType   // the return type
```

---

### 2.4 Interfaces

Interfaces group operations for reuse.

```tsp
interface SampleInterface {
  foo(): int32;
  bar(): string;
}

// Interface composition
interface A { a(): string; }
interface B { b(): string; }
interface C extends A, B { c(): string; }
// C has: a(), b(), c()

// Interface templates
interface ReadWrite<T> {
  read(): T;
  write(t: T): void;
}
```

**Caution**: Templated operations inside an interface template are NOT included in service operations unless explicitly instantiated. Use aliases for building-block patterns:

```tsp
alias MyReadWrite = ReadWrite<string>;
op myRead is MyReadWrite.read;
op myWrite is MyReadWrite.write<int32>;
```

---

### 2.5 Enums

```tsp
// Basic enum (members are string values matching member names)
enum Direction {
  North,    // "North"
  East,     // "East"
  South,    // "South"
  West,     // "West"
}

// String-valued enum
enum Direction {
  North: "north",
  East: "east",
}

// Integer-valued enum
enum Foo {
  One: 1,
  Ten: 10,
  Hundred: 100,
}

// Float-valued enum
enum Hour {
  Zero: 0,
  Quarter: 0.25,
}

// Spread to combine
enum DirectionExt {
  ...Direction,
  `North East`,
  `North West`,
}

// Reference members
alias North = Direction.North;
```

---

### 2.6 Unions

```tsp
// Union expression (unnamed)
alias Breed = Beagle | GermanShepherd | GoldenRetriever;

// Named union (allows per-variant decorators)
union Breed {
  beagle: Beagle,
  shepherd: GermanShepherd,
  retriever: GoldenRetriever,
}
```

---

### 2.7 Scalars

```tsp
scalar ternary;
scalar Password extends string;
scalar ipv4 extends string {
  init fromInt(value: uint32);
}

const homeIp = ipv4.fromInt(2130706433);

// Built-in temporal constructors
const date = plainDate.fromISO("2024-05-06");
const timestamp = utcDateTime.fromISO("2024-05-06T12:20:00Z");
```

---

### 2.8 Templates

Templates (generics) can be applied to aliases, models, operations, and interfaces.

```tsp
model Page<Item> {
  size: int32;
  item: Item[];
}

// Default values
model Page<Item = string> { size: int32; item: Item[]; }

// Type constraints
alias Foo<Type extends string> = Type;
alias Foo<Type extends {name: string}> = Type;

// Named template arguments (skip or reorder optional params)
alias Test<T, U extends numeric = int32, V extends string = "example"> = { t: T; v: V; };
alias Example1 = Test<unknown, V = "example1">;
alias Example2 = Test<V = "example2", T = unknown, U = uint64>;

// Value templates
alias TakesValue<StringType extends string, StringValue extends valueof string> = {
  @doc(StringValue)
  property: StringType;
};
```

**Rule**: Once a named argument is used, all subsequent arguments must also be named. Optional arguments must come after required ones.

---

### 2.9 Namespaces & Imports

```tsp
// Block namespace
namespace SampleNamespace {
  model SampleModel {}
}

// Nested (two equivalent forms)
namespace Foo.Bar.Baz {
  model SampleModel {}
}
// or: namespace Foo { namespace Bar { namespace Baz { ... } } }

// File-level namespace (applies to all declarations in file)
namespace PetStore;

// Using — brings namespace contents into scope (not exported)
using SampleNamespace;

// Imports
import "./models/foo.tsp";          // TypeSpec file
import "./decorators.js";           // JS decorators
import "@typespec/rest";            // library
import "./models";                  // directory => main.tsp
```

---

### 2.10 Decorators

Decorators are the core extensibility mechanism. Defined in JavaScript and applied with `@`.

```tsp
@tag("Sample")
model Dog {
  @validate(false)
  name: string;
}

// Augment decorators — apply from a different location (must end with ;)
@@tag(Dog, "Sample");
@@visibility(Dog.name, Lifecycle.Read);

// Auto decorators (no JS implementation needed)
auto dec label(target: Model, value: valueof string);
```

---

### 2.11 Type Literals & Aliases

```tsp
alias Str = "Hello World!";
alias Num = 1000;
alias PI = 3.14;
alias IsTrue = true;

// Multi-line strings (auto-trims indentation to closing """)
alias Str = """
  This is a multi line string
   - opt 1
   - opt 2
  """;

// String template interpolation
alias hello = "bonjour";
alias Single = "${hello} world!";
```

---

### 2.12 Values (`#{}`, `#[]`, `const`)

```tsp
// Object values
const point = #{ x: 0, y: 0 };

// Array values
const points = #[#{ x: 0, y: 0 }, #{ x: 1, y: 1 }];

// Scalar values
const n = int8(100);
const s = string("hello");

// typeof operator
const stringValue: string = "hello";
// typeof stringValue => string

const oneValue = 1;
// typeof oneValue => 1 (exact literal type)
```

---

### 2.13 Documentation

#### `@doc` decorator

```tsp
@doc("This is a sample model")
model Dog {
  @doc("This is a sample property")
  name: string;
}

// Template doc with source object
@doc("Templated {name}", Type)
model Template<Type extends {}> {}
```

#### Doc comments (`/** */`) — preferred approach

```tsp
/**
 * Get a widget.
 * @param widgetId The ID of the widget to retrieve.
 * @returns The widget.
 * @template T the resource type
 */
op read(@path widgetId: string): Widget | Error;
```

| Tag | Purpose |
|-----|---------|
| `@param <name>` | Documents a parameter |
| `@returns` | Documents the operation response |
| `@template <T>` | Documents a template parameter |
| `@example` (unofficial) | Show examples |

#### Regular comments (not emitted)

```tsp
// Single-line — compiler ignores, does not emit
/* Multi-line — compiler ignores, does not emit */
```

#### Markdown support

All `@doc` and doc comment content supports **CommonMark** formatting:

```tsp
@doc("This is a **bold** text")
model Dog {
  @doc("This is a _italic_ text")
  name: string;

  /**
   * Contains a bullet list
   * - one
   * - two
   * and code blocks
   *
   * ```typescript
   * dog.age = 5;
   * ```
   */
  age: int32;
}
```

---

### 2.14 Directives

```tsp
// Deprecation
#deprecated "Use NewUser instead"
model LegacyUser {}

// Suppress specific warnings
model Post {
  #suppress "deprecated" "We are not ready to migrate yet"
  author: LegacyUser;
}
```

---

## 3. Built-in Decorators Reference

### Documentation

| Decorator | Signature | Target |
|-----------|-----------|--------|
| `@doc` | `@doc(doc: valueof string, formatArgs?: {})` | Any type |
| `@summary` | `@summary(summary: valueof string)` | Any type |
| `@errorsDoc` | `@errorsDoc(doc: valueof string)` | Operation |
| `@returnsDoc` | `@returnsDoc(doc: valueof string)` | Operation |

### Type Structure

| Decorator | Signature | Target |
|-----------|-----------|--------|
| `@key` | `@key(altName?: valueof string)` | ModelProperty |
| `@error` | `@error` | Model |
| `@discriminator` | `@discriminator(propertyName: valueof string)` | Model |
| `@discriminated` | `@discriminated(options?: valueof DiscriminatedOptions)` | Union |
| `@service` | `@service(options?: valueof ServiceOptions)` | Namespace |
| `@secret` | `@secret` | Scalar, ModelProperty, Model, Union, Enum |

### Validation

| Decorator | Target types |
|-----------|-------------|
| `@minLength(n)`, `@maxLength(n)` | `string`, ModelProperty |
| `@minItems(n)`, `@maxItems(n)` | `unknown[]`, ModelProperty |
| `@minValue(n)`, `@maxValue(n)` | numeric/datetime types |
| `@minValueExclusive(n)`, `@maxValueExclusive(n)` | numeric/datetime types |
| `@pattern(regex, message?)` | `string`, `bytes`, ModelProperty |

### Encoding & Serialization

| Decorator | Purpose |
|-----------|---------|
| `@encode(encoding, encodedAs?)` | Specify wire format (e.g., `@encode("rfc3339")` on datetime, `@encode(string)` on numeric) |
| `@encodedName(mimeType, name)` | Alternative serialized name per MIME type |
| `@format(format)` | Format hint (e.g., `"uuid"`, `"uri"`, `"email"`) |
| `@mediaTypeHint(mediaType)` | Hint for serialization (e.g., `"application/xml"`) |

### Visibility (Lifecycle)

```tsp
model Example {
  @visibility(Lifecycle.Read) id: string;
  @visibility(Lifecycle.Create, Lifecycle.Read) name: string;
  description: string;  // all phases by default
}
```

| Decorator | Purpose |
|-----------|---------|
| `@visibility(...visibilities)` | Add visibility modifiers |
| `@removeVisibility(...visibilities)` | Remove specific modifiers |
| `@invisible(Class)` | Remove all modifiers in a class |
| `@defaultVisibility(...visibilities)` | Set defaults for a visibility enum |
| `@parameterVisibility(...visibilities)` | Constrain operation parameters |
| `@returnTypeVisibility(...visibilities)` | Constrain operation return types |

Lifecycle enum members: `Create`, `Read`, `Update`, `Delete`, `Query`.

### Model Transformations

| Decorator | Effect |
|-----------|--------|
| `@withVisibility(...visibilities)` | Keep only properties matching all given visibilities |
| `@withOptionalProperties` | Make all properties optional |
| `@withoutDefaultValues` | Strip default values |
| `@withoutOmittedProperties(omit)` | Remove specified properties |
| `@withPickedProperties(pick)` | Keep only specified properties |
| `@withUpdateableProperties` | Keep only updateable properties |

### Pagination

| Decorator | Target | Purpose |
|-----------|--------|---------|
| `@list` | Operation | Marks a list operation |
| `@pageItems` | ModelProperty | Items array field |
| `@continuationToken` | ModelProperty | Token for next page |
| `@nextLink` / `@prevLink` / `@firstLink` / `@lastLink` | ModelProperty | Link-based pagination |
| `@offset` / `@pageIndex` / `@pageSize` | ModelProperty | Offset/index pagination |

### Other

| Decorator | Purpose |
|-----------|---------|
| `@tag(tag)` | Categorize operations |
| `@friendlyName(name)` | Custom display name |
| `@overload(overloadbase)` | Operation overload |
| `@example(value)` | Example value |
| `@opExample(example)` | Operation-level example |

---

## 4. HTTP & REST Protocol Bindings

### 4.1 HTTP library (`@typespec/http`)

```tsp
import "@typespec/http";
using Http;

@route("/pets")
namespace Pets {
  @get op listPets(): {
    @statusCode statusCode: 200;
    @body pets: Pet[];
  };

  @get op getPet(@path petId: int32):
    | { @statusCode statusCode: 200; @body pet: Pet; }
    | { @statusCode statusCode: 404; };

  @post op createPet(@body pet: Pet):
    | { @statusCode statusCode: 201; @body newPet: Pet; }
    | { @statusCode statusCode: 400; @body error: ValidationError; };

  @put op updatePet(@path petId: int32, @body pet: Pet): ...;

  @delete op deletePet(@path petId: int32): {
    @statusCode statusCode: 204;
  };
}
```

#### HTTP method decorators

`@get`, `@put`, `@post`, `@patch`, `@delete`, `@head`

**Default**: If no method decorator is given: `post` if there's a `@body`, otherwise `get`.

#### Parameter decorators

| Decorator | Purpose |
|-----------|---------|
| `@path` | Path parameter |
| `@query` | Query string parameter |
| `@header` | HTTP header parameter |
| `@body` | Request body |
| `@statusCode` | HTTP status code on response |

#### Error responses

```tsp
@error
model NotFoundError {
  code: "NOT_FOUND";
  message: string;
}

@error
model ValidationError {
  code: "VALIDATION_ERROR";
  message: string;
  details: string[];
}
```

#### Composable response models

Standard response models from `@typespec/http`: `OkResponse`, `CreatedResponse`, `AcceptedResponse`, `NoContentResponse`, `BadRequestResponse`, `UnauthorizedResponse`, `NotFoundResponse`, `ForbiddenResponse`, `ConflictResponse`.

```tsp
model PetResponse {
  ...OkResponse;
  ...Body<Pet>;
}

model PetErrorResponse {
  ...BadRequestResponse;
  ...Body<ValidationError>;
}

// Clean operation signatures
op getPet(@path petId: int32):
  PetResponse | PetNotFoundResponse;
```

#### Route hierarchy via nested namespaces

```tsp
@route("/widgets")
namespace Widgets {
  @route("/{id}/parts")
  namespace Parts {
    op list(@path id: string): Part[];
    // Final path: /widgets/{id}/parts
  }
}
```

#### Security / Authentication

```tsp
@useAuth(BearerAuth)
@post op createPet(...): ...;

// OAuth2
@useAuth(OAuth2Auth<["read", "write"]>)
namespace MyService;
```

### 4.2 REST library (`@typespec/rest`)

Provides `@resource`, `@readsResource`, `@createsResource`, `@action`, `@autoRoute`, `@segment`, etc. for RESTful API patterns.

---

## 5. Versioning (`@typespec/versioning`)

```tsp
import "@typespec/versioning";
using Versioning;

@versioned(Versions)
namespace PetStore;

enum Versions {
  v1: "1.0",
  v2: "2.0",
}

@added(Versions.v2)
model Toy {
  id: int32;
  name: string;
}

@added(Versions.v2)
@get op listToys(@path petId: int32): Toy[] | Error;
```

Generates separate OpenAPI specs per version: `openapi.1.0.yaml`, `openapi.2.0.yaml`.

---

## 6. Emitters

### OpenAPI 3 (`@typespec/openapi3`)

```bash
npm install @typespec/openapi3
# tspconfig.yaml: emit: ["@typespec/openapi3"]
```

### JSON Schema (`@typespec/json-schema`)

Emits JSON Schema from TypeSpec definitions.

### Protobuf (`@typespec/protobuf`)

Emits `.proto` files for gRPC services.

### HTTP Client SDKs

`@typespec/http-client-js`, `@typespec/http-client-csharp`, `@typespec/http-client-java`, `@typespec/http-client-python`

### HTTP Server Stubs

`@typespec/http-server-csharp`, `@typespec/http-server-js`

---

## 7. Best Practices & Patterns

### 7.1 Reusable parameters

```tsp
model CommonParameters {
  @header requestID: string;
  @query locale?: string;
  @header clientVersion?: string;
}

// Spread across operations
@get op listPets(...CommonParameters): PetListResponse;
@get op getPet(@path petId: int32, ...CommonParameters): PetResponse | Error;
```

### 7.2 Discriminated unions (polymorphism)

```tsp
@discriminator("kind")
model Pet { name: string; weight?: float32; }
model Cat extends Pet { kind: "cat"; meow?: int32; }
model Dog extends Pet { kind: "dog"; bark?: string; }

@discriminated(#{ envelope: "none" })
union Pet {
  cat: Cat,
  dog: Dog,
}
```

### 7.3 Additional properties with `Record<T>`

```tsp
model Bar extends Record<unknown> { bar?: string; }   // allows extra properties
model Strict { bar: Record<never>; }                   // forbids extra properties
model StringMap { bar: Record<string>; }               // typed extra properties
```

### 7.4 Service metadata

```tsp
@service(#{ title: "Widget Service" })
@server("https://example.com", "Single server endpoint")
namespace WidgetService;

@info(#{
  contact: #{ name: "API Support", email: "contact@contoso.com" },
  license: #{ name: "Apache 2.0", url: "https://www.apache.org/licenses/LICENSE-2.0.html" },
})
```

### 7.5 Multiple content types

```tsp
@put op uploadImage(@header contentType: "image/png", @body image: bytes): void;

@sharedRoute @post op process(...Widget): Widget | Error;
@sharedRoute @post op processCsv(...CsvBody): Widget | Error;
```

### 7.6 Pagination

```tsp
@list
op listPets(...CommonParameters): {
  @pageItems pets: Pet[];
  @nextLink next?: url;
};

// Or offset-based
@list
op listPets(@offset offset: int32, @pageSize pageSize: int32): {
  @pageItems pets: Pet[];
};
```

---

## 8. CLI Commands

```bash
tsp compile <path>              # Compile TypeSpec source
tsp compile <path> --watch      # Watch mode
tsp init [templateUrl]          # Create a new project
tsp install                     # Install dependencies
tsp format "**/*.tsp"          # Format source files
tsp format --check "**/*.tsp"  # CI check (dry-run)
tsp info                        # Compiler version info
tsp code                        # Manage VS Code extension
tsp vs                          # Manage Visual Studio extension
```

---

## 9. Style Guide Summary

| Construct | Convention | Example |
|-----------|-----------|---------|
| scalar | camelCase | `scalar uuid extends string;` |
| model | PascalCase | `model Pet {}` |
| model property | camelCase | `model Pet { furColor: string }` |
| enum | PascalCase | `enum Direction {}` |
| enum member | camelCase | `enum Direction { up, down }` |
| namespace | PascalCase.dotted | `namespace Org.PetStore` |
| interface | PascalCase | `interface Stores {}` |
| operation | camelCase | `op listPets(): Pet[];` |
| operation params | camelCase | `op getPet(petId: string): Pet;` |
| unions | PascalCase | `union Pet { cat: Cat, dog: Dog }` |
| union variant | camelCase | `cat: Cat` |
| decorators | camelCase | `@format`, `@resourceCollection` |
| file name | kebab-case | `my-lib.tsp` |
| template param | PascalCase | `<ExampleParameter>` |

**Forbidden**: `I` prefix on interfaces, `T` prefix on template params.

**Formatting**: 2-space indent, space before `{`, no spaces inside `()`, spaces inside `{}`, no trailing spaces.

---

## 10. TypeSpec Package Ecosystem

| Category | Package |
|----------|---------|
| **Compiler** | `@typespec/compiler` |
| **Protocols** | `@typespec/http`, `@typespec/rest`, `@typespec/versioning`, `@typespec/events`, `@typespec/streams`, `@typespec/sse`, `@typespec/xml` |
| **Emitters** | `@typespec/openapi3`, `@typespec/json-schema`, `@typespec/protobuf`, `@typespec/html-program-viewer` |
| **Client SDKs** | `@typespec/http-client-js`, `@typespec/http-client-csharp`, `@typespec/http-client-java`, `@typespec/http-client-python` |
| **Server Stubs** | `@typespec/http-server-csharp`, `@typespec/http-server-js` |
| **Tooling** | `@typespec/prettier-plugin-typespec`, `@typespec/tspd`, `@typespec/playground` |

---

## References

- TypeSpec home: https://typespec.io
- GitHub: https://github.com/microsoft/typespec
- Playground: https://typespec.io/playground/
- Style guide: https://typespec.io/docs/handbook/style-guide/
