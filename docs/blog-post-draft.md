# Announcing MemoryGraph for Gemini CLI: The First Persistent Memory Extension

**The first memory extension for Google's AI coding tool is here - and it changes everything about how AI learns from your work.**

---

## TL;DR

MemoryGraph brings persistent, graph-based memory to Gemini CLI. It's the first MCP-based memory extension for Google's AI coding tool, and it solves a critical problem: **AI that forgets everything when the session ends**.

- 🎉 **First** persistent memory extension for Gemini CLI
- 🧠 Graph-based memory that connects problems to solutions
- 🚀 Cross-project intelligence - learn once, apply everywhere
- 🤝 Perfect complement to Conductor's context-driven development
- 💾 Works locally (SQLite) or syncs via cloud (memorygraph.dev)

**[Install now](https://github.com/memorygraphdev/memorygraph-gemini)** | **[Documentation](https://memorygraph.dev/docs/quickstart/gemini-cli)**

---

## The Problem: AI Memory Loss

Gemini CLI is powerful. Conductor makes it context-aware. But there's a missing piece: **persistent memory**.

When you:
- Solve a tricky authentication bug
- Figure out the right FastAPI middleware order
- Discover why your async code was deadlocking
- Optimize a slow database query

...that knowledge disappears when the session ends. When Conductor archives an old track, the patterns you discovered go with it.

**You solved that problem. But did your AI learn from it?**

---

## The Solution: MemoryGraph

MemoryGraph is the first persistent memory extension for Gemini CLI. It gives your AI long-term memory that:

### 1. **Persists Across Sessions**

```bash
# Today: solve a problem
> Store this solution: Fixed N+1 query using selectinload().
> Reduced page load from 2s to 50ms. Tag: sqlalchemy, performance

# Next week: similar problem
> I have a slow query in SQLAlchemy. What have I learned about this?

# MemoryGraph recalls your solution immediately
```

Your knowledge compounds over time instead of resetting every session.

### 2. **Connects the Dots with Graph Relationships**

Problems → Solutions. Errors → Fixes. Patterns → Implementations.

```bash
# Store an error
> Store this error: "asyncio.CancelledError in background tasks"

# Store the fix
> Store this fix: Use asyncio.shield() to protect critical cleanup code

# Link them
> Link that fix to the error I just stored
```

MemoryGraph builds a graph of your knowledge, making it easy to navigate from problem to solution.

### 3. **Enables Cross-Project Learning**

The best developers recognize patterns across projects. Now your AI can too.

```bash
# In Project A: learn a FastAPI authentication pattern
> Store: JWT refresh tokens with httpOnly cookies. Tag: fastapi, auth, jwt

# In Project B: recall that pattern
> What authentication patterns have I used in other FastAPI projects?

# MemoryGraph finds the pattern from Project A
```

**Knowledge transfers.** Learn once, apply everywhere.

### 4. **Complements Conductor Perfectly**

Conductor excels at **project-local context** and **current task tracking**. MemoryGraph adds **cross-project memory** and **historical patterns**.

| Conductor Does | MemoryGraph Adds |
|----------------|------------------|
| Project specs and plans | Cross-project patterns |
| Session-bound context | Persistent knowledge |
| Archive old tracks | Learn from archives |
| Current task focus | Historical context |

**Better together.** After completing a Conductor track:

```bash
> Extract the key learnings from this track and store them in MemoryGraph
```

Now your insights from archived tracks become searchable, reusable knowledge.

---

## How It Works

### Installation (2 minutes)

```bash
# Install the MCP server
pipx install memorygraphMCP

# Install the Gemini CLI extension
gemini extensions install https://github.com/memorygraphdev/memorygraph-gemini --auto-update

# Verify it's working
gemini mcp list
# Should show: memorygraph: connected
```

### Natural Language Interface

MemoryGraph tools are automatically available in Gemini CLI. Just use natural language:

```bash
# Recall memories
> What have I learned about rate limiting?
> Show me my Redis patterns
> What solutions did I store for CORS issues?

# Store memories
> Remember this: Use bcrypt with cost factor 12 for passwords
> Store this pattern: FastAPI depends on Request for accessing headers

# Link memories
> Link this solution to the authentication problem I stored yesterday
```

The AI uses MemoryGraph tools intelligently - no manual tool invocation needed.

### Memory Types

MemoryGraph supports 12 memory types:

- `solution` - Working fixes and approaches
- `problem` - Bugs and blockers
- `error` - Error messages and stack traces
- `fix` - Code changes that resolved errors
- `code_pattern` - Reusable patterns
- `technology` - Tech stack knowledge
- `workflow` - Process patterns
- And more...

### Flexible Backends

**Local-first** with SQLite (default):
```bash
# Zero config - just works
```

**Cloud sync** for multi-machine workflows:
```bash
export MEMORY_BACKEND=cloud
export MEMORYGRAPH_API_KEY=your_key  # from memorygraph.dev
```

**Enterprise** with Neo4j or FalkorDB:
```bash
export MEMORY_BACKEND=neo4j
export NEO4J_URI=bolt://localhost:7687
```

---

## Real-World Workflows

### Archive to Learn

You've completed a Conductor track. Don't let that knowledge disappear:

```bash
# Extract learnings
> Extract key patterns from this Conductor track and store in MemoryGraph

# Tag appropriately
> Tag those memories with: project-alpha, fastapi, authentication, jwt
```

Now those patterns are searchable in future projects.

### Debug with Memory

Hit an error? Check if you've solved it before:

```bash
> I'm getting "RuntimeError: Event loop is closed". Have I seen this before?

# MemoryGraph recalls your previous fix
> Yes! You solved this by using asyncio.run() instead of loop.run_until_complete()
```

### Pattern Library

Build a personal library of proven patterns:

```bash
# Store patterns as you discover them
> Store pattern: FastAPI background tasks should use Depends() for DB sessions
> Store pattern: Redis pipeline for bulk operations reduces RTT by 90%

# Recall when needed
> Show me my FastAPI background task patterns
> What Redis performance patterns do I know?
```

---

## Why First-Mover Matters

MemoryGraph is the **first persistent memory extension for Gemini CLI**. This positioning matters because:

1. **No competition yet** - We're defining the category
2. **Conductor complement story** - Natural fit for existing Gemini CLI + Conductor workflows
3. **MCP advantage** - Works with any MCP-compatible AI tool (Claude Code, Cursor, etc.)
4. **Platform-agnostic** - The memory layer for AI coding tools

As AI coding tools evolve, **persistent memory becomes table stakes**. MemoryGraph is first to market.

---

## The Memory Layer for AI Coding

MemoryGraph isn't just for Gemini CLI. It's the **memory layer for any AI coding tool**:

- ✅ **Gemini CLI** + Conductor (this release)
- ✅ **Claude Code CLI** (already supported)
- ✅ **Cursor, Windsurf, Continue.dev** (via MCP)
- ✅ **Any MCP-compatible tool** (future-proof)

**One memory graph. Multiple AI frontends.**

---

## What's Next

### Immediate Roadmap
- Visual memory browser (GUI for exploring the graph)
- Memory analytics (insights into knowledge patterns)
- Team memory sharing (collaborative knowledge bases)
- Integration templates (common workflow examples)

### Join the Community
- **GitHub**: [memorygraphdev/memorygraph-gemini](https://github.com/memorygraphdev/memorygraph-gemini)
- **Docs**: [memorygraph.dev/docs](https://memorygraph.dev/docs)
- **Issues**: Report bugs, request features
- **Discussions**: Share your workflows

---

## Get Started Today

```bash
# Install
pipx install memorygraphMCP
gemini extensions install https://github.com/memorygraphdev/memorygraph-gemini --auto-update

# Start using
gemini
> Tell me about my stored memories
```

**It's that simple.**

Your AI now has a memory that:
- Persists across sessions
- Connects problems to solutions
- Transfers knowledge between projects
- Complements Conductor's context-driven development

**Try it. Build your knowledge graph. Never solve the same problem twice.**

---

## Technical Details

For those interested in the implementation:

### Architecture
- **MCP Protocol**: Model Context Protocol for tool registration
- **Graph Backend**: SQLite (default), Neo4j, FalkorDB, or cloud
- **Relationship Types**: 35+ semantic relationships (SOLVES, CAUSES, FIXES, etc.)
- **Search**: Fuzzy matching with stemming for natural language queries
- **Filters**: By type, tags, importance, project, date range

### Extension Manifest
```json
{
  "name": "memorygraph",
  "version": "1.0.0",
  "description": "Persistent graph-based memory for Gemini CLI",
  "mcp_servers": {
    "memorygraph": {
      "command": "memorygraph",
      "args": ["--mcp"]
    }
  }
}
```

### Memory Schema
```typescript
interface Memory {
  id: string;
  type: MemoryType;
  title: string;
  content: string;
  summary?: string;
  tags: string[];
  importance: number;  // 0.0 - 1.0
  project_path?: string;
  created_at: Date;
  updated_at: Date;
}

interface Relationship {
  from_memory_id: string;
  to_memory_id: string;
  type: RelationshipType;
  strength?: number;
  confidence?: number;
  context?: string;
}
```

---

## Conclusion

**MemoryGraph is the first persistent memory extension for Gemini CLI** - and it fundamentally changes how AI learns from your work.

- **No more forgetting** - Knowledge persists across sessions
- **Connected insights** - Graph relationships link problems to solutions
- **Cross-project transfer** - Patterns learned once, applied everywhere
- **Conductor synergy** - Turn archived tracks into searchable knowledge

**Install it. Use it. Watch your AI get smarter over time.**

[Get Started](https://memorygraph.dev/docs/quickstart/gemini-cli) | [GitHub](https://github.com/memorygraphdev/memorygraph-gemini) | [Documentation](https://memorygraph.dev/docs)

---

*MemoryGraph is open source (Apache 2.0) and works with any MCP-compatible AI coding tool.*
