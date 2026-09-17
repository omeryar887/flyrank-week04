# Why this checkpoint is more agentic than FL-06

FL-06 used a fixed sequence: gather, synthesize, draft, review, format. That is a workflow because the path was predetermined.

FL-07 keeps the job narrow but gives the model live tools and lets it decide which workspace files to inspect based on the request. The model can discover files, search for evidence, choose a relevant source, read it, and then decide whether more evidence is needed before finishing.

This does not mean the build is fully autonomous. The scope, tool boundaries, output requirements, and stopping conditions are still defined by the builder. The useful checkpoint is the change from a fixed prompt chain toward model-directed tool use.
