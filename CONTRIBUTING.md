# Contributing to MemoryGraph Gemini CLI Extension

Thank you for your interest in contributing! This document provides guidelines for contributing to the MemoryGraph Gemini CLI extension.

## Getting Started

### Prerequisites

- [Gemini CLI](https://github.com/google-gemini/gemini-cli) installed
- [MemoryGraph MCP Server](https://github.com/memory-graph/memorygraph) installed via `pipx install memorygraphMCP`
- Python 3.10+ (for running validation scripts)

### Local Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/memory-graph/memorygraph-gemini.git
   cd memorygraph-gemini
   ```

2. Install the extension locally:
   ```bash
   gemini extensions install . --consent
   ```

3. Verify installation:
   ```bash
   gemini extensions list
   # Should show: memorygraph (1.0.0)
   ```

## Making Changes

### Code Style

- **TOML files**: Follow the existing format in `commands/memory/`
- **Markdown**: Use standard GitHub-flavored Markdown
- **JSON**: Use 2-space indentation

### Validation

Before submitting changes, run the validation script:

```bash
python3 scripts/validate.py
```

This checks:
- JSON syntax in manifest files
- TOML syntax in command files
- Required fields are present

### Testing Changes

1. Reinstall the extension after changes:
   ```bash
   gemini extensions uninstall memorygraph
   gemini extensions install . --consent
   ```

2. Test in a Gemini CLI session:
   ```bash
   gemini -y
   > "Recall memories about testing"
   ```

## Submitting Changes

### Issues

- **Bug reports**: Include Gemini CLI version, OS, and steps to reproduce
- **Feature requests**: Describe the use case and expected behavior

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run validation: `python3 scripts/validate.py`
5. Commit with a clear message following [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat: Add new command`
   - `fix: Correct TOML syntax`
   - `docs: Update installation guide`
6. Push and open a PR

### PR Checklist

- [ ] Validation passes (`python3 scripts/validate.py`)
- [ ] Documentation updated if needed
- [ ] CHANGELOG.md updated for user-facing changes
- [ ] Commit messages follow conventional format

## Project Structure

```
memorygraph-gemini/
├── gemini-extension.json     # Extension manifest
├── GEMINI.md                 # AI context file
├── commands/memory/          # TOML command files
│   ├── learn-track.toml
│   ├── conductor-context.toml
│   ├── auto-learn.toml
│   ├── restore-context.toml
│   └── detect-conflicts.toml
├── docs/                     # User documentation
├── marketing/                # Launch and marketing materials
└── scripts/                  # Development scripts
```

## Command File Format

TOML command files follow this structure:

```toml
description = "Brief description shown in help"

# NOTE: This file contains prompt instructions for the LLM, not executable code.
# Code blocks illustrate MCP tool calls to make. Actual tool names may vary.

prompt = """
## SYSTEM DIRECTIVE
Clear instructions for the AI...

## PROTOCOL
Step-by-step process...

## OUTPUT FORMAT
Expected output structure...
"""
```

## Questions?

- Open a [GitHub Issue](https://github.com/memory-graph/memorygraph-gemini/issues)
- Check existing [Discussions](https://github.com/memory-graph/memorygraph-gemini/discussions)

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
