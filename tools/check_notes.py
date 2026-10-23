"""Find quoted phrases in the notes that don't appear in any text.

Run from the repo root:

    python3 tools/check_notes.py

check_quotes.py checks the blockquotes. This script checks everything else:
the commentary under each passage, and planning/claims.md and status.md.
Any phrase of four or more words inside "double quotes" should be copied
from a text. A phrase listed here is one of:

- fine: a quote of our own spec or claims, a title, or a note saying a
  phrase is *not* in the text;
- fine but worth a look: words in a badly scanned (OCR) text;
- a problem: a translation or paraphrase inside quotation marks. Move the
  quotation marks to the source's own words, or drop them.
"""
import glob
import re
import unicodedata


def letters(s):
    s = unicodedata.normalize("NFKC", s)  # also turns the long s into s
    s = re.sub(r"\[\d+\]|\(\d{3,4}\)", "", s)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main():
    texts = [letters(open(f, encoding="utf-8").read()) for f in glob.glob("sources/texts/*.txt")]
    ours = letters("".join(open(f, encoding="utf-8").read() for f in ["planning/SPEC.md", "planning/claims.md"]))
    files = sorted(glob.glob("sources/primary/*.md")) + ["planning/claims.md", "planning/status.md"]

    total = flagged = 0
    for f in files:
        for line in open(f, encoding="utf-8").read().splitlines():
            if line.startswith((">", "- **Checked", "- **Location", "| 2026")):
                continue
            line = line.replace("“", '"').replace("”", '"')
            for q in re.findall(r'"([^"]*)"', line):
                if q.count(" ") < 3:
                    continue
                parts = [letters(x) for x in re.split(r"\[\.\.\.\]|\.\.\.|\[[^\]]*\]|…", q)]
                parts = [x for x in parts if len(x) > 10]
                if not parts:
                    continue
                total += 1
                if all(any(x in t for t in texts) for x in parts):
                    continue
                if f.startswith("sources") and all(x in ours for x in parts):
                    continue
                flagged += 1
                print(f"{f.split('/')[-1]}  |  {q[:110]}")

    print(f"\n{total} quoted phrases in notes; {flagged} not found in any text.")


if __name__ == "__main__":
    main()
