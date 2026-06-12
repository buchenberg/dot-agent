---
description: Sanitize agent skills by replacing domain-specific class names, property names, and verbiage with generic vanilla equivalents, and removing sensitive information. Use when importing a skill from a real project into a shared/public skill library, or when reviewing existing skills for domain leakage. WHEN: sanitize skill, genericize, remove domain names, make skill generic, strip sensitive data, clean skill for sharing.
---

# Sanitize Skill for Sharing

Step-by-step instructions for taking a skill written in the context of a specific project and making it **generic and safe** for inclusion in a shared skill library like `dot-agent`.

## Why

Skills born from real projects carry domain fingerprints — internal class names, proprietary terminology, connection strings, tenant IDs, internal URLs, and jargon that only makes sense in one company. Before a skill goes into a shared library, all of that must be replaced with vanilla equivalents so the skill is universally useful.

## Process

### 1. Read the entire skill

Read `SKILL.md` (and any files in `references/`, `templates/`, `scripts/`) completely before editing.

### 2. Identify domain-specific elements

Scan for these categories:

**Code identifiers to replace:**
- Class names that reference specific business concepts (e.g., `RouteDispositionBuilder`, `RoutingSession`, `MatchUriSpecimenBuilder`, `RouteCode`)
- Enum members tied to a specific domain (e.g., `ProjectStatus.Closed` → `ItemStatus.Closed`)
- Method names containing domain verbs (e.g., `GetRouteDisposition()` → `GetItemStatus()`)
- Property/parameter names (e.g., `matchUri` → `itemUri`, `routeCode` → `itemCode`)
- Namespace segments that are company-specific

**Verbiage to replace:**
- Internal project or product names in descriptions and comments
- Company-specific jargon or acronyms
- References to internal systems, services, or APIs by name
- Team names or internal process references

**Sensitive data to remove/replace:**
- Connection strings, API keys, tokens, secrets
- Internal URLs, hostnames, tenant IDs, subscription IDs
- Email addresses, names, or any PII
- Internal ticket numbers, PR numbers, commit SHAs (unless they reference a public repo)
- Internal file paths or server names

### 3. Choose generic replacements

Use these conventions for replacements:

| Domain concept | Generic replacement |
|---|---|
| Routes, routing | Items, orders, widgets |
| Disposition, status-specific | Status, state |
| Sessions | Context, session (keep if generic) |
| Match, matching | Item, entity |
| Code (business code) | Code, identifier |
| Company-specific prefix | Remove entirely |

For placeholder class names, prefer:
- `Widget*`, `Item*`, `Order*` for business entities
- `Sample*`, `Example*` for demonstration classes
- `My*` for user-extensible base classes (e.g., `MyAutoDataAttribute` — this is already generic and fine to keep)

### 4. Apply replacements consistently

- Replace ALL occurrences — class definitions, usages in code blocks, references in prose
- Update the skill's `description` frontmatter to use generic terminology
- Update the `## When to use` and `## When NOT to use` sections
- Keep code examples compilable — if you rename a class in a code block, rename it everywhere it appears

### 5. Preserve what should stay

**Do NOT replace:**
- Framework/library class names (`AutoFixture`, `IFixture`, `ISpecimenBuilder`, `xUnit`, etc.)
- Package names and versions
- Public blog posts, documentation URLs, and reference links
- Generic programming terms (fixture, specimen, builder, customization)
- The structural patterns and advice — those are the skill's value

### 6. Final review checklist

- [ ] No class names reference a specific business domain
- [ ] No internal URLs, hostnames, or connection strings remain
- [ ] No company names, team names, or internal project names in prose
- [ ] No PII (names, emails, IDs) anywhere in the skill
- [ ] Code examples are internally consistent (all renamed classes match)
- [ ] The `description` frontmatter is generic
- [ ] External references (public URLs, package refs) are intact

## Example transformation

**Before (domain-specific):**
```csharp
public sealed class RoutingSessionSpecimenBuilder : ISpecimenBuilder
{
    public object Create(object request, ISpecimenContext context)
    {
        if (request is Type t && t == typeof(RoutingSession))
            return RoutingSession.Empty;
        return new NoSpecimen();
    }
}
```

**After (generic):**
```csharp
public sealed class OrderContextSpecimenBuilder : ISpecimenBuilder
{
    public object Create(object request, ISpecimenContext context)
    {
        if (request is Type t && t == typeof(OrderContext))
            return OrderContext.Empty;
        return new NoSpecimen();
    }
}
```

The *pattern* (type-targeted specimen builder returning a factory `.Empty`) is preserved. The domain dressing (routing) is replaced with a vanilla concept (order).

## Pitfalls

- **Partial rename**: The most common mistake — renaming a class in its definition but missing a usage in a different code block or in prose. Grep the whole file.
- **Breaking code examples**: If a renamed class has members (`RoutingSession.Empty`), make sure the replacement also has that member (`OrderContext.Empty`). Don't leave dangling references.
- **Over-sanitizing**: Don't replace things that are genuinely generic. `Session` is fine if it means a generic session. `Builder` is fine. Only replace domain-specific terms.
- **Forgetting the description**: The frontmatter `description` is the most visible part of a skill. Make sure it reads cleanly with no domain leakage.
- **Leaving breadcrumbs**: Internal PR numbers, JIRA tickets, or commit SHAs in "lessons learned" sections. Replace with dates or remove entirely.
