# The Totalitarian Self

A diagnosis of the Western Self in its calcified, American form.

This repository holds the essay and its planning material as plain-text documents ("docs as code").

## Layout

```
planning/
  SPEC.md            the specification (kept whole as the reference)
  claims.md          every claim in the thesis, numbered, with its test status
  decisions.md       decision log (live copy of SPEC §12)
  open-questions.md  open questions (live copy of SPEC §14)
  logic-gates.md     how decisions are made: small A/B/C gates
  status.md          where the argument stands: one-page summary
essay/               the essay, one file per section, in reading order
  00-introduction.md ... 07-objections.md
sources/
  README.md          how sources are collected and tagged
  bibliography.md    sources and lineage (live copy of SPEC §13)
  to-pull.md         master list of sources still to pull, in order
  texts/             full public-domain primary texts (never edited)
  primary/           one file per primary work: passages tagged to claims
  notes/             reading notes and secondary literature
deferred/
  cures.md           out-of-scope material (live copy of SPEC §11)
tools/
  check_quotes.py    checks every quote in sources/primary/ against the texts
  check_notes.py     checks quoted phrases in the notes against the texts
CLAUDE.md            working rules Claude reads at the start of each session
```
