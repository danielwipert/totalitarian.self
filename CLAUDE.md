# CLAUDE.md

This repo holds the essay *The Totalitarian Self* as plain-text documents. The plan is in `planning/SPEC.md`; its §11–14 have live copies elsewhere (see `README.md`), and those copies are the ones to update.

## Sources (the core of the project)

The thesis is unproven; the job is to test it against primary texts, not to confirm it.

- Every claim lives in `planning/claims.md` with an ID (e.g. C4.9).
- **Quote only from a file in `sources/texts/` or a copy in hand, never from memory.** Give the location.
- Tag each passage in `sources/primary/` to claims as **for**, **against** or **complicates**. Look for "against" as hard as "for".
- Never edit `sources/texts/`; corrections go in `sources/primary/`.
- After any new reading, run `python3 tools/check_quotes.py` and read by eye anything scored below 0.85.
- Put quotation marks only around words copied from a text. Paraphrase goes outside quotation marks.
- Conventions: `sources/README.md`.

## Logic gates (how to ask for decisions)

When a path forward needs my decision, don't write one long answer with a big decision at the end.

- Break the decision into small **gates**, one at a time.
- Each gate gives **three clear options**, labeled A, B and C, readable in about one minute.
- Mark the recommended option.
- Keep each option to one or two lines: what it means and what it leads to.
- When there are several gates, show the path first (numbered list, current gate marked).
- After I pick, lock it in with one line, then move to the next gate.
- I may tweak an option ("A, but ..."); restate it and move on.
- When the gates are done, record the decisions in the project's decision log (`planning/decisions.md`).

Full method: `planning/logic-gates.md`.
