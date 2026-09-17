# FL-07 Walkthrough

## 1. Start the server

Create the virtual environment, install `mcp`, and confirm the server starts.

## 2. Connect it to Claude

Add the MCP server to the client configuration using the actual absolute paths on the machine. Restart the client and verify the three tools appear.

## 3. Load the agent instructions

Use `agent/CLAUDE_PROJECT_INSTRUCTIONS.md` as the project's instructions or equivalent system-level instructions in the selected Claude environment.

## 4. Run the new input

Use `agent/run-prompt.md` exactly as the single request for the checkpoint recording. Do not edit intermediate results.

## 5. Observe the loop

The expected behavior is:

1. Agent understands the request.
2. Agent discovers the workspace.
3. Agent searches for relevant evidence.
4. Agent reads the selected source.
5. Agent writes study notes.
6. Agent checks the result against retrieved evidence.
7. Agent reports sources, gaps, and human review.

## 6. Capture evidence

Record approximately two minutes from the initial request through the final result. Keep the recording raw and unedited. The recording should show tool calls, not just the final answer.
