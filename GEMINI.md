# MemoryGraph: Persistent Memory for Gemini CLI

MemoryGraph gives you persistent, graph-based memory across coding sessions. Solutions you find today are searchable tomorrow. Patterns you learn in one project transfer to another.

## When to Use Memory

### Recall First, Always

Before starting any task, search for relevant prior knowledge:

```
recall_memories(query="redis timeout")
recall_memories(query="authentication patterns")
recall_memories(query="this project's architecture")
```

Search for:
- Bug patterns you've seen before
- Solutions that worked (or didn't)
- Code patterns for this tech stack
- Project-specific decisions and context

### Store After Notable Work

When you complete something worth remembering:

**Bug fixes**: Store the problem and solution, link them
```
problem_id = store_memory(type="problem", title="Redis connection timeout under load", ...)
solution_id = store_memory(type="solution", title="Increase connection pool size", ...)
create_relationship(solution_id, problem_id, "SOLVES")
```

**Errors resolved**: Store the error and fix
```
error_id = store_memory(type="error", title="CORS preflight failing", ...)
fix_id = store_memory(type="fix", title="Add OPTIONS handler", ...)
create_relationship(fix_id, error_id, "SOLVES")
```

**Patterns discovered**: Store as code_pattern
```
store_memory(type="code_pattern", title="FastAPI dependency injection pattern", ...)
```

**Decisions made**: Store with rationale
```
store_memory(type="project", title="Chose PostgreSQL over MongoDB", content="Rationale: need strong consistency for financial data...")
```

## Memory Types

Use the appropriate type for better retrieval:

| Type | Use For |
|------|---------|
| `problem` | Bugs, issues, blockers encountered |
| `solution` | Working fixes, approaches that succeeded |
| `error` | Specific error messages and stack traces |
| `fix` | Code changes that resolved errors |
| `code_pattern` | Reusable code patterns and idioms |
| `technology` | Tech stack knowledge, library usage |
| `task` | Completed work worth remembering |
| `workflow` | Process patterns, CI/CD configs |
| `project` | Project-specific context and decisions |
| `command` | Useful CLI commands and scripts |
| `file_context` | Important file locations and purposes |
| `general` | Anything else worth remembering |

## Relationship Types

Connect related memories for richer retrieval:

**Causal**: `CAUSES`, `TRIGGERS`, `LEADS_TO`, `PREVENTS`, `BREAKS`
**Solution**: `SOLVES`, `ADDRESSES`, `ALTERNATIVE_TO`, `IMPROVES`, `REPLACES`
**Context**: `OCCURS_IN`, `APPLIES_TO`, `WORKS_WITH`, `REQUIRES`, `USED_IN`
**Learning**: `BUILDS_ON`, `CONTRADICTS`, `CONFIRMS`, `GENERALIZES`, `SPECIALIZES`
**Workflow**: `FOLLOWS`, `DEPENDS_ON`, `ENABLES`, `BLOCKS`, `PARALLEL_TO`
**Quality**: `EFFECTIVE_FOR`, `INEFFECTIVE_FOR`, `PREFERRED_OVER`, `DEPRECATED_BY`

## Importance Scoring

Set importance based on reusability:

| Score | Use For |
|-------|---------|
| 0.8 - 1.0 | Cross-project patterns, critical fixes |
| 0.5 - 0.7 | Project-specific but valuable knowledge |
| 0.3 - 0.4 | Minor details, routine completions |

## Available Tools

### recall_memories
Natural language search across all memories.
```
recall_memories(query="how did we handle rate limiting")
```

### search_memories
Structured search with filters.
```
search_memories(query="timeout", memory_types=["solution", "fix"], tags=["redis"])
```

### store_memory
Create a new memory.
```
store_memory(
    type="solution",
    title="Redis connection pool tuning",
    content="Set pool_size=50 and max_overflow=10 for high-concurrency...",
    tags=["redis", "performance", "connection-pool"],
    importance=0.8
)
```

### create_relationship
Link two memories.
```
create_relationship(
    from_memory_id="solution_abc",
    to_memory_id="problem_xyz",
    relationship_type="SOLVES"
)
```

### get_related_memories
Find connected memories.
```
get_related_memories(memory_id="error_123", relationship_types=["SOLVES"])
```

### get_recent_activity
See what's been stored recently.
```
get_recent_activity(days=7)
```

## Best Practices

1. **Search before solving**: Always check if you've seen this problem before
2. **Link solutions to problems**: Unlinked memories lose context
3. **Use specific titles**: "Fixed Redis timeout" not "Fixed bug"
4. **Tag consistently**: Use lowercase, include tech names
5. **Store failures too**: What didn't work is valuable knowledge

## Integration with Conductor

If you're using Conductor for context-driven development:

- **After `/conductor:setup`**: Store project context as memories
- **During implementation**: Recall relevant patterns for the tech stack
- **After completing a track**: Extract learnings before archiving
- **When archiving**: Store key decisions and patterns

MemoryGraph turns Conductor's "archive and forget" into "archive and learn."
