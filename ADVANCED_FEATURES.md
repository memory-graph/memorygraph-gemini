# Advanced Features Guide

This guide covers the Phase 3 advanced features that enhance MemoryGraph's integration with Conductor workflows.

## Overview

Phase 3 adds three powerful commands that automate knowledge capture, restore session context, and prevent file conflicts:

1. **Auto-Learning** - Automatically extract learnings from archived tracks
2. **Context Restoration** - Resume work seamlessly across sessions
3. **Conflict Detection** - Identify potential coordination issues

## Command Reference

### `/memory:auto-learn`

**Purpose**: Automatically extract and store learnings from recently archived Conductor tracks.

**When to use**:
- After archiving one or more tracks
- Periodically to catch any missed archives
- As part of an automated workflow

**Basic usage**:
```bash
gemini> /memory:auto-learn
```

**What it does**:
1. Scans `conductor/archive/` for recently archived tracks (last 7 days by default)
2. Identifies tracks not yet processed (no `.memorygraph-processed` marker)
3. Extracts learnings using the same logic as `/memory:learn-track`
4. Creates marker files to prevent duplicate processing
5. Provides aggregated summary of all knowledge captured

**Setup Options**:

**Option 1: Manual Trigger** (Recommended for getting started)
```bash
# After archiving
gemini> /conductor:archive feature-user-auth
gemini> /memory:auto-learn
```

**Option 2: Script Automation**
Create `scripts/archive-with-learning.sh`:
```bash
#!/bin/bash
TRACK_NAME=$1
gemini <<EOF
/conductor:archive ${TRACK_NAME}
/memory:auto-learn
EOF
```

Usage: `./scripts/archive-with-learning.sh feature-user-auth`

**Option 3: File Watcher** (Advanced)
Monitor archive directory and auto-trigger learning extraction (see command documentation for setup).

---

### `/memory:restore-context`

**Purpose**: Restore full context when resuming work on a track from a previous session.

**When to use**:
- Resuming work after a break (hours, days, or weeks)
- Starting a new session on an in-progress track
- Switching between multiple tracks
- After system restart or context loss

**Basic usage**:
```bash
gemini> /memory:restore-context feature-user-auth
```

**What it does**:
1. Searches MemoryGraph for all context related to the track
2. Analyzes current track state from Conductor files
3. Calculates session gap and estimates completion percentage
4. Presents comprehensive "Resuming Track" summary including:
   - What you completed
   - Where you left off
   - Active blockers and how past ones were resolved
   - Key technical decisions made
   - Files modified
   - Related memories from MemoryGraph
   - Recommended next actions

**Output modes**:
```bash
# Standard (default)
gemini> /memory:restore-context feature-user-auth

# Compact (quick resume)
gemini> /memory:restore-context feature-user-auth --compact

# Detailed (for long gaps)
gemini> /memory:restore-context feature-user-auth --detailed

# JSON (for scripting)
gemini> /memory:restore-context feature-user-auth --json
```

**Smart Features**:
- **Session Gap Intelligence**: Adjusts detail level based on time since last session
- **Context Drift Detection**: Warns if significant changes occurred since last session
- **Cross-Track Coordination**: Alerts if related tracks modified shared files
- **Smart Recommendations**: Suggests patterns and warns about pitfalls based on history

---

### `/memory:detect-conflicts`

**Purpose**: Detect potential conflicts when files you're about to modify were recently changed by other tracks.

**When to use**:
- Before starting a new track that touches existing code
- During track planning after creating spec.md
- When encountering unexpected changes in files
- Periodically for active multi-developer projects

**Basic usage**:
```bash
# Auto-detect from current track
gemini> /memory:detect-conflicts

# Specify files explicitly
gemini> /memory:detect-conflicts src/auth/middleware.ts src/utils/jwt.ts

# Check entire directory
gemini> /memory:detect-conflicts src/auth/
```

**What it does**:
1. Identifies files in scope (from track spec/plan or explicit arguments)
2. Searches MemoryGraph for recent modifications to those files
3. Performs temporal analysis to categorize conflicts:
   - 🔴 **CRITICAL** (<24 hours): Active work, immediate coordination needed
   - 🟡 **RECENT** (1-7 days): Review recommended
   - 🟢 **HISTORICAL** (>7 days): Context useful but low conflict risk
4. Analyzes conflict severity and provides recommendations
5. Generates detailed conflict report with action plan

**Conflict Severity Levels**:

**HIGH SEVERITY**:
- Same file modified in multiple active tracks
- Modifications in last 24 hours
- Overlapping functionality (same functions/classes)
- Different developers working simultaneously

**MEDIUM SEVERITY**:
- Same file modified in recently completed track
- Changes within last week
- Related but non-overlapping functionality

**LOW SEVERITY**:
- File mentioned in older tracks (>7 days)
- Different parts of codebase
- Informational context only

**Output modes**:
```bash
# Standard report (default)
gemini> /memory:detect-conflicts

# Compact summary
gemini> /memory:detect-conflicts --compact

# JSON output
gemini> /memory:detect-conflicts --json
```

## Recommended Workflow

### Complete Conductor + MemoryGraph Workflow

**1. Initial Setup**
```bash
gemini> /conductor:setup
gemini> /memory:conductor-context
```

**2. Starting a New Track**
```bash
gemini> /conductor:newTrack feature-payment-processing
# ... create spec.md with file paths ...
gemini> /memory:detect-conflicts
# Review any conflicts before proceeding
```

