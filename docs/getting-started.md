# Getting Started with MemoryGraph for Gemini CLI

This guide will get you up and running with MemoryGraph in your Gemini CLI environment in under 5 minutes.

## Prerequisites

Before installing the extension, you need the MemoryGraph MCP server:

```bash
# Install MemoryGraph MCP server via pipx
pipx install memorygraphMCP

# Verify installation
memorygraph --version
```

**Requirements:**
- Python 3.10 or higher
- pipx (recommended) or pip
- Gemini CLI installed and configured

## Installation

### Install the Extension

```bash
gemini extensions install https://github.com/memory-graph/memorygraph-gemini --auto-update
```

### Verify Installation

```bash
# Check extension is listed
gemini extensions list

# Verify MCP server connection
gemini mcp list
# Should show: memorygraph: connected
```

## First Use

Start a Gemini CLI session:

```bash
gemini
```

### 1. Check Your Memory (First Time)

```
> Search my memories for any patterns
```

On first run, this will return empty results. That's expected - you haven't stored anything yet!

### 2. Store Your First Memory

After solving a problem or learning something, store it:

```
> Remember this: Use bcrypt with cost factor 12 for password hashing in Node.js applications
```

The AI will use the `store_memory` tool to save this knowledge.

### 3. Recall Later

In a future session:

```
> What do I know about password hashing?
```

MemoryGraph returns your stored knowledge, ready to apply.

## How It Works

MemoryGraph provides 9 MCP tools that Gemini CLI can use automatically:

| Tool | What It Does |
|------|--------------|
| `recall_memories` | Natural language search |
| `search_memories` | Structured search with filters |
| `store_memory` | Create a new memory |
| `get_memory` | Retrieve a specific memory by ID |
| `update_memory` | Modify an existing memory |
| `delete_memory` | Remove a memory |
| `create_relationship` | Link two memories together |
| `get_related_memories` | Find connected memories |
| `get_recent_activity` | See recent memory activity |

You don't need to call these directly. Gemini will use them when appropriate based on your requests.

## Quick Examples

### Before Starting Work

```
> I'm about to implement OAuth2 authentication. What do I know about this?
```

### After Fixing a Bug

```
> Store this solution: Fixed the N+1 query problem in the users endpoint by using
> selectinload() for the user.posts relationship. Reduced page load from 2s to 50ms.
> Tag it with sqlalchemy, performance, and n-plus-one.
```

### Finding Cross-Project Patterns

```
> What authentication patterns have I used in my FastAPI projects?
```

### Linking Solutions to Problems

```
> Link my Redis connection pool solution to the timeout problem I stored yesterday
```

## Next Steps

- **[Commands Reference](./commands-reference.md)** - Deep dive into all 9 MCP tools
- **[Configuration](./configuration.md)** - Set up cloud sync and customize settings
- **[Best Practices](./best-practices.md)** - Memory hygiene patterns for maximum value

## Troubleshooting

### "memorygraph" command not found

```bash
# Reinstall with pipx
pipx install memorygraphMCP --force

# Verify it's in your PATH
which memorygraph
```

### Extension not loading

```bash
# Check extension status
gemini extensions list

# Reinstall if needed
gemini extensions uninstall memorygraph
gemini extensions install https://github.com/memory-graph/memorygraph-gemini --auto-update
```

### MCP server not connecting

```bash
# Test memorygraph directly
memorygraph --health

# Check for errors in extension
gemini mcp list --verbose
```

### Memories not persisting

Check your data directory:

```bash
ls ~/.memorygraph/
# Should contain: memorygraph.db (for SQLite backend)
```

If the directory doesn't exist, it will be created on first memory store.

## Need Help?

- [Full Documentation](https://memorygraph.dev/docs)
- [GitHub Issues](https://github.com/memory-graph/memorygraph-gemini/issues)
- [MemoryGraph Community](https://memorygraph.dev/community)
