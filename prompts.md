# Prompts Used

These prompts are designed to be pasted into the no-code project one stage at a time. The output from one stage becomes the input to the next stage.

## Prompt 1 — Gather

```text
STAGE 1 — GATHER

Topic/source:
{{INPUT}}

Extract the evidence needed to create study notes.

Return:
1. Key facts
2. Definitions
3. Procedures or steps
4. Examples explicitly present in the source
5. Important constraints or warnings
6. Source references/locations when available
7. Missing information that prevents a complete explanation

Rules:
- Use the supplied source as the primary evidence.
- Do not invent facts.
- Do not write the final study notes yet.
- Mark unsupported or missing information clearly.
```

## Prompt 2 — Synthesize

```text
STAGE 2 — SYNTHESIZE

Use the Stage 1 evidence packet below.

{{GATHER_OUTPUT}}

Build a logical topic structure.

Return:
1. Topic overview
2. Key concepts in logical order
3. Relationships/dependencies
4. Important differences or comparisons
5. Beginner prerequisites
6. Evidence gaps
7. A compact outline for the final notes

Rules:
- Do not add unsupported claims.
- Keep source-supported facts traceable to the evidence packet.
- If two pieces of evidence conflict, flag the conflict instead of choosing silently.
```

## Prompt 3 — Draft

```text
STAGE 3 — DRAFT

Create beginner-friendly technical study notes from this synthesis:

{{SYNTHESIS_OUTPUT}}

Return:
- clear headings;
- simple definitions;
- step-by-step explanations where useful;
- practical examples;
- common mistakes or warnings when supported;
- a short recap.

Rules:
- Stay faithful to the supplied synthesis.
- Do not invent citations or source claims.
- Label illustrative examples when they are not directly from the source.
```

## Prompt 4 — Review & format

```text
STAGE 4 — REVIEW AND FORMAT

Review the draft below against the Gather evidence and Synthesis.

GATHER:
{{GATHER_OUTPUT}}

SYNTHESIS:
{{SYNTHESIS_OUTPUT}}

DRAFT:
{{DRAFT_OUTPUT}}

Perform a strict quality check:
1. Identify unsupported claims.
2. Identify missing important steps.
3. Identify misleading simplifications.
4. Identify terminology that changed meaning.
5. Identify examples that need verification.
6. Identify source gaps or conflicts.

Then output the final study notes using:
1. Topic
2. Short explanation
3. Key terms
4. Main concepts
5. Step-by-step explanation
6. Examples
7. What the source supports
8. What needs human verification
9. Final review status

Never hide a problem just to make the final notes look complete.
```
