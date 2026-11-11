# DocAssistant

A small documentation assistant that answers questions about
*The Swift Programming Language* book and cites the sections it used.
It is the running project behind a series of Medium articles by Muhammad Asher
(https://medium.com/@asherazeem25). Each article builds one part and links to the code here.

## Stack

- Backend: Python + FastAPI
- Docs: [The Swift Programming Language](https://github.com/swiftlang/swift-book) (Apache 2.0),
  downloaded into `data/` (not committed)
- Answers: Claude through the Anthropic API (model chosen on Day 2)
- Search: SQLite + local embeddings, no hosted database
- iOS client: SwiftUI (articles A5 onward); API keys stay on the server

## Layout

```
ingest/   download the docs, split into chunks, build the index   (A1)
app/      FastAPI service: retrieve + answer with citations      (A1, A3)
eval/     the 20-question test set and results                    (A2)
ios/      SwiftUI client                                          (A5)
```

## Setup

Needs [uv](https://docs.astral.sh/uv/) and git.

```
uv sync
uv run python -m ingest.download      # clone the Swift book into data/
uv run python -m ingest.build_index   # chunk + embed locally, about a minute, no API key
uv run python -m ingest.search "How do I capture values in a closure?"
```

For answers (next step): `cp .env.example .env` and add your ANTHROPIC_API_KEY.

Example output: [runs/day2-search.md](runs/day2-search.md).
