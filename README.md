# Week 5: Build a No-Code Workflow

## Phase
Build (core)

## Estimated effort
7 hours

## One-line claim
I build practical software systems that turn real requirements into usable web, mobile, and backend solutions.

## What this week proves
Single prompts are useful, but a repeatable workflow is more valuable. This week turns a research/writing task into a small multi-step pipeline with clear handoffs, repeatable prompts, testing, timing, and human review.

## Pipeline chosen
**Source-grounded study notes**

The workflow takes a new technical topic and moves it through four distinct steps:

1. **Gather** — identify useful source material and extract only source-supported facts.
2. **Synthesize** — organize the extracted facts into a clean understanding of the topic.
3. **Draft** — turn the synthesis into readable study notes with examples.
4. **Review & format** — check accuracy against the supplied source material, flag unsupported claims, and format the final notes.

## No-code build
The intended no-code implementation is a structured **Claude Project**. The project instructions, step prompts, handoff formats, and run records are included in this folder so the workflow can be reproduced without writing application code.

## Important evidence note
The workflow configuration is complete and the five run records are provided as a working evidence structure. Where an actual external tool execution is required, the record explicitly identifies what must be replaced with the user's real output rather than pretending an external Claude/NotebookLM run happened here.

## Folder structure

```text
build-workflow/
├── README.md
├── workflow-design.md
├── claude-project-config.md
├── prompts.md
├── handoff-contracts.md
├── walkthrough.md
├── time-accounting.md
├── failure-points.md
├── human-review-checklist.md
├── evidence-checklist.md
├── runs/
│   ├── run-01-http-apis.md
│   ├── run-02-databases.md
│   ├── run-03-git.md
│   ├── run-04-rest-api-security.md
│   └── run-05-software-testing.md
└── workflow/
    └── source-grounded-study-notes-flow.md
```

## Pass/revise checklist

- [x] Three+ distinct workflow steps defined.
- [x] Handoffs between steps defined.
- [x] Every prompt/configuration is documented.
- [x] Five real technical inputs are specified.
- [x] Time accounting includes setup cost.
- [x] Failure points are named.
- [x] Human review responsibilities are named.
- [ ] External-tool screenshots/URLs must be added after the actual Claude Project is run.

## Status
**Build package ready. External execution evidence must be captured from the selected no-code tool before treating the submission as fully verified.**
