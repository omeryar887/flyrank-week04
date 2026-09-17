# Workflow vs Agent

## Workflow
A workflow is a planned sequence. The builder decides the stages and the handoffs before execution. An LLM can perform one or more stages, but the overall path is predetermined.

For FL-04, the path is:

```text
Source → Gather → Synthesize → Draft → Review & format → Human check
```

If the same kind of input is supplied again, the workflow still follows those stages in that order.

## Agent
An agent gives the model more control over the process. Instead of following one fixed route, the model can decide what action or tool to use next based on what it observes. A typical agent can plan, act through tools, inspect the result, adjust its approach, and continue until a stopping condition or human checkpoint is reached.

## FL-04 classification
**FL-04 is a workflow.**

The key reason is not simply that it has multiple prompts. It is that the handoffs and sequence are fixed. The model is not deciding whether it needs another research pass, which tool to call next, or whether to change the overall plan. Those decisions are outside the current workflow design.

This matches Anthropic's distinction: workflows use predefined paths, while agents dynamically direct their own process and tool use. See the source notes for the exact source basis.
