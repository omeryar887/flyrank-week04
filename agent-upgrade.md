# Concrete Agent Upgrade for FL-04

## Upgrade: Evidence-driven research loop

### Current workflow
```text
Gather → Synthesize → Draft → Review → Human check
```

### Proposed agent version
```text
New source
   ↓
Agent inspects source coverage
   ↓
Enough evidence?
 ┌──────┴──────┐
Yes           No
 ↓             ↓
Synthesize   Use MCP research/search tool
 ↓             ↓
Draft      Inspect new result
 ↓             ↓
Review  ←─────┘
 ↓
Human check
```

### What changes
The model would be allowed to decide whether another research pass is necessary. It could call a connected research tool, inspect the returned evidence, and decide whether to continue or move forward.

### Guardrails
- Maximum number of research iterations.
- Only approved/read-only research tools.
- Require source references for important claims.
- Stop and request human input when evidence conflicts.
- Human approval before publishing or submitting final notes.

### Why this is an agent upgrade
The important change is not adding another prompt. The model gains control over the next action based on tool results. That is the part that moves the design away from a fixed path and toward an agentic loop.
