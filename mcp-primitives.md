# MCP Primitives

Model Context Protocol (MCP) is a standard way for AI applications to connect models with external context and capabilities.

## 1. Tools
Tools are callable functions. They allow a model to ask the connected server to perform an operation, such as searching files, querying a service, calculating something, or taking another supported action.

**In this project:** `list_files`, `read_file`, and `search_files` are tools.

## 2. Resources
Resources are readable pieces of contextual information exposed by an MCP server. They are useful when an application or model needs structured, read-only information from an external system.

**In this project:** `workflow://fl-04` exposes the FL-04 workflow description.

## 3. Prompts
Prompts are reusable templates that a user can select and fill with arguments. They help make repeated interactions consistent.

**In this project:** `review_workflow_file` is a reusable review prompt.

## Simple mental model

```text
Prompts  → reusable instructions for the user
Resources → context/data made available to the client
Tools     → functions the model can call
```

The important distinction is that MCP is the connection/protocol layer. It does not automatically turn every connected chat into an autonomous agent. An agent still needs model-driven decision-making, tool use, feedback, and an execution loop.
