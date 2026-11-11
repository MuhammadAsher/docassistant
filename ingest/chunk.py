"""Split the Swift book's Markdown into chunks that each know where they came from.

One chunk = one section (## or ### heading) of one chapter. Long sections are split
at paragraph breaks, never inside a code block. Each chunk keeps its chapter, section
and a link to the matching page on docs.swift.org, so answers can cite it later.
"""

import re
from dataclasses import dataclass
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "data" / "swift-book" / "TSPL.docc"
DOCS_URL = "https://docs.swift.org/swift-book/documentation/the-swift-programming-language"
MAX_CHARS = 1500  # long sections are split near this size

COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)  # the book's hidden test code
HEADING = re.compile(r"^(#{1,3}) (.+)$")


@dataclass
class Chunk:
    id: str
    chapter: str
    section: str
    url: str
    text: str


def anchor(heading: str) -> str:
    # docs.swift.org anchors look like "Closure-Expressions"
    return re.sub(r"[^A-Za-z0-9]+", "-", heading).strip("-")


def split_long(text: str) -> list[str]:
    """Split at blank lines outside code fences, keeping parts under MAX_CHARS where possible."""
    if len(text) <= MAX_CHARS:
        return [text]
    blocks, current, in_code = [], [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if not line.strip() and not in_code:
            blocks.append("\n".join(current))
            current = []
        else:
            current.append(line)
    blocks.append("\n".join(current))

    parts, part = [], ""
    for block in filter(str.strip, blocks):
        if part and len(part) + len(block) > MAX_CHARS:
            parts.append(part)
            part = ""
        part = f"{part}\n\n{block}" if part else block
    if part:
        parts.append(part)
    return parts


def chunk_file(path: Path) -> list[Chunk]:
    text = COMMENT.sub("", path.read_text(encoding="utf-8"))
    page = f"{DOCS_URL}/{path.stem.lower()}"
    chapter, section, buf, sections = path.stem, "", [], []

    def flush():
        body = "\n".join(buf).strip()
        if body:
            sections.append((section, body))
        buf.clear()

    for line in text.splitlines():
        m = HEADING.match(line)
        if m and len(m.group(1)) == 1:
            chapter = m.group(2).strip()
        elif m:
            flush()
            section = m.group(2).strip()
        else:
            buf.append(line)
    flush()

    chunks = []
    for section_name, body in sections:
        url = f"{page}#{anchor(section_name)}" if section_name else page
        for i, part in enumerate(split_long(body)):
            chunk_id = f"{path.stem}/{anchor(section_name) or 'intro'}/{i}"
            chunks.append(Chunk(chunk_id, chapter, section_name or chapter, url, part))
    return chunks


def chunk_book() -> list[Chunk]:
    files = sorted(BOOK_DIR.rglob("*.md"))
    if not files:
        raise SystemExit(f"No Markdown found in {BOOK_DIR}. Run: python -m ingest.download")
    return [c for f in files for c in chunk_file(f)]
