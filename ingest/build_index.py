"""Chunk the book, embed every chunk locally, and save it all in data/index.sqlite."""

import sqlite3
import time
from pathlib import Path

import numpy as np
from fastembed import TextEmbedding

from ingest.chunk import chunk_book

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "index.sqlite"
MODEL = "BAAI/bge-small-en-v1.5"  # small, runs on a laptop CPU, no API key


def main():
    start = time.perf_counter()
    chunks = chunk_book()
    print(f"{len(chunks)} chunks from the book")

    model = TextEmbedding(MODEL)
    # Embed the chapter and section names with the text, so headings help matching.
    inputs = [f"{c.chapter} > {c.section}\n\n{c.text}" for c in chunks]
    vectors = np.array(list(model.embed(inputs)), dtype=np.float32)

    DB_PATH.unlink(missing_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.execute(
        "CREATE TABLE chunks (id TEXT PRIMARY KEY, chapter TEXT, section TEXT,"
        " url TEXT, text TEXT, embedding BLOB)"
    )
    db.executemany(
        "INSERT INTO chunks VALUES (?, ?, ?, ?, ?, ?)",
        [(c.id, c.chapter, c.section, c.url, c.text, v.tobytes()) for c, v in zip(chunks, vectors)],
    )
    db.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT)")
    db.execute("INSERT INTO meta VALUES ('model', ?)", (MODEL,))
    db.commit()
    db.close()

    size_mb = DB_PATH.stat().st_size / 1e6
    print(f"Saved {DB_PATH.name} ({size_mb:.1f} MB) in {time.perf_counter() - start:.0f}s")


if __name__ == "__main__":
    main()
