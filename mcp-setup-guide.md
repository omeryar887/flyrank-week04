# MCP Setup Guide

## Goal
Connect the included read-only local MCP server to an MCP client and run three tool calls.

## Requirements
- Python 3.10 or newer.
- An MCP client that supports local stdio MCP servers.
- Access to this Week 6 folder.

## Install
Open PowerShell in `mcp-server`:

```powershell
py -m pip install -r requirements.txt
```

## Server
The server file is:

```text
mcp-server/server.py
```

It exposes:

| Primitive | Name | Purpose |
|---|---|---|
| Tool | `list_files` | Lists files under the allowed project directory |
| Tool | `read_file` | Reads a text file from the project |
| Tool | `search_files` | Searches text files for a phrase |
| Resource | `workflow://fl-04` | Exposes the FL-04 workflow description |
| Prompt | `review_workflow_file` | Creates a reusable review instruction |

## Client configuration
Configure the MCP client to launch `server.py` through your Python executable. Use absolute paths.

Example shape:

```json
{
  "mcpServers": {
    "flyrank-week6-files": {
      "command": "C:\\Path\\To\\python.exe",
      "args": ["C:\\Path\\To\\mcp-server\\server.py"]
    }
  }
}
```

The exact location and UI for MCP configuration can vary by client version. Use the current client documentation for the final placement of this configuration.

## Security choice
The server is intentionally read-only. It only allows access to files below the Week 6 project directory. It does not provide arbitrary shell execution, file deletion, file writing, or credential access.

## What counts as evidence
A valid screenshot should show:
- the MCP server/tool name;
- the tool call;
- the input supplied to the tool;
- the returned result;
- enough surrounding UI to show the result came from a tool call rather than ordinary assistant text.
