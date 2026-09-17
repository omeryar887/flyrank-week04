# Week 6 Walkthrough

## Part A — Concept work

1. Review `workflow-vs-agent.md`.
2. Review `mcp-primitives.md`.
3. Read `explainer.md` and compare it with the required 600–900 word target.
4. Review `agent-upgrade.md`.

## Part B — Run the MCP server

The included server is a local, read-only Python MCP server.

From the `mcp-server` folder:

```powershell
py -m pip install -r requirements.txt
py server.py
```

For a stdio MCP server, the client normally launches the server process itself, so you should not need to keep a separate terminal running when Claude is configured to start it.

## Part C — Connect it to an MCP client

Use an MCP client that supports local stdio servers, such as a current Claude desktop client. Follow the client's current MCP/server configuration flow and point it at the absolute path to `server.py` using the Python executable on your machine.

A generic configuration shape is:

```json
{
  "mcpServers": {
    "flyrank-week6-files": {
      "command": "C:\\Path\\To\\Python\\python.exe",
      "args": ["C:\\Path\\To\\week-06-agent-mcp-basics\\mcp-server\\server.py"]
    }
  }
}
```

Do not copy the example paths literally. Replace them with real absolute paths on your computer.

## Part D — Run three tasks

Use the three task files in `tasks/`. For each task, capture a screenshot where the MCP tool call and the returned result are visible.

1. List files in the workflow package.
2. Read the Claude Project configuration.
3. Search the workflow failure-points document for human-review or failure-related text.

These tasks demonstrate that the client is actually using a connected tool rather than answering from the chat context alone.

## Evidence rule
Do not claim the connector works until the tool calls have actually appeared in the MCP client. Replace the evidence placeholders with screenshots and short notes after the real runs.
