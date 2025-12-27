# Commands Reference

Complete reference for all 9 MCP tools available through the MemoryGraph Gemini CLI extension.

## Overview

MemoryGraph provides tools in three categories:

| Category | Tools |
|----------|-------|
| **Search** | `recall_memories`, `search_memories` |
| **CRUD** | `store_memory`, `get_memory`, `update_memory`, `delete_memory` |
| **Relationships** | `create_relationship`, `get_related_memories`, `get_recent_activity` |

---

## Search Tools

### recall_memories

**Purpose**: Natural language search optimized for fuzzy matching.

**Best for**: Finding memories when you don't know exact terms.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Natural language search query |
| `memory_types` | array | No | Filter by memory types (e.g., `["solution", "fix"]`) |
| `project_path` | string | No | Filter to specific project |
| `limit` | integer | No | Maximum results (default: 20, max: 1000) |
| `offset` | integer | No | Skip first N results for pagination |

**Example Prompts**:
```
> Search my memories for timeout fixes
> What do I know about Redis connection issues?
> Recall any patterns for handling CORS in Express
```

**Example Tool Call**:
```
recall_memories(
    query="redis timeout fix",
    memory_types=["solution", "fix"],
    limit=10
)
```

---

### search_memories

**Purpose**: Structured search with precise filters.

**Best for**: Finding memories with specific criteria (tags, importance, exact terms).

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | No | Text to search in content |
| `terms` | array | No | Multiple search terms for complex queries |
| `memory_types` | array | No | Filter by types |
| `tags` | array | No | Filter by tags |
| `min_importance` | number | No | Minimum importance score (0.0-1.0) |
| `project_path` | string | No | Filter to specific project |
| `search_tolerance` | string | No | `"strict"`, `"normal"` (default), or `"fuzzy"` |
| `match_mode` | string | No | `"any"` (OR) or `"all"` (AND) |
| `limit` | integer | No | Maximum results (default: 50) |
| `offset` | integer | No | Skip first N results |

**Example Prompts**:
```
> Find all high-importance Redis solutions
> Search for memories tagged with "authentication" and "fastapi"
> Find exact matches for "connection pool" in my solutions
```

**Example Tool Call**:
```
search_memories(
    query="connection pool",
    memory_types=["solution"],
    tags=["redis"],
    min_importance=0.7,
    search_tolerance="strict"
)
```

---

## CRUD Tools

### store_memory

**Purpose**: Create a new memory with metadata.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | string | Yes | Memory type (see Memory Types below) |
| `title` | string | Yes | Short, descriptive title |
| `content` | string | Yes | Detailed content |
| `tags` | array | No | Categorization tags |
| `importance` | number | No | Importance score (0.0-1.0) |
| `summary` | string | No | Brief summary |
| `context` | object | No | Additional context metadata |

**Memory Types**:
| Type | Use For |
|------|---------|
| `problem` | Bugs, issues, blockers |
| `solution` | Working fixes and approaches |
| `error` | Specific error messages and stack traces |
| `fix` | Code changes that resolved errors |
| `code_pattern` | Reusable patterns and idioms |
| `technology` | Tech stack knowledge, library usage |
| `task` | Completed work worth remembering |
| `workflow` | Process patterns, CI/CD configs |
| `project` | Project-specific context and decisions |
| `command` | Useful CLI commands and scripts |
| `file_context` | Important file locations and purposes |
| `general` | Anything else worth remembering |

**Example Prompts**:
```
> Store this solution: Fixed Redis timeout by increasing connection pool size to 50
> Remember this pattern: Use dependency injection for database connections in FastAPI
> Save this error and its fix for future reference
```

**Example Tool Call**:
```
store_memory(
    type="solution",
    title="Redis connection pool tuning for high concurrency",
    content="Set pool_size=50 and max_overflow=10. This handles 500+ concurrent connections without timeout errors.",
    tags=["redis", "performance", "connection-pool"],
    importance=0.8
)
```

**Returns**: `memory_id` - Use this to create relationships or update later.

---

### get_memory

**Purpose**: Retrieve a specific memory by ID.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `memory_id` | string | Yes | ID of the memory |
| `include_relationships` | boolean | No | Include connected memories (default: true) |

**Example Tool Call**:
```
get_memory(
    memory_id="abc-123-def",
    include_relationships=true
)
```

---

### update_memory

**Purpose**: Modify an existing memory.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `memory_id` | string | Yes | ID of the memory to update |
| `title` | string | No | New title |
| `content` | string | No | New content |
| `summary` | string | No | New summary |
| `tags` | array | No | New tags (replaces existing) |
| `importance` | number | No | New importance score |