**3. Resuming Previous Work**
```bash
gemini> /memory:restore-context feature-user-auth
gemini> /conductor:implement feature-user-auth
# Continue with full context restored
```

**4. During Development**
```bash
# Use natural language to recall patterns
> I'm implementing the checkout flow. What patterns have I used before?
> What are common pitfalls with Stripe webhooks?
```

**5. After Track Completion**
```bash
gemini> /memory:learn-track feature-checkout
# Extract and store learnings manually
```

**6. After Archiving**
```bash
gemini> /memory:auto-learn
# Automatically capture learnings from all recent archives
```

**7. Before Major Changes**
```bash
gemini> /memory:detect-conflicts src/auth/
# Check for conflicts before modifying critical code
```

## Integration Scenarios

### Solo Developer Workflow

**Focus**: Session continuity and knowledge retention

```bash
# Monday: Start new feature
gemini> /conductor:newTrack feature-oauth
gemini> /memory:detect-conflicts

# Wednesday: Resume after break
gemini> /memory:restore-context feature-oauth
gemini> /conductor:implement feature-oauth

# Friday: Complete and archive
gemini> /conductor:archive feature-oauth
gemini> /memory:auto-learn
```

### Team Development Workflow

**Focus**: Coordination and conflict prevention

```bash
# Before starting work
gemini> /memory:restore-context feature-api-v2
gemini> /memory:detect-conflicts

# Check for conflicts frequently
gemini> /memory:detect-conflicts src/api/

# Coordinate on high-severity conflicts
# Review other team members' recent changes
```

### Long-Term Projects

**Focus**: Context preservation across extended gaps

```bash
# Resuming after 2 weeks
gemini> /memory:restore-context feature-migration
# Detailed summary with context drift warnings

# Check what changed during break
gemini> /memory:detect-conflicts
# Identify any architectural changes

# Batch process all archived work
gemini> /memory:auto-learn
```

## Tips and Best Practices

### Auto-Learning
- Run `auto-learn` regularly to keep knowledge base current
- Consider setting up file watcher for automatic processing
- Review high-value learnings (importance ≥ 0.8) for documentation

### Context Restoration
- Run before every session on in-progress tracks
- Pay attention to context drift warnings
- Review recommended next actions before diving in
- Use compact mode for same-day resume, detailed for longer gaps

### Conflict Detection
- Run during track planning, not just before implementation
- Prioritize high-severity conflicts for immediate coordination
- Use medium-severity conflicts as code review opportunities
- Learn from historical conflicts to improve architecture

### General Best Practices
- **Be proactive**: Run detect-conflicts before starting, not after encountering problems
- **Stay consistent**: Make auto-learn part of your archive workflow
- **Trust the system**: Context restoration improves as your memory graph grows
- **Review regularly**: Periodically check high-value learnings for patterns

## Troubleshooting

### "No archives found"
- Ensure Conductor is installed and configured
- Check that tracks have been archived to `conductor/archive/`
- Verify directory path is correct

### "No context available"
- Normal for new tracks without prior sessions
- Context will accumulate as you store memories during work
- Run `/memory:learn-track` after completing work to populate

### "No conflicts detected" but git shows conflicts
- MemoryGraph detects semantic conflicts, git shows textual conflicts
- MemoryGraph relies on stored memories - may not have full history yet
- Use both MemoryGraph AND git for comprehensive conflict detection

### Partial processing failures
- Check marker files in archived tracks (`.memorygraph-processed`)
- Re-run with verbose logging to identify issues
- Can safely re-run commands - they're designed to be idempotent

## Advanced Usage

### Scripting with JSON Output

```bash
# Get conflict data programmatically
CONFLICTS=$(gemini -c "/memory:detect-conflicts --json")
HIGH_SEVERITY=$(echo $CONFLICTS | jq '.summary.high_severity')

if [ $HIGH_SEVERITY -gt 0 ]; then
  echo "WARNING: $HIGH_SEVERITY high-severity conflicts detected!"
  exit 1
fi
```

### Custom Automation

Create your own workflows combining these commands:

```bash
#!/bin/bash
# smart-resume.sh - Intelligent session startup

TRACK=$1

echo "Restoring context for $TRACK..."
gemini -c "/memory:restore-context $TRACK"

echo "Checking for conflicts..."
gemini -c "/memory:detect-conflicts"

echo "Ready to work on $TRACK!"
```

### Integration with Git Hooks

```bash
# .git/hooks/pre-push
#!/bin/bash
# Check for conflicts before pushing

gemini -c "/memory:detect-conflicts --compact" || {
  echo "Conflicts detected. Review before pushing."
  exit 1
}
```

## Future Enhancements

Planned improvements for these features:

1. **Conductor Integration**: Automatic context restoration when running `/conductor:implement`
2. **Team Collaboration**: Multi-developer coordination and notification features
3. **Predictive Conflicts**: ML-based prediction of potential conflicts before they occur
4. **Smart Scheduling**: Recommend optimal timing for track work based on conflict patterns
5. **Cross-Repository**: Detect conflicts across multiple related projects

## Feedback and Contributions

These are new features! Your feedback helps improve them:

- Found a bug? [Open an issue](https://github.com/memorygraphdev/memorygraph-gemini/issues)
- Have a suggestion? [Start a discussion](https://github.com/memorygraphdev/memorygraph-gemini/discussions)
- Want to contribute? PRs welcome!

---

**Built with ❤️ for seamless context-driven development**
