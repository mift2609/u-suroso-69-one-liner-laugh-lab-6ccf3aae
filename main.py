"""One-Liner Laugh Lab — a robot vacuum's excuse after eating a sock."""

import os

LINE = "I didn't eat your sock — I was just giving it the deep clean it clearly needed after living under your bed for a month."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written entry does not match"
    assert written.strip() == LINE, "written entry is not a single line"
    print(written.strip())
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
