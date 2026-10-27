"""Check that every quotation in sources/primary/ appears in a text in sources/texts/ or sources/excerpts/.

Run from the repo root:

    python3 tools/check_quotes.py

Each blockquote (lines starting with "> ") is split at [...] and other [bracketed]
insertions. Each piece is compared with the texts, ignoring case, punctuation,
spacing and footnote markers like [514] or (1882).

A piece that isn't found exactly gets a closeness score (0 to 1) against the
nearest stretch of text. OCR corrections usually score 0.85 or more; anything
lower is worth reading by eye.
"""
import difflib
import glob
import re
import sys
import unicodedata

MIN_LETTERS = 25  # shorter pieces are too common to test


def letters(s):
    """Lowercase letters and digits only."""
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\[\d+\]|\(\d{3,4}\)", "", s)  # footnote markers
    return re.sub(r"[^a-z0-9]", "", s.lower())


def quotes(md_text):
    """Yield each blockquote in a Markdown file as one string."""
    for block in re.findall(r"(?:^> .*\n?)+", md_text, re.M):
        yield " ".join(line[2:] for line in block.splitlines())


def closeness(piece, texts):
    """Best similarity between piece and any stretch of any text."""
    best = 0.0
    step = max(1, len(piece) // 8)
    for t in texts:
        for k in range(0, len(piece) - 12, step):
            anchor = piece[k:k + 12]
            i = t.find(anchor)
            while i != -1:
                window = t[max(0, i - k - 20): i - k + len(piece) + 20]
                r = difflib.SequenceMatcher(None, piece, window, autojunk=False).ratio()
                best = max(best, r)
                if best > 0.97:
                    return best
                i = t.find(anchor, i + 1)
    return best


def main():
    texts = [letters(open(f, encoding="utf-8").read()) for f in glob.glob("sources/texts/*.txt") + glob.glob("sources/excerpts/*.txt")]
    if not texts:
        sys.exit("No texts found. Run this from the repo root.")

    checked = problems = 0
    for md in sorted(glob.glob("sources/primary/*.md")):
        for q in quotes(open(md, encoding="utf-8").read()):
            for raw in re.split(r"\[[^\]]*\]", q):
                piece = letters(raw)
                if len(piece) < MIN_LETTERS:
                    continue
                checked += 1
                if any(piece in t for t in texts):
                    continue
                score = closeness(piece, texts)
                problems += 1
                flag = "check by eye" if score < 0.85 else "OCR-level difference"
                print(f"{score:.2f}  {flag:20}  {md.split('/')[-1]}  |  {raw.strip()[:70]}")

    print(f"\n{checked} quote pieces checked; {checked - problems} exact; {problems} not exact.")


if __name__ == "__main__":
    main()
