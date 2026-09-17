# Agent Concepts and MCP Basics — Explainer

## From a fixed workflow to a tool-using agent

An AI workflow and an AI agent can look similar from the outside because both can use language models and multiple steps. The important difference is who controls the path. In a workflow, the builder defines the route ahead of time. In an agent, the model has more control over deciding what to do next and which tools to use based on what it learns during execution.

My FL-04 build, the Source-Grounded Technical Study Notes pipeline, is a workflow. It has four planned stages: Gather, Synthesize, Draft, and Review & format. Each stage has a defined output that becomes the input to the next stage. That makes the process predictable and easy to inspect. If a new technical source arrives, the system does not decide on its own to invent a fifth stage, search a different system, or repeat research. The path was designed beforehand. This is consistent with Anthropic's distinction between predefined workflows and agents that dynamically direct their own process and tool use.

An agent is better understood as an AI system that can direct its own process while working toward a goal. A useful agent loop is: understand the task, decide what action is needed, use a tool, observe the result, decide what to do next, and continue until the task is complete or a human checkpoint is needed. Anthropic describes agents as systems where the LLM dynamically directs its process and tool use, with environmental feedback helping it assess progress.

## What MCP adds

Model Context Protocol, or MCP, is a standard way for AI applications to connect models with external systems. Instead of creating a different custom integration pattern for every AI application and tool, MCP provides a common protocol for exposing capabilities and context. The official documentation describes three core primitives: tools, resources, and prompts.

Tools are callable functions. For example, an MCP server can expose a file-search function, a database query, or another supported operation. In my Week 6 practice server, the tools are deliberately simple and read-only: listing files, reading a file, and searching files. These are useful because a normal chat message does not automatically have access to the contents of my local project directory.

Resources provide readable context. A resource can expose information such as file contents or another structured source that a client can make available to the model. My practice server exposes the FL-04 workflow description as a resource. Prompts are reusable templates that users can select and fill with arguments. The MCP documentation treats prompts as user-selected templates, which makes them useful for repeated tasks without pretending they are autonomous actions.

MCP therefore does not equal agent. MCP is an interface for connecting an AI application to context and capabilities. An agent can use MCP tools as part of its action loop, but a fixed workflow can also use MCP tools without becoming an agent.

## What FL-04 would need to become an agent

The first upgrade I would make is a **research-loop decision step**. Instead of always doing Gather → Synthesize → Draft → Review exactly once, the system would inspect the evidence after the first gather stage and decide whether the source coverage is sufficient. If important claims are missing, it could use an MCP research tool to gather another source, inspect the new evidence, and repeat until a defined evidence threshold is met or a maximum number of iterations is reached.

That change would introduce model-directed decisions and tool use. The agent could choose whether to search again, which available research operation to call, and when the evidence was good enough to move forward. A stopping rule would still be necessary because more autonomy also creates more opportunities for cost, latency, or compounding errors. Anthropic recommends adding complexity only when it improves the result and emphasizes testing and guardrails for autonomous systems.

A human would still review important claims, source quality, and the final study notes. The goal would not be to make the system autonomous just for the label. The goal would be to give it enough decision-making ability to handle research cases where the correct number of steps cannot be known in advance.

## Sources

- Anthropic, *Building Effective Agents*: https://www.anthropic.com/engineering/building-effective-agents
- Model Context Protocol documentation: https://modelcontextprotocol.io/docs/getting-started/intro
- MCP server concepts: https://modelcontextprotocol.io/specification/draft/server
