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

```
cp .env.example .env   # then add your ANTHROPIC_API_KEY
```

Further steps are added as each part is built.
