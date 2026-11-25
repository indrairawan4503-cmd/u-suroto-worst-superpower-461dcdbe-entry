#!/usr/bin/env python3
"""Worst Superpower (variant A): perfect knowledge of the past, always right
and always too late. One concrete scene, one surprising turn, one sentence."""

ENTRY = "I predict last night's lottery numbers with perfect accuracy - the numbers arrive the second my ticket expires, and I am never wrong."

def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
