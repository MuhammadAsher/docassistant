"""Download The Swift Programming Language book (Apache 2.0) into data/swift-book."""

import subprocess
from pathlib import Path

REPO = "https://github.com/swiftlang/swift-book"
DEST = Path(__file__).resolve().parent.parent / "data" / "swift-book"

if DEST.exists():
    print(f"Already downloaded: {DEST}")
else:
    subprocess.run(["git", "clone", "--depth", "1", REPO, str(DEST)], check=True)
commit = subprocess.run(
    ["git", "-C", str(DEST), "log", "-1", "--format=%h %cs"],
    capture_output=True, text=True, check=True,
).stdout.strip()
print(f"Swift book at commit {commit}")
