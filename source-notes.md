# Source Notes

## Anthropic — Building Effective Agents
Source: https://www.anthropic.com/engineering/building-effective-agents

Relevant ideas used in this assignment:
- Workflows use predefined code paths.
- Agents dynamically direct their own processes and tool use.
- Agents can use environmental/tool results as feedback and continue until completion or a stopping condition.
- Workflows are useful when tasks can be decomposed into predictable subtasks.
- Agentic systems add complexity, cost, latency, and possible compounding errors, so complexity should be justified and tested.

## Model Context Protocol
Source: https://modelcontextprotocol.io/docs/getting-started/intro

Relevant ideas used in this assignment:
- MCP standardizes how AI applications connect to external context and capabilities.
- Core server primitives include tools, resources, and prompts.

## MCP server concepts
Source: https://modelcontextprotocol.io/specification/draft/server

Relevant ideas used in this assignment:
- Prompts are predefined templates/instructions.
- Resources provide structured contextual data.
- Tools are executable functions available to the model.

## MCP SDK reference
Source: https://py.sdk.modelcontextprotocol.io/

Relevant implementation basis:
- Python MCP SDK provides server/client support.
- FastMCP can expose tools, resources, and prompts.
- This project uses a local stdio-style server so an MCP client can launch it as a process.
