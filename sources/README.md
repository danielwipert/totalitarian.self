# Sources

This is where the thesis gets tested. Every claim in `planning/claims.md` should be checked against what the primary texts actually say, including passages that cut against it.

**Weighing sources.** For claims about the culture, sources are weighed in four tiers: established critics and intellectuals (Tier 1), data (Tier 2), institutions (Tier 3), popular carriers (Tier 4). One voice is one among millions: a carrier shows how the Self speaks, not how far it has spread. The full standard is in `planning/claims.md`, "Evidence standard". When a new source file is written, note its tier in the header.

## Folders

| Folder | What goes in it |
|---|---|
| `texts/` | Full primary texts, where they are public domain. Untouched downloads; never edit them. See `texts/README.md` for where each came from. |
| `primary/` | One file per primary work: details about the edition, then the passages we pull, each tagged to claims. |
| `notes/` | Reading notes and secondary literature (historians, commentators). |
| `bibliography.md` | The master list of sources and the role each plays. |

## The rules

1. **Quote from a file, never from memory.** Every quotation in `primary/` is copied from a file in `texts/`, or from a copy of a copyrighted book in front of you, with its page number.
2. **Cite the standard reference first, then this edition.** Section numbers differ between editions (our Locke numbers II.xxvii two higher than the standard Nidditch edition). Give both when they differ.
3. **Look for evidence against the thesis as hard as evidence for it.** An "against" passage is a result, not a problem.
4. **Mark each passage's verdict** for each claim it bears on:
   - **for**: the passage supports the claim as written.
   - **against**: the passage contradicts the claim as written.
   - **complicates**: the passage doesn't refute the claim, but the claim can't stand as written.
5. **Check OCR texts against the scan.** Texts from the Internet Archive are machine-read and contain errors. Fix the quote in `primary/`, never in `texts/`, and mark it `checked against scan`.

## Passage format

Copy this into a `primary/` file for each passage:

```markdown
### author-work.NN · Standard reference — short label

- **Claims:** C4.9 (for), C7.1 (complicates)
- **Location:** this edition's section/page; `texts/filename.txt` line N
- **Checked:** text file / scan / print copy

> The quotation, exactly as in the source.

One or two lines on why it bears on the claim.
```

Find every passage tagged to a claim with: `grep -rn "C4.9" sources/primary/`
