# MemoryGraph for Gemini CLI

**The first persistent memory extension for Gemini CLI.**

MemoryGraph gives your Gemini CLI sessions persistent, graph-based memory. Solutions you find today are searchable tomorrow. Patterns you learn in one project transfer to another.

## Features

- **Persistent memory**: Knowledge survives across sessions
- **Graph-based relationships**: Link problems to solutions, errors to fixes
- **Cross-project learning**: Apply patterns from Project A in Project B
- **Zero infrastructure**: SQLite default, works immediately
- **Cloud sync**: Optional sync via [memorygraph.dev](https://memorygraph.dev)

## Installation

### Prerequisites

Install MemoryGraph MCP server:

```bash
pipx install memorygraphMCP
```

### Install Extension

```bash
gemini extensions install https://github.com/memorygraphdev/memorygraph-gemini --auto-update
```

### Verify Installation

```bash
gemini mcp list
# Should show: memorygraph: connected
```

## Quick Start

Start a Gemini CLI session and try:

```
> Search my memories for authentication patterns
> Remember this: Use bcrypt with cost factor 12 for password hashing
> What solutions have I found for CORS issues?
```

MemoryGraph tools are automatically available. The AI will use them when relevant.

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MEMORY_BACKEND` | No | `sqlite` | Backend: `sqlite`, `neo4j`, `falkordb`, `cloud` |
| `MEMORYGRAPH_API_KEY` | For cloud | - | API key from [memorygraph.dev](https://memorygraph.dev) |
| `MEMORYGRAPH_DATA_DIR` | No | `~/.memorygraph` | Data directory for SQLite |

### Using Cloud Backend

1. Sign up at [memorygraph.dev](https://memorygraph.dev)
2. Get your API key from the dashboard
3. Set environment variables:

```bash
export MEMORY_BACKEND=cloud
export MEMORYGRAPH_API_KEY=your_api_key
```

## Usage Examples

### Recall Before Starting Work

```
> I'm about to implement rate limiting. What do I know about this?
```

The AI will search your memories for rate limiting patterns, past solutions, and relevant context.

### Store After Solving Problems

```
> Store this solution: Fixed the N+1 query problem by using selectinload()
> for the user.posts relationship. Reduced page load from 2s to 50ms.
> Tag it with sqlalchemy, performance, n-plus-one.
```

### Link Problems to Solutions

```
> Link that solution to the performance problem I stored yesterday
```

### Cross-Project Patterns

```
> What authentication patterns have I used in other FastAPI projects?
```

## Integration with Conductor

MemoryGraph complements [Conductor](https://github.com/gemini-cli-extensions/conductor) for context-driven development:

| Conductor Does | MemoryGraph Adds |
|----------------|------------------|
| Project-local specs and plans | Cross-project memory |
| Session-bound context | Persistent knowledge |
| Archive old tracks | Learn from archives |
| Current task tracking | Historical patterns |

After completing a Conductor track:

```
> Extract the key learnings from this track and store them in memory
```

## Available Tools

The extension provides these MCP tools:

| Tool | Description |
|------|-------------|
| `recall_memories` | Natural language search |
| `search_memories` | Structured search with filters |
| `store_memory` | Create a new memory |
| `get_memory` | Retrieve a specific memory |
| `update_memory` | Update an existing memory |
| `delete_memory` | Delete a memory |
| `create_relationship` | Link two memories |
| `get_related_memories` | Find connected memories |
| `get_recent_activity` | See recent memory activity |

## Memory Types

| Type | Use For |
|------|---------|
| `problem` | Bugs, issues, blockers |
| `solution` | Working fixes and approaches |
| `error` | Error messages and stack traces |
| `fix` | Code changes that resolved errors |
| `code_pattern` | Reusable patterns and idioms |
| `technology` | Tech stack knowledge |
| `task` | Completed work |
| `workflow` | Process patterns |
| `project` | Project context and decisions |
| `command` | Useful CLI commands |
| `file_context` | Important file locations |
| `general` | Anything else |

## Relationship Types

Connect memories for richer context:

- **Causal**: `CAUSES`, `TRIGGERS`, `LEADS_TO`, `PREVENTS`, `BREAKS`
- **Solution**: `SOLVES`, `ADDRESSES`, `ALTERNATIVE_TO`, `IMPROVES`, `REPLACES`
- **Context**: `OCCURS_IN`, `APPLIES_TO`, `WORKS_WITH`, `REQUIRES`
- **Learning**: `BUILDS_ON`, `CONTRADICTS`, `CONFIRMS`, `GENERALIZES`
- **Workflow**: `FOLLOWS`, `DEPENDS_ON`, `ENABLES`, `BLOCKS`
- **Quality**: `EFFECTIVE_FOR`, `INEFFECTIVE_FOR`, `PREFERRED_OVER`

## Troubleshooting

### Extension not loading

```bash
# Check if memorygraph CLI is available
which memorygraph

# If not found, install it
pipx install memorygraphMCP
```

### MCP server not connecting

```bash
# Test memorygraph directly
memorygraph --health

# Check extension status
gemini extensions list
```

### Memories not persisting

Check your data directory:

```bash
ls ~/.memorygraph/
# Should contain: memorygraph.db (for SQLite backend)
```

## Links

- [MemoryGraph Documentation](https://memorygraph.dev/docs)
- [GitHub Repository](https://github.com/memorygraphdev/memorygraph)
- [Gemini CLI Extensions Gallery](https://geminicli.com/extensions/)
- [Report Issues](https://github.com/memorygraphdev/memorygraph-gemini/issues)

## License

Apache 2.0
