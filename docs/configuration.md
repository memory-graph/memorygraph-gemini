# Configuration Guide

Configure MemoryGraph for Gemini CLI with different backends, data locations, and cloud sync options.

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MEMORY_BACKEND` | No | `sqlite` | Backend type: `sqlite`, `neo4j`, `falkordb`, `cloud` |
| `MEMORYGRAPH_API_KEY` | For cloud | - | API key from [memorygraph.dev](https://memorygraph.dev) |
| `MEMORYGRAPH_DATA_DIR` | No | `~/.memorygraph` | Data directory for SQLite backend |

## Backend Options

### SQLite (Default)

Zero-configuration local storage. Works immediately.

```bash
# No configuration needed - this is the default
# Data stored in ~/.memorygraph/memorygraph.db
```

**Pros**:
- No setup required
- Works offline
- Fast for individual use
- No external dependencies

**Cons**:
- Not synced across machines
- No team sharing

---

### Cloud Backend

Sync memories across devices and share with your team via [memorygraph.dev](https://memorygraph.dev).

#### Setup

1. **Create Account**: Sign up at [memorygraph.dev](https://memorygraph.dev)

2. **Get API Key**: From your dashboard, generate an API key

3. **Configure Environment**:

```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export MEMORY_BACKEND=cloud
export MEMORYGRAPH_API_KEY=your_api_key_here
```

4. **Restart Shell or Source Profile**:

```bash
source ~/.zshrc  # or ~/.bashrc
```

5. **Verify Connection**:

```bash
# In a new Gemini CLI session
gemini mcp list
# Should show: memorygraph: connected
```

**Pros**:
- Synced across all devices
- Backup and recovery
- Team sharing (coming soon)
- Web dashboard for browsing memories

**Cons**:
- Requires internet connection for sync
- Subscription required for full features

---

### Neo4j Backend

For users with existing Neo4j infrastructure.

```bash
export MEMORY_BACKEND=neo4j
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=your_password
```

**Requirements**:
- Neo4j 4.4+ or 5.x
- APOC plugin installed

---

### FalkorDB Backend

High-performance graph database option.

```bash
export MEMORY_BACKEND=falkordb
export FALKORDB_HOST=localhost
export FALKORDB_PORT=6379
```

**Requirements**:
- FalkorDB server running
- Redis protocol compatible

---

## Data Directory Configuration

### Custom Location

Override the default data directory:

```bash
export MEMORYGRAPH_DATA_DIR=/path/to/custom/directory
```

**Use cases**:
- Store data on a specific drive
- Use encrypted storage
- Separate data for different contexts

### Multiple Configurations

For different contexts (work vs personal):

```bash
# Work profile
alias gemini-work='MEMORYGRAPH_DATA_DIR=~/.memorygraph-work gemini'

# Personal profile
alias gemini-personal='MEMORYGRAPH_DATA_DIR=~/.memorygraph-personal gemini'
```

---

## Extension Configuration

The extension reads configuration from `gemini-extension.json`:

```json
{
  "name": "memorygraph",
  "version": "1.0.0",
  "contextFileName": "GEMINI.md",
  "mcpServers": {
    "memorygraph": {
      "command": "memorygraph",
      "args": [],
      "env": {
        "MEMORY_BACKEND": "${MEMORY_BACKEND:-sqlite}",
        "MEMORYGRAPH_API_KEY": "${MEMORYGRAPH_API_KEY}",
        "MEMORYGRAPH_DATA_DIR": "${MEMORYGRAPH_DATA_DIR}"
      }
    }
  }
}
```

Environment variable substitution is automatic. Variables use the format `${VAR:-default}`.

---

## File Locations

| Path | Purpose |
|------|---------|
| `~/.gemini/extensions/memorygraph/` | Extension installation |
| `~/.memorygraph/` | Default data directory |
| `~/.memorygraph/memorygraph.db` | SQLite database file |
| `~/.gemini/settings.json` | MCP server config (if manually configured) |

---

## Project-Specific Configuration

### Per-Project Context

Create `.gemini/GEMINI.md` in your project root to add project-specific context:

```markdown
# Project: My API

This is a FastAPI backend with PostgreSQL.

## Key Files
- `app/main.py` - Entry point
- `app/models/` - SQLAlchemy models

## Important Decisions
- Using async SQLAlchemy for all database operations
- JWT authentication with refresh tokens
```

This context is automatically included in Gemini sessions for that project.

### Per-Project Memory Filtering

When searching, you can filter to project-specific memories:

```
> Search for authentication patterns in this project only
```

The AI will use `project_path` filtering to scope results.

---

## Cloud Configuration Details

### API Key Security

**DO NOT** commit your API key to version control.

Recommended approaches:

1. **Shell Profile** (most common):
   ```bash
   # ~/.zshrc or ~/.bashrc
   export MEMORYGRAPH_API_KEY=your_key_here
   ```

2. **direnv** (per-project):
   ```bash
   # .envrc (add to .gitignore)
   export MEMORYGRAPH_API_KEY=your_key_here
   ```

3. **1Password / Secrets Manager**:
   ```bash
   export MEMORYGRAPH_API_KEY=$(op read "op://Development/MemoryGraph/api-key")
   ```

### Sync Behavior

- **Immediate**: Memories are synced on store/update/delete
- **Eventual**: Search includes recently synced data
- **Offline**: Falls back to local cache when disconnected

### Rate Limits

| Plan | Memories/Month | API Calls/Min |
|------|----------------|---------------|
| Free | 1,000 | 60 |
| Pro | 50,000 | 300 |
| Team | Unlimited | 1,000 |

---

## Troubleshooting Configuration

### Backend Not Connecting

```bash
# Check which backend is configured
echo $MEMORY_BACKEND

# Test memorygraph directly
memorygraph --health
```

### Cloud Sync Issues

```bash
# Verify API key is set
echo $MEMORYGRAPH_API_KEY | head -c 10

# Test cloud connection
memorygraph --health --backend cloud
```

### Wrong Data Directory

```bash
# Check current data directory
echo $MEMORYGRAPH_DATA_DIR

# List contents
ls -la ${MEMORYGRAPH_DATA_DIR:-~/.memorygraph}
```

### Environment Variables Not Loading

Ensure your shell profile is sourced:

```bash
# For zsh
source ~/.zshrc

# For bash
source ~/.bashrc

# Verify
env | grep MEMORY
```

---

## Migration

### SQLite to Cloud

```bash
# Export from SQLite
memorygraph export --output memories.json

# Configure cloud backend
export MEMORY_BACKEND=cloud
export MEMORYGRAPH_API_KEY=your_key

# Import to cloud
memorygraph import --input memories.json
```

### Between Machines

```bash
# On source machine
cp ~/.memorygraph/memorygraph.db /path/to/backup/

# On target machine
mkdir -p ~/.memorygraph
cp /path/to/backup/memorygraph.db ~/.memorygraph/
```

---

## Advanced Configuration

### Custom MCP Server

For advanced users running a custom MemoryGraph server:

```bash
export MEMORYGRAPH_URL=http://localhost:8000
```

### Debug Logging

Enable verbose logging for troubleshooting:

```bash
export MEMORYGRAPH_LOG_LEVEL=debug
```

### Connection Timeout

Adjust timeout for slow connections:

```bash
export MEMORYGRAPH_TIMEOUT=30  # seconds
```
