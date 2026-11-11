"""Find the book sections closest to a question.

    python -m ingest.search "How do I capture values in a closure?"
"""

import sqlite3
import sys
from dataclasses import dataclass

import numpy as np
from fastembed import TextEmbedding

from ingest.build_index import DB_PATH


@dataclass
class Hit:
    score: float
    chapter: str
    section: str
    url: str
    text: str


class Index:
    def __init__(self):
        if not DB_PATH.exists():
            raise SystemExit("No index yet. Run: python -m ingest.build_index")
        db = sqlite3.connect(DB_PATH)
        model_name = db.execute("SELECT value FROM meta WHERE key = 'model'").fetchone()[0]
        rows = db.execute("SELECT chapter, section, url, text, embedding FROM chunks").fetchall()
        db.close()
        self.rows = [r[:4] for r in rows]
        self.vectors = np.stack([np.frombuffer(r[4], dtype=np.float32) for r in rows])
        self.model = TextEmbedding(model_name)

    def search(self, question: str, k: int = 5) -> list[Hit]:
        q = next(iter(self.model.query_embed(question)))
        # Vectors are normalised, so the dot product is cosine similarity.
        scores = self.vectors @ q
        best = np.argsort(-scores)[:k]
        return [Hit(float(scores[i]), *self.rows[i]) for i in best]


def main():
    question = " ".join(sys.argv[1:]) or "How do I capture values in a closure?"
    print(f"Q: {question}\n")
    for n, hit in enumerate(Index().search(question), 1):
        preview = " ".join(hit.text.split())[:160]
        print(f"{n}. [{hit.score:.3f}] {hit.chapter} > {hit.section}")
        print(f"   {hit.url}")
        print(f"   {preview}...\n")


if __name__ == "__main__":
    main()
