# Week 7 — Build the Agent

## Checkpoint 1: MVP

**Phase:** Build (core)  
**Estimated effort:** 10 hours  
**Platform:** Claude Desktop / MCP client  
**Core job:** Turn a new technical source in the project workspace into source-grounded study notes without mid-run hand editing.

This build continues the FL-06 work. FL-06 established that the original pipeline was a fixed workflow. This checkpoint adds a live MCP connection and gives Claude permission to inspect the workspace dynamically while completing the core task.

## MVP loop

```text
User gives source/topic
        ↓
Agent inspects workspace with MCP
        ↓
Agent identifies the relevant source
        ↓
Agent reads the source and supporting workflow rules
        ↓
Agent produces study notes
        ↓
Agent runs a quality check against the source
        ↓
Final notes + source gaps + human-review items
```

## Live connection

The included MCP server exposes read-only tools for listing files, reading files, and searching file contents. Configure it in the selected MCP client before claiming a live run.

## Definition of done

- [ ] MCP server connected and visible to Claude.
- [ ] A brand-new input is supplied.
- [ ] Claude selects and reads the relevant files through MCP.
- [ ] Claude creates the study-note result without the user editing intermediate output.
- [ ] Final answer identifies sources and uncertainty.
- [ ] Raw, unedited ~2-minute screen recording captured.
- [ ] Build log records actual failures and changes.

**Evidence rule:** screenshots, timings, and the screen recording are left for the real run. They are not fabricated in this repository.
