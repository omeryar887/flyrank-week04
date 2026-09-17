# Failure Points and Human Review

## Known failure points

1. **Weak sources** — poor or incomplete source material leads to incomplete notes.
2. **Source ambiguity** — a sentence can be interpreted more broadly than the source intended.
3. **Over-simplification** — beginner-friendly wording can remove an important technical condition.
4. **Example drift** — a generated example may look correct while not being supported by the supplied source.
5. **Missing context** — the source may assume prerequisites the learner does not know.
6. **Conflicting evidence** — multiple sources can disagree; the workflow must flag the conflict.
7. **Prompt leakage between stages** — if the previous output is pasted incompletely, later stages may make incorrect assumptions.
8. **Formatting bias** — a polished final answer can look more reliable than the evidence actually is.
9. **Tool limits** — a no-code service can have context, account, rate, or feature limits.
10. **Human verification remains necessary** — important technical claims should still be checked against the source.

## Human must still check

- source quality and relevance;
- important technical facts;
- commands, code, versions, and API behavior when applicable;
- examples that could cause incorrect implementation;
- missing prerequisites;
- conflicts between sources;
- whether the final notes actually answer the learning goal.

## Rule
A successful automation is not one that removes human judgment. It is one that makes the repeatable parts faster while making the remaining human checks visible.
