# Best Practices for MemoryGraph

Memory hygiene patterns for building a useful, searchable knowledge base.

## Core Principles

### 1. Recall First, Always

**Before starting any task**, search for relevant prior knowledge:

```
> I'm about to implement rate limiting. What do I know about this?
> Search for authentication patterns in FastAPI
> Have I seen this error before?
```

**Why**: Your past self may have already solved this problem.

### 2. Store After Notable Work

**After solving something**, store it:

```
> Store this solution: Fixed the N+1 query problem by using selectinload()
```

**Why**: Today's solution is tomorrow's time-saver.

### 3. Link Related Memories

**Connect solutions to problems**:

```
> Link that solution to the timeout problem I stored yesterday
```

**Why**: Unlinked memories lose context. Linked memories form a knowledge graph.

---

## What to Store

### Always Store

| Event | Memory Type | Example |
|-------|-------------|---------|
| Bug fixed | `problem` + `solution` | "Fixed CORS error by adding OPTIONS handler" |
| Error resolved | `error` + `fix` | "Connection timeout - increased pool size" |
| Pattern discovered | `code_pattern` | "Dependency injection pattern in FastAPI" |
| Decision made | `project` | "Chose PostgreSQL over MongoDB for ACID" |
| Workflow optimized | `workflow` | "Pre-commit hooks for linting and tests" |
| Useful command | `command` | "Docker cleanup: docker system prune -af" |

### Sometimes Store

- Completed tasks that taught you something new
- Technology learnings that apply broadly
- File locations that are hard to find

### Never Store

- Temporary debugging notes
- Generic "worked on X" without specifics
- Duplicate of existing memory
- Secrets, credentials, or sensitive data

---

## Memory Quality Guidelines

### Titles

**Good**: Specific, searchable, actionable
```
"Fixed Redis connection timeout by increasing pool size"
"FastAPI dependency injection pattern for database sessions"
"CORS preflight failing - add OPTIONS handler"
```

**Bad**: Vague, generic, unsearchable
```
"Fixed bug"
"Updated code"
"Solved problem"
```

### Content

**Include**:
- What the problem/solution was
- Why it works
- How to apply it
- Key code snippets (if relevant)
- File paths and line numbers (for code fixes)

**Example**:
```markdown
## Problem
Redis connection timeouts under high load (500+ concurrent users).
Error: "ConnectionPool: timed out waiting for connection"

## Root Cause
Default pool_size (10) too small for concurrent requests.

## Solution
```python
redis_pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50,
    socket_timeout=5
)
```

## Result
Zero timeouts under 1000 concurrent users.
```

### Tags

**Best Practices**:
- Use lowercase consistently
- Include technology names (`redis`, `fastapi`, `postgres`)
- Include categories (`performance`, `security`, `auth`)
- Use 3-5 tags per memory

**Example**:
```
tags: ["redis", "performance", "connection-pool", "timeout"]
```

---

## Importance Scoring Guide

| Score | Use For | Examples |
|-------|---------|----------|
| **0.8 - 1.0** | Cross-project patterns, critical fixes | Auth patterns, security fixes, core architecture |
| **0.5 - 0.7** | Project-specific but valuable | API design decisions, database schema choices |
| **0.3 - 0.4** | Minor details, routine work | Small bug fixes, config tweaks |

**Rule of Thumb**: If you'd want to find this in 6 months, score 0.7+.

---

## Relationship Patterns

### Problem-Solution Pairs

Always link solutions to their problems:

```
problem_id = store_memory(type="problem", title="Redis timeout under load", ...)
solution_id = store_memory(type="solution", title="Increase connection pool", ...)
create_relationship(solution_id, problem_id, "SOLVES")
```

### Error-Fix Pairs

```
error_id = store_memory(type="error", title="CORS preflight failing", ...)
fix_id = store_memory(type="fix", title="Add OPTIONS handler", ...)
create_relationship(fix_id, error_id, "SOLVES")
```

### Pattern Evolution

When you improve on an existing pattern:

```
create_relationship(new_pattern_id, old_pattern_id, "IMPROVES")
# or
create_relationship(new_pattern_id, old_pattern_id, "REPLACES")
```

### Dependencies

When one solution requires another:

```
create_relationship(dependent_id, dependency_id, "DEPENDS_ON")
```

---

## Memory Hygiene

### Regular Review (Weekly)

```
> Show my recent memory activity
> What problems are still unresolved?
```

### Consolidation

If you have multiple related memories, consider:
1. Creating a summary memory with higher importance
2. Linking the related memories to it
3. Lowering importance of fragmented memories

### Cleanup

Remove outdated or superseded memories:

```
> Delete that memory about the deprecated API
> Update my old auth pattern - we use JWT now instead of sessions
```

---

## Workflow Integration

### Start of Session

```
> What did I work on yesterday in this project?
> Any unresolved problems I should be aware of?
```

### During Development

```
> I'm getting a timeout error. Have I seen this before?
> What's the pattern for handling database connections here?
```

### After Fixing Issues

```
> Store this fix: [description]
> Link it to the error I stored earlier
```

### End of Session

```
> Extract the key learnings from today's session
```

---

## Integration with Conductor

If using [Conductor](https://github.com/gemini-cli-extensions/conductor) for context-driven development:

### After Setup

```
> Store the key decisions from this project's tech stack
```

### During Implementation

```
> What patterns have I used for this tech stack before?
```

### After Completing a Track

```
> Extract learnings from this track before archiving
```

### When Archiving

```
> Store the important patterns from this completed track
```

**Key Insight**: Conductor archives = forget. MemoryGraph archives = searchable knowledge.

---

## Anti-Patterns to Avoid

### Memory Hoarding

**Problem**: Storing everything dilutes valuable memories.

**Solution**: Be selective. Only store what you'd want to find again.

### Orphan Memories

**Problem**: Unlinked memories lack context.

**Solution**: Always link solutions to problems, fixes to errors.

### Stale Memories

**Problem**: Outdated information misleads future searches.

**Solution**: Update or delete memories when they become obsolete.

### Inconsistent Tagging

**Problem**: `Redis`, `redis`, `REDIS` are three different tags.

**Solution**: Standardize on lowercase, use consistent terminology.

### Missing Context

**Problem**: "Fixed the bug" - which bug? How?

**Solution**: Include what, why, and how in every memory.

---

## Quick Reference Checklist

Before storing a memory:

- [ ] Title is specific and searchable
- [ ] Content explains what, why, and how
- [ ] Tags are lowercase and consistent (3-5 tags)
- [ ] Importance reflects cross-project vs project-specific value
- [ ] Linked to related memories (problems, solutions, patterns)

Before searching:

- [ ] Start with natural language recall
- [ ] Narrow with specific filters if needed
- [ ] Explore relationships for connected knowledge

Regular maintenance:

- [ ] Review recent activity weekly
- [ ] Consolidate fragmented memories
- [ ] Update or delete stale information
- [ ] Check for unresolved problems
