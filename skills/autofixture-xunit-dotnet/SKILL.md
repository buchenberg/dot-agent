---
name: autofixture-xunit-dotnet
description: "AutoFixture + xUnit patterns for .NET tests — custom ISpecimenBuilder, ICustomization, and extending AutoDataAttribute / InlineAutoDataAttribute. Use when authoring or refactoring xUnit tests that need anonymous test data, parameter-name-targeted specimen generation, or shared customization across many tests. WHEN: AutoFixture, AutoData, InlineAutoData, ISpecimenBuilder, ICustomization, specimen builder, anonymous test data, fixture.Customize, custom AutoDataAttribute, .NET unit tests, xUnit theory data, refactor tests to AutoFixture, generate test data, test data builder."
---

# AutoFixture + xUnit (.NET)

Patterns for using AutoFixture in xUnit tests: writing `ISpecimenBuilder`s,
packaging them in `ICustomization`s, and exposing them via `AutoDataAttribute` /
`InlineAutoDataAttribute` subclasses for clean `[Theory]` data injection.

## When to use
- Test setups have repetitive Arrange code building anonymous data.
- A type cannot be constructed by AutoFixture's defaults (e.g., interfaces, abstract types, types pulling in `Microsoft.Extensions.Primitives.StringValues`).
- A property/parameter needs domain-specific format (e.g., codes, IDs).
- Multiple tests share the same fixture customization.

## When NOT to use
- A single `[Fact]` test with trivial inputs — `new T(...)` is clearer.
- Behavior under specific edge values — use `[InlineData]` directly; AutoFixture is for *anonymous* data.

## Packages

```xml
<PackageReference Include="AutoFixture" Version="4.18.1" />
<PackageReference Include="AutoFixture.Xunit2" Version="4.18.1" />
```

- `AutoFixture` — core engine.
- `AutoFixture.Xunit2` — `AutoDataAttribute` and `InlineAutoDataAttribute`.
- (Optional) `AutoFixture.AutoMoq` — automatic mock injection for interfaces.

4.18.1 targets netstandard2.0 and works on net10 as of 2026.

## Core concepts
- **Specimen** — example value of a type (an `int`, a `string`, an `Employee`).
- **`ISpecimenBuilder`** — strategy that returns either a built specimen or `new NoSpecimen()` when it cannot satisfy the request.
- **`ICustomization`** — bundles one or more builders so a fixture can be configured with one line.
- **`AutoDataAttribute`** — xUnit `DataAttribute` that injects auto-generated values as `[Theory]` parameters.
- **`InlineAutoDataAttribute`** — combines `[InlineData(...)]` values for the leading parameters with auto-generated values for the rest.

## Pattern 1 — Type-targeted specimen builder

For when AutoFixture cannot build a type at all (third-party interfaces, types with unbuildable members):

```csharp
public sealed class OrderContextSpecimenBuilder : ISpecimenBuilder
{
    public object Create(object request, ISpecimenContext context)
    {
        if (request is Type t && t == typeof(OrderContext))
        {
            return OrderContext.Empty;
        }
        return new NoSpecimen();
    }
}
```

## Pattern 2 — Parameter/property-name-targeted builder

For when a specific *named* parameter or property needs a format:

```csharp
public sealed class ItemUriSpecimenBuilder : ISpecimenBuilder
{
    public object Create(object request, ISpecimenContext context)
    {
        if (request is ParameterInfo p &&
            p.Name?.Equals("itemUri", StringComparison.OrdinalIgnoreCase) == true &&
            p.ParameterType == typeof(Uri))
        {
            return new Uri($"https://example.com/items/{Guid.NewGuid()}");
        }
        return new NoSpecimen();
    }
}
```

`PropertyInfo` is also a valid request shape — use it for properties on POCOs.

## Pattern 3 — `ICustomization` to bundle builders

