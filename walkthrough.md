# Workflow Walkthrough

## 1. Start with a new input
Choose a new technical topic and provide the source material to the configured no-code project.

## 2. Run Gather
Paste the input into Prompt 1. Save the evidence packet.

## 3. Run Synthesize
Pass the evidence packet into Prompt 2. Save the structured outline.

## 4. Run Draft
Pass the synthesis into Prompt 3. Save the candidate notes.

## 5. Run Review
Pass Gather + Synthesis + Draft into Prompt 4. Save the final notes and review flags.

## 6. Human check
The human reviewer checks the source for the flagged claims, verifies important technical details, and confirms that the notes are appropriate for the intended learner.

## End-to-end test
A brand-new input should move through all four stages without changing the workflow design. Only the input and source material should change.

## What counts as a successful run
A run is successful when:
- all four stages execute;
- each stage receives the previous stage's required handoff;
- the final output follows the required format;
- review flags are present even when there are no major issues;
- no unsupported claim is presented as source-backed.
