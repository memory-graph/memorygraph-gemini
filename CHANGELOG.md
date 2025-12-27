# Changelog

All notable changes to the MemoryGraph Gemini CLI extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

#### Conductor Integration Commands (Phase 2)
- **`/memory:learn-track`** command - Extract and store learnings from completed Conductor tracks
  - Analyzes spec.md and plan.md to identify reusable patterns
  - Automatically creates problem→solution relationships
  - Scores importance based on cross-project applicability
  - Generates detailed extraction reports with statistics
- **`/memory:conductor-context`** command - Inject historical context into Conductor setup
  - Searches MemoryGraph for relevant patterns based on tech stack
  - Identifies common pitfalls with chosen technologies
  - Finds similar past projects for context
  - Enhances tech-stack.md, product.md, and workflow.md with "Historical Insights" sections
- **Conductor integration documentation** in README with workflow best practices
- **Integration architecture diagram** showing Conductor ↔ MemoryGraph synergy

## [1.0.0] - 2025-12-27

### 🎉 Initial Release

**MemoryGraph for Gemini CLI is the first persistent memory extension for Google's AI coding tool.**

### Added

#### Core Memory Features
- **Natural language memory search** via `recall_memories` - fuzzy matching across all stored knowledge
- **Structured search** with `search_memories` - filter by type, tags, importance, project
- **Memory storage** with `store_memory` - capture solutions, patterns, errors, and fixes
- **Memory retrieval** with `get_memory` - access specific memories by ID
- **Memory updates** with `update_memory` - refine and improve stored knowledge
- **Memory deletion** with `delete_memory` - remove outdated or incorrect information

#### Graph-Based Relationships
- **Create relationships** between memories (SOLVES, CAUSES, FIXES, DEPENDS_ON, etc.)
- **Navigate memory graph** with `get_related_memories` - find connected knowledge
- **Relationship types** - 35+ semantic relationship types for rich context

#### Backend Support
- **SQLite backend** (default) - zero-config local storage
- **Neo4j backend** - enterprise graph database support
- **FalkorDB backend** - high-performance graph queries
- **Cloud backend** - sync across machines via memorygraph.dev

#### Gemini CLI Integration
- **Automatic tool registration** - MemoryGraph tools available in all sessions
- **Conductor compatibility** - extract learnings from archived tracks
- **Cross-project memory** - knowledge persists beyond project boundaries
- **Natural language interface** - no manual tool invocation needed

#### Memory Types
- `solution` - Working fixes and approaches
- `problem` - Bugs, issues, blockers
- `error` - Error messages and stack traces
- `fix` - Code changes that resolved errors
- `code_pattern` - Reusable patterns and idioms
- `technology` - Tech stack knowledge
- `task` - Completed work
- `workflow` - Process patterns
- `project` - Project context and decisions
- `command` - Useful CLI commands
- `file_context` - Important file locations
- `general` - Everything else

### Documentation
- Comprehensive README with installation, configuration, and usage examples
- Extension manifest (`gemini-extension.json`) with MCP server configuration
- Apache 2.0 license
- Troubleshooting guide

### Links
- GitHub Repository: https://github.com/memory-graph/memorygraph-gemini
- Documentation: https://memorygraph.dev/docs
- Gemini CLI Extensions Gallery: https://geminicli.com/extensions/

---

## Future Roadmap

### Planned Features
- **Visual memory browser** - GUI for exploring the memory graph
- **Memory analytics** - insights into stored knowledge patterns
- **Team memory sharing** - collaborative knowledge bases
- **Advanced filtering** - temporal queries, importance scoring
- **Memory migrations** - import/export between backends
- **Integration examples** - common workflow templates

### Coming Soon
- Support for custom memory types
- Batch memory operations
- Memory versioning and history
- Search result ranking improvements
- Performance optimizations for large memory graphs

---

[1.0.0]: https://github.com/memory-graph/memorygraph-gemini/releases/tag/v1.0.0
