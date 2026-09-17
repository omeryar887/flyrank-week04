# Workflow Design

## Chosen pipeline: Source-grounded study notes

### Problem
When making study notes from technical material, doing every step manually means repeatedly reading, extracting, organizing, drafting, and checking the same information.

### Goal
Create a repeatable workflow that starts with a new source/topic and produces structured study notes while keeping source grounding and human verification visible.

## Step diagram

```text
NEW INPUT / SOURCE
       |
       v
+----------------+
| 1. GATHER      |
| Extract facts  |
| + source refs  |
+----------------+
       |
       | Handoff A: evidence packet
       v
+----------------+
| 2. SYNTHESIZE  |
| Group facts,   |
| define terms,  |
| connect ideas  |
+----------------+
       |
       | Handoff B: topic outline
       v
+----------------+
| 3. DRAFT       |
| Study notes +  |
| examples       |
+----------------+
       |
       | Handoff C: draft notes
       v
+----------------+
| 4. REVIEW      |
| Check support, |
| gaps, clarity, |
| and formatting |
+----------------+
       |
       v
FINAL STUDY NOTES
       |
       v
HUMAN CHECK
``` 

## Why four steps
The assignment requires three or more distinct steps. Four makes the handoffs visible and separates source extraction from writing and quality checking.

## Input contract
Each run starts with:
- one new technical topic or source;
- the intended learner level: beginner/intermediate;
- any source text or links available to the no-code tool;
- requested note format.

## Output contract
The final output contains:
- short topic overview;
- key definitions;
- important concepts;
- step-by-step explanation where appropriate;
- one or more practical examples;
- source-grounding notes;
- uncertainty or missing-source warnings;
- human-review flags.
