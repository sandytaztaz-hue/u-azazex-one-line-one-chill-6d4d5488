"""One Line, One Chill - entry program.

Writes the single horror sentence to /output/entry.txt.
"""

import os

ENTRY = "My dog has been staring at the corner for an hour, and just now the corner started staring back."

# The entry text is the only output: no title, no extra words, no trailing newline.
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