```csharp
public sealed class MyCustomization : ICustomization
{
    public void Customize(IFixture fixture)
    {
        fixture.Customizations.Add(new OrderContextSpecimenBuilder());
        fixture.Customizations.Add(new ItemUriSpecimenBuilder());
    }
}
```

## Pattern 4 — Extend `AutoDataAttribute` (and `InlineAutoDataAttribute`)

Wraps the customization so individual tests don't repeat fixture setup:

```csharp
public sealed class MyAutoDataAttribute : AutoDataAttribute
{
    public MyAutoDataAttribute()
        : base(() => new Fixture().Customize(new MyCustomization()))
    {
    }
}

public sealed class MyInlineAutoDataAttribute : InlineAutoDataAttribute
{
    public MyInlineAutoDataAttribute(params object[] values)
        : base(new MyAutoDataAttribute(), values)
    {
    }
}
```

Usage:

```csharp
[Theory, MyAutoData]
public void Some_test(MyService sut, OrderContext context) { /* ... */ }

[Theory]
[MyInlineAutoData(ItemStatus.Closed)]
[MyInlineAutoData(ItemStatus.Paused)]
public void Status_drives_branch(ItemStatus status, MyService sut) { /* ... */ }
```

## Common pitfalls
- **Order matters**: `fixture.Customizations` is consulted in registration order, so register narrower builders before broader ones if they overlap.
- **`NoSpecimen` vs `null`**: never return `null` from a builder when you can't satisfy a request — return `new NoSpecimen()` so the pipeline can fall through.
- **Recursion**: AutoFixture aborts on cycles in object graphs. Replace `ThrowingRecursionBehavior` with `OmitOnRecursionBehavior` only for genuine cycles.
- **Value-type collections**: AutoFixture populates dictionaries/lists with random data, which can pollute assertions. Add a builder returning empty collections when relevant.
- **`StringValues` / Primitives**: types depending on `Microsoft.Extensions.Primitives.StringValues` (or similar) can fail to construct — handle with a type-targeted builder returning a known-good factory like `T.Empty`.
- **Records with `init`-only properties**: AutoFixture sets them via constructor or property setter; if your record has computed members that don't round-trip, register a customization using `fixture.Customize<T>(c => c.With(...).OmitAutoProperties())`.
- **Don't auto-resolve when assertions need reference equality**: if a test asserts the *same instance* of an injected dependency, construct the SUT manually inside the test instead of letting AutoFixture build it.

## References
- Vidisha Parab, "AutoFixture - Specimen Builders" — https://dev.to/vparab/autofixture-specimen-builders-135k
- Adam Storr, "AutoFixture — Generate Specific Format Values By Extending AutoDataAttribute" — https://adamstorr.co.uk/blog/autofixture-generate-specific-format-values-by-extending-autodataattribute/
- Mark Seemann, "Convention-based Customizations with AutoFixture" — https://blog.ploeh.dk/2010/10/19/Convention-basedCustomizationswithAutoFixture/

## Lessons learned (rolling)
<!-- Append new entries here as patterns/pitfalls are discovered. Format:
- YYYY-MM-DD: <observation>
-->
- 2026-06-11: `System.Text.Json.JsonElement` cannot be built by default AutoFixture because it transitively references the ref struct `Utf8JsonReader&`. Any type containing a `Dictionary<string, JsonElement>` (very common for `[JsonExtensionData]` properties) will throw `ObjectCreationExceptionWithPath`. Fix with a type-targeted builder returning `default(JsonElement)` — covers every occurrence at once and is preferable to chasing individual properties with `c.Without(...)`.
- 2026-06-11: AutoFixture populates `List<T>` and `Dictionary<,>` property bags with three random entries by default. Tests asserting collection size (`ContainSingle()`, `BeEmpty()`) must `.Clear()` the collection on the auto-resolved instance before mutating it, or assert membership (`Contain(item)`) instead.
- 2026-06-11: AutoFixture 4.18.1 (netstandard2.0) works without issues on net10 / .NET 10.
