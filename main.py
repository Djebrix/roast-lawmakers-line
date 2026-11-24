"""One satirical sentence roasting lawmakers who regulate AI but cannot convert a file to PDF."""

import os

LINE = "The senator who just wrote a 400-page law governing artificial intelligence still forwards his .docx to an aide with the subject line 'please make PDF'."

assert 1 <= len(LINE) <= 320, f"line is {len(LINE)} chars"
assert LINE.strip() == LINE and LINE.strip()
# Exactly one sentence: ends with one period, no ". " mid-sentence, no ! or ?.
# (The period inside ".docx" is followed by a letter, not a space, so it is not a sentence break.)
assert LINE.endswith(".") and LINE.count(". ") == 0 and "!" not in LINE and "?" not in LINE, "must be exactly one sentence"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
