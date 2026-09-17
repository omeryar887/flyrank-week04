# Build Log — FL-07

> Keep this log chronological. The entries below are the planned/initial build record. After the real run, append the actual timestamp, failure, change, and result rather than rewriting history.

| Step | What happened | Change | Reason | Result |
|---|---|---|---|---|
| 1 | FL-06 classified the original pipeline as a workflow | Reused the same core job | Keep scope narrow for Checkpoint 1 | Defined MVP |
| 2 | A live tool was required | Added a read-only local MCP server | Need genuine external tool use | Three tools available |
| 3 | Unbounded filesystem access would be unnecessary | Added workspace-root validation | Reduce accidental access | Reads stay inside project workspace |
| 4 | Writing files would expand scope | Kept server read-only | MVP only needs gather/read | Simpler first build |
| 5 | Automated evidence would be misleading without a real client run | Left screenshots/timing as live evidence | Keep submission honest | Ready for actual recording |

## Spec cuts

- No automatic file writing in the MVP.
- No web search connector in the MVP.
- No multi-agent architecture.
- No long-running background loop.
- No external database.

These cuts keep the checkpoint focused on one end-to-end job with one real tool connection.

## Actual run notes

Add entries here after the real Claude run:

- Date/time:
- New input used:
- Tools called:
- What broke:
- What changed:
- What was cut:
- Final result:
- Manual intervention during run: None / Describe exactly
