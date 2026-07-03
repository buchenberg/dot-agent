---
description: Sanitize dot-agent content by replacing domain-specific class names, property names, and verbiage with generic vanilla equivalents, and removing sensitive information. Covers all content types — skills (SKILL.md + references/), agents (*.agent.yaml), rules, commands, context, and hooks. Use when importing content from a real project into this shared/public library, or when reviewing existing content for domain leakage. WHEN: sanitize, genericize, remove domain names, make content generic, strip sensitive data, clean for sharing, audit for leakage.
---

# Sanitize Content for Sharing

Step-by-step instructions for taking content written in the context of a specific project and making it **generic and safe** for inclusion in this shared library. Applies to every content type under `content/`:

- **skills** — `content/skills/<name>/SKILL.md` and any `references/`, `templates/`, `scripts/` files
- **agents** — `content/agents/*.agent.yaml` (especially `system_prompt`, `voice`, `description`)
- **rules / commands / context / hooks** — `content/<type>/*.md`

## Why

Content born from real projects carries domain fingerprints — internal class names, proprietary terminology, connection strings, tenant IDs, internal URLs, and jargon that only makes sense in one company. Before any file goes into this library, all of that must be replaced with vanilla equivalents so the content is universally useful. This is a stated invariant of the repo: *all content is domain-agnostic and sanitized*.

## Process

### 1. Read the entire content unit

Read every file in the unit completely before editing. For a skill, that means `SKILL.md` **and** all files in `references/`, `templates/`, `scripts/`. For an agent, the whole `.agent.yaml`. Consistency requires seeing every occurrence before you start renaming.

### 2. Identify domain-specific elements

Scan every file for these categories:

**Code identifiers to replace:**
- Class names that reference specific business concepts (e.g., `RouteDispositionBuilder`, `RoutingSession`, `MatchUriSpecimenBuilder`, `RouteCode`)
- Enum members tied to a specific domain (e.g., `ProjectStatus.Closed` → `ItemStatus.Closed`)
- Method names containing domain verbs (e.g., `GetRouteDisposition()` → `GetItemStatus()`)
- Property/parameter names (e.g., `matchUri` → `itemUri`, `routeCode` → `itemCode`)
- Namespace segments that are company-specific

**Verbiage to replace:**
- Internal project or product names in descriptions, comments, and agent system prompts
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
- `My*` for user-extensible base classes (e.g., `MyAutoDataAttribute` — already generic and fine to keep)

### 4. Apply replacements consistently

- Replace ALL occurrences — class definitions, usages in code blocks, references in prose, and across every file in the unit (a class renamed in `SKILL.md` must also be renamed in `references/*.md`).
- Update the frontmatter `description` to use generic terminology.
- For agents, update `system_prompt`, `voice`, and `description` fields.
- For skills, update the `## When to use` and `## When NOT to use` sections.
- Keep code examples compilable — if you rename a class in a code block, rename it everywhere it appears.

### 5. Preserve what should stay

**Do NOT replace:**
- Framework/library class names (`AutoFixture`, `IFixture`, `ISpecimenBuilder`, `xUnit`, JUCE classes, etc.)
- Package names and versions
- Public blog posts, documentation URLs, and reference links (Khronos, isocpp, Microsoft Learn, GitHub, npm, etc.)
- Generic programming terms (fixture, specimen, builder, customization, plugin, processor)
- The structural patterns and advice — those are the content's value

### 6. Final review checklist

Run this against **every** file in the unit:

- [ ] No class names reference a specific business domain
- [ ] No internal URLs, hostnames, or connection strings remain
- [ ] No company names, team names, or internal project names in prose or prompts
- [ ] No PII (names, emails, IDs) anywhere
- [ ] Code examples are internally consistent (all renamed classes match) — grep the whole unit
- [ ] The frontmatter `description` is generic
- [ ] Agent `system_prompt` / `voice` contain no domain leakage
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

- **Partial rename**: The most common mistake — renaming a class in its definition but missing a usage in a different code block, a `references/` file, or in prose. Grep the whole unit, not just the file you're editing.
- **Breaking code examples**: If a renamed class has members (`RoutingSession.Empty`), make sure the replacement also has that member (`OrderContext.Empty`). Don't leave dangling references.
- **Over-sanitizing**: Don't replace things that are genuinely generic. `Session` is fine if it means a generic session. `Builder` is fine. Only replace domain-specific terms.
- **Forgetting the description**: The frontmatter `description` is the most visible part of a skill. Make sure it reads cleanly with no domain leakage.
- **Leaving breadcrumbs**: Internal PR numbers, JIRA/ticket IDs, or commit SHAs in "lessons learned" sections. Replace with dates or remove entirely.
- **Cross-file drift**: A skill with `references/` is one unit. Renaming in `SKILL.md` but not in a reference file breaks consistency. Always grep across the whole directory.
