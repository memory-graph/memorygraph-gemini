# MemoryGraph for Gemini CLI

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Extension-4285F4.svg)](https://geminicli.com/extensions/)

**🎉 The first persistent memory extension for Gemini CLI.**

MemoryGraph brings graph-based, persistent memory to Google's AI coding tool. Solutions you find today are searchable tomorrow. Patterns you learn in one project transfer to another. Knowledge that persists when Conductor archives.

**[Get Started](https://memorygraph.dev/docs/quickstart/gemini-cli)** | **[Documentation](https://memorygraph.dev/docs)** | **[Report Issue](https://github.com/memory-graph/memorygraph-gemini/issues)**

## Why MemoryGraph?

### 🚀 First-Mover Advantage
MemoryGraph is the **first MCP-based persistent memory extension for Gemini CLI**. While Conductor provides excellent project-local context, MemoryGraph adds the missing layer: **cross-project, long-term intelligence**.

### ✨ Key Features

- **Persistent memory**: Knowledge survives across sessions and Conductor archives
- **Graph-based relationships**: Link problems to solutions, errors to fixes, patterns to implementations
- **Cross-project learning**: Apply patterns from Project A in Project B - true knowledge transfer
- **Zero infrastructure**: SQLite default, works immediately with no setup
- **Cloud sync**: Optional sync via [memorygraph.dev](https://memorygraph.dev) for multi-machine workflows
- **Perfect Conductor complement**: Turn archived tracks into searchable, reusable knowledge

## Installation

### Prerequisites

Install MemoryGraph MCP server:

```bash
pipx install memorygraphMCP
```

### Install Extension

```bash
gemini extensions install https://github.com/memory-graph/memorygraph-gemini --auto-update
```

### Verify Installation

```bash
gemini mcp list
# Should show: memorygraph: connected
```

## Quick Start

### 🎬 See It In Action

Start a Gemini CLI session and try natural language memory interactions:

```bash
# Recall before starting work
> I'm implementing OAuth2. What patterns have I used before?

# Store solutions as you work
> Store this solution: Fixed rate limiting by using Redis with sliding window.
> Reduced CPU from 80% to 12%. Tag: redis, performance, rate-limiting

# Link related memories
> Link that solution to the performance problem I stored yesterday

# Cross-project learning
> What FastAPI authentication patterns have I used in other projects?

# Archive to learn (after Conductor track)
> Extract key learnings from this track and store them for future projects
```

**MemoryGraph tools are automatically available** - the AI uses them intelligently when relevant to your conversation.

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

### Conductor Integration Commands

MemoryGraph provides specialized commands for Conductor workflows:

#### `/memory:learn-track` - Extract Learnings from Completed Tracks

After completing a Conductor track, automatically extract and store learnings:

```bash
gemini> /memory:learn-track feature-user-auth
```

**What it extracts:**
- **From spec.md**: Technical decisions, architecture choices, scope boundaries
- **From plan.md**: Blockers + solutions, workflow adjustments, performance fixes
- **From code**: Reusable patterns, integration approaches, testing strategies

**Memory types created:**
- Problems → Solutions (with SOLVES relationship)
- Errors → Fixes (with FIXES relationship)
- Code patterns → Technology integrations
- Workflow improvements → Process optimizations

**Example usage:**
```
> /memory:learn-track checkout-optimization

# Returns:
Learning Extraction Report: checkout-optimization

Statistics:
- Problems captured: 3 (with 3 solutions)
- Code patterns identified: 5
- Technologies documented: 2
- Workflows improved: 1
- Total memories created: 14
- Relationships established: 8

High-Value Learnings (Importance ≥ 0.8):
1. Redis sliding window rate limiting pattern - Reduced API abuse 95%
2. Optimistic locking for inventory - Prevented overselling
3. Stripe webhook idempotency pattern - Ensured payment integrity
```

#### `/memory:conductor-context` - Inject Historical Context

Run **after** `/conductor:setup` to enhance your project with historical intelligence:

```bash
gemini> /memory:conductor-context
```

**What it does:**
1. Reads your Conductor context files (product.md, tech-stack.md, workflow.md)
2. Searches MemoryGraph for relevant patterns, pitfalls, and similar projects
3. Injects "Historical Insights" sections into your Conductor files

**Enhancements added:**
- **tech-stack.md**: Proven patterns, known pitfalls, integration recommendations
- **product.md**: Similar past projects, domain-specific learnings
- **workflow.md**: Process optimizations from historical data

**Example output:**
```
Historical Context Injection Report

Search Results:
- Technologies matched: Next.js, TypeScript, PostgreSQL, Redis
- Memories retrieved: 47 total (23 high relevance, 24 medium)
- Projects analyzed: 3 similar projects found

Injected Content:
✅ Enhanced tech-stack.md with 8 patterns and 5 pitfalls
✅ Enhanced product.md with 3 related project insights
✅ Enhanced workflow.md with 4 process optimizations

Key Insights Added:
1. Pattern: JWT middleware refresh with expiry buffer (prevents infinite loops)
2. Pitfall: PostgreSQL connection pool exhaustion under load
3. Workflow: Parallel test execution reduced CI time by 60%

Cross-Project Intelligence:
- Found 85% technology overlap with "ecommerce-platform" project
- Identified 8 reusable patterns from past work
- Surfaced 5 common pitfalls to avoid
```

#### `/memory:auto-learn` - Automatic Learning from Archives

Automatically extract learnings from recently archived Conductor tracks:

```bash
gemini> /memory:auto-learn
```

**What it does:**
1. Scans `conductor/archive/` for recently archived tracks
2. Identifies tracks not yet processed for learning extraction
3. Automatically extracts and stores learnings from each track
4. Marks processed tracks to prevent duplication

**Setup options:**
- **Manual trigger**: Run after archiving a track
- **Script automation**: Use provided scripts for post-archive hooks
- **File watcher**: Monitor archive directory for automatic processing

**Example output:**
```
Auto-Learning Summary

Tracks Processed:
- feature-user-auth: 14 memories created, 8 relationships
- bugfix-checkout-flow: 6 memories created, 3 relationships

Total Knowledge Captured:
- Problems: 4 (with 4 solutions)
- Code Patterns: 7
- Technologies: 2
- Workflows: 1
- Total memories: 20
- Total relationships: 11

High-Value Learnings (Importance ≥ 0.8):
1. JWT refresh middleware pattern - Prevents infinite loops
2. Stripe idempotency key handling - Ensures payment integrity
3. PostgreSQL connection pooling - Prevents exhaustion under load
```

#### `/memory:restore-context` - Resume Work Seamlessly

Restore context when resuming work on a track from a previous session:

```bash
gemini> /memory:restore-context feature-user-auth
```

**What it does:**
1. Searches MemoryGraph for context from previous sessions
2. Analyzes current track state (completed tasks, blockers, etc.)
3. Presents comprehensive "Resuming Track" summary
4. Detects context drift and cross-track dependencies

**Example output:**
```
🔄 Resuming Track: feature-user-auth

Session Gap Analysis:
- Last activity: 3 days ago
- Current state: 65% complete

What You've Completed:
✅ JWT middleware implementation
✅ Token generation logic
✅ Basic auth routes

Where You Left Off:
🔄 Current task: Add token refresh logic
⏳ Next up: Implement logout endpoint

Blockers & Challenges:
✅ JWT infinite loop → Resolved by middleware pattern

Key Decisions Made:
- Using middleware for token validation
- 5-minute expiry buffer to prevent race conditions

Files Modified:
- src/auth/middleware.ts
- src/utils/jwt.ts

Related Memories: 8 stored
Ready to resume work!
```

#### `/memory:detect-conflicts` - Prevent File Conflicts

Detect when files you're about to modify were recently changed by other tracks:

```bash
gemini> /memory:detect-conflicts
```

**What it does:**
1. Identifies files mentioned in current track spec/plan
2. Searches MemoryGraph for recent modifications to those files
3. Analyzes conflict severity (critical, recent, or historical)
4. Provides coordination recommendations

**Example output:**
```
🔍 Conflict Detection Report

Conflicts detected: 1 high, 1 medium

🔴 HIGH SEVERITY
src/auth/middleware.ts
- Modified 6 hours ago in feature-2fa-authentication (active)
- HIGH OVERLAP: Both tracks modifying JWT validation
- URGENT: Coordinate before proceeding

🟡 MEDIUM SEVERITY
src/utils/jwt.ts
- Modified 2 days ago in bugfix-token-expiry (completed)
- SAFE TO PROCEED: No direct conflict
- REVIEW: Read recent changes to understand new expiry logic

Action Plan:
1. 🚨 Coordinate on middleware.ts - HIGH PRIORITY
2. 📖 Review changes in jwt.ts - 10 minutes
```

### Conductor Workflow Best Practices

**1. Setup Phase**
```bash
gemini> /conductor:setup
# ... complete Conductor setup ...
gemini> /memory:conductor-context
# Inject historical intelligence
```

**2. Before Starting a Track**
```bash
gemini> /conductor:newTrack feature-payment-processing
# ... create spec.md ...
gemini> /memory:detect-conflicts
# Check for potential file conflicts
```

**3. Resuming Previous Work**
```bash
gemini> /memory:restore-context feature-user-auth
# Restore context from previous session
gemini> /conductor:implement feature-user-auth
# Continue implementation with full context
```

**4. During Development**
Use natural language to recall patterns:
```
> I'm implementing the checkout flow. What patterns have I used before?
> What are common pitfalls with Stripe webhooks?
```

**5. After Track Completion**
```bash
gemini> /memory:learn-track feature-checkout
# Extract and store all learnings
```

**6. Automatic Archive Learning**
```bash
# After archiving tracks
gemini> /memory:auto-learn
# Automatically extract learnings from all recent archives
```

**7. Long-Term Benefits**
When Conductor archives old tracks, MemoryGraph preserves the knowledge:
```
> What did I learn from that authentication track I archived last month?
```

### Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Gemini CLI Session                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐         ┌─────────────────────┐       │
│  │  Conductor  │◄───────►│    MemoryGraph      │       │
│  │  Extension  │         │    Extension        │       │
│  └─────────────┘         └─────────────────────┘       │
│        │                          │                     │
│        ▼                          ▼                     │
│  conductor/*.md             FalkorDB Graph             │
│  (specs, plans)            (persistent memory)         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Key synergies:**
- Conductor provides structured workflow → MemoryGraph learns from it
- MemoryGraph provides historical context → Conductor uses it for better specs
- Conductor archives old work → MemoryGraph makes it searchable forever

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

## The Memory Layer for AI Coding

MemoryGraph isn't just for Gemini CLI. It's the **memory layer for any AI coding tool**:

- ✅ **Gemini CLI + Conductor** (this extension)
- ✅ **Claude Code CLI** ([already supported](https://memorygraph.dev/docs/quickstart/claude-code))
- ✅ **Cursor, Windsurf, Continue.dev** (via MCP)
- ✅ **Any MCP-compatible tool** (future-proof)

**One memory graph. Multiple AI frontends.**

## Links

- [MemoryGraph Documentation](https://memorygraph.dev/docs)
- [Quickstart Guide for Gemini CLI](https://memorygraph.dev/docs/quickstart/gemini-cli)
- [Main MemoryGraph Repository](https://github.com/memory-graph/memorygraph)
- [Gemini CLI Extensions Gallery](https://geminicli.com/extensions/)
- [Report Issues](https://github.com/memory-graph/memorygraph-gemini/issues)
- [Blog Post: Announcing MemoryGraph for Gemini CLI](marketing/blog-post-draft.md)

## Community

- 🐛 **Found a bug?** [Open an issue](https://github.com/memory-graph/memorygraph-gemini/issues)
- 💡 **Have an idea?** [Start a discussion](https://github.com/memory-graph/memorygraph-gemini/discussions)
- 📖 **Need help?** Check the [documentation](https://memorygraph.dev/docs)
- 🎯 **Want to contribute?** PRs welcome!

## License

Apache 2.0 - see [LICENSE](LICENSE) for details.

---

**Built with ❤️ for the Gemini CLI community**