**Example Prompts**:
```
> Update that Redis solution to mention it also works for PostgreSQL connections
> Increase the importance of my authentication pattern memory
> Add the "production" tag to that deployment memory
```

**Example Tool Call**:
```
update_memory(
    memory_id="abc-123-def",
    content="Updated content with new findings...",
    importance=0.9
)
```

---

### delete_memory

**Purpose**: Remove a memory and all its relationships.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `memory_id` | string | Yes | ID of the memory to delete |

**Example Prompts**:
```
> Delete that outdated memory about the old API
> Remove the memory about the deprecated library
```

**Example Tool Call**:
```
delete_memory(memory_id="abc-123-def")
```

---

## Relationship Tools

### create_relationship

**Purpose**: Link two memories together with a typed relationship.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from_memory_id` | string | Yes | Source memory ID |
| `to_memory_id` | string | Yes | Target memory ID |
| `relationship_type` | string | Yes | Type of relationship (see below) |
| `strength` | number | No | Strength of relationship (0.0-1.0) |
| `confidence` | number | No | Confidence in relationship (0.0-1.0) |
| `context` | string | No | Description of the relationship |

**Relationship Types**:

| Category | Types |
|----------|-------|
| **Causal** | `CAUSES`, `TRIGGERS`, `LEADS_TO`, `PREVENTS`, `BREAKS` |
| **Solution** | `SOLVES`, `ADDRESSES`, `ALTERNATIVE_TO`, `IMPROVES`, `REPLACES` |
| **Context** | `OCCURS_IN`, `APPLIES_TO`, `WORKS_WITH`, `REQUIRES`, `USED_IN` |
| **Learning** | `BUILDS_ON`, `CONTRADICTS`, `CONFIRMS`, `GENERALIZES`, `SPECIALIZES` |
| **Similarity** | `SIMILAR_TO`, `VARIANT_OF`, `RELATED_TO`, `ANALOGY_TO`, `OPPOSITE_OF` |
| **Workflow** | `FOLLOWS`, `DEPENDS_ON`, `ENABLES`, `BLOCKS`, `PARALLEL_TO` |
| **Quality** | `EFFECTIVE_FOR`, `INEFFECTIVE_FOR`, `PREFERRED_OVER`, `DEPRECATED_BY`, `VALIDATED_BY` |

**Common Patterns**:

```
# Solution solves a problem
create_relationship(solution_id, problem_id, "SOLVES")

# Fix resolves an error
create_relationship(fix_id, error_id, "SOLVES")

# Pattern A builds on pattern B
create_relationship(pattern_a_id, pattern_b_id, "BUILDS_ON")

# New approach replaces old
create_relationship(new_id, old_id, "REPLACES")
```

**Example Prompts**:
```
> Link that Redis solution to the timeout problem
> Connect my new authentication pattern to the old one as a replacement
> Mark the new fix as an alternative to the previous solution
```

---

### get_related_memories

**Purpose**: Find memories connected to a specific memory.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `memory_id` | string | Yes | Starting memory ID |
| `relationship_types` | array | No | Filter by relationship types |
| `max_depth` | integer | No | How many hops to traverse (1-5, default: 1) |

**Example Prompts**:
```
> What solutions are linked to this problem?
> Find all memories related to my authentication pattern
> What does this error lead to?
```

**Example Tool Call**:
```
get_related_memories(
    memory_id="error-123",
    relationship_types=["SOLVES"],
    max_depth=2
)
```

---

### get_recent_activity

**Purpose**: Summary of recent memory activity for session context.

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `days` | integer | No | Days to look back (default: 7, max: 365) |
| `project` | string | No | Filter by project path |

**Returns**:
- Memory counts by type
- Recent memories (up to 20)
- Unresolved problems

**Example Prompts**:
```
> What have I stored recently?
> Show my memory activity from the last month
> What problems are still unresolved in this project?
```

**Example Tool Call**:
```
get_recent_activity(days=7)
```

---

## Usage Tips

### Natural Conversation

You don't need to specify tool names. Just describe what you want:

```
> Remember this solution for next time
> What patterns do I have for API rate limiting?
> Connect these two memories
```

Gemini will select the appropriate tool automatically.

### Batch Operations

For efficiency, you can request multiple operations:

```
> Store this problem, then store the solution, then link them together
```

### Search Strategy

1. **Start broad**: Use `recall_memories` with natural language
2. **Narrow down**: Use `search_memories` with specific filters
3. **Explore connections**: Use `get_related_memories` to find linked knowledge

### Memory Quality

- **Specific titles**: "Fixed Redis timeout with connection pooling" not "Fixed bug"
- **Detailed content**: Include what, why, and how
- **Consistent tags**: Use lowercase, include technology names
- **Appropriate importance**: 0.8+ for cross-project patterns, 0.5-0.7 for project-specific
