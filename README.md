# Dijkstra Pipeline Utility
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

A tiny staged processing pipeline that loads a weighted directed graph, runs Dijkstra's algorithm using a binary heap, and formats the shortest‑path results.

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Analysis Document](#analysis-document)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

## Overview
The library is organized as a three‑stage pipeline under `pipeline/stages/`:
1. **GraphLoader** – reads an edge list file into an adjacency list.
2. **DijkstraStage** – computes shortest distances from a source node using a binary heap.
3. **ResultFormatter** – turns the distance map into a sorted, human‑readable string.
The `pipeline/orchestrator.py` wires these stages together.

## Tech Stack
- Python 3.9+
- Standard library only (`heapq`, `pathlib`, `typing`)
- `pytest` for the test suite

## Architecture
```text
pipeline/
├─ stages/
│  ├─ graph_loader.py      # Load graph from file
│  ├─ dijkstra_stage.py    # Core algorithm with binary heap
│  └─ result_formatter.py # Human‑readable output
└─ orchestrator.py          # Pipeline façade
```
The data flows linearly from left to right.

## Theoretical Background
Dijkstra's algorithm finds the shortest path from a single source to all other vertices in a weighted graph with non‑negative edge costs. The classic implementation uses a priority queue to repeatedly extract the vertex with the smallest tentative distance. By employing a binary heap (Python's `heapq`), each `push` and `pop` operation runs in O(log V) time, yielding an overall complexity of O((E+V) log V) for sparse graphs.

The binary heap is an array‑based structure where the parent of index `i` resides at `(i‑1)//2`. Insertion appends the new element and percolates it up; extraction swaps the root with the last element, removes it, and percolates the new root down. This implementation relies on `heapq.heappush` and `heapq.heappop`, which encapsulate those mechanics.

Separating the algorithm into a dedicated stage improves testability and reusability. The loader stage validates input format, the algorithm stage focuses purely on computation, and the formatter stage handles presentation concerns without side effects.

## Installation
```bash
git clone https://github.com/yourorg/dijkstra-pipeline.git
cd dijkstra-pipeline
pip install -r requirements.txt
```
*(No external dependencies beyond the standard library; `requirements.txt` is provided for future extensions.)*

## Usage
```python
from pipeline.orchestrator import DijkstraPipeline

pipeline = DijkstraPipeline('path/to/edges.txt', source=1)
print(pipeline.run())
```
The example script `examples/run_pipeline.py` demonstrates a full end‑to‑end run with a temporary graph file.

## API Reference
- `class GraphLoader(path: Path|str)`
  - `load() -> Adjacent`: Returns adjacency list.
- `class DijkstraStage(adjacency: Adjacent, source: int)`
  - `run() -> dict[int, float]`: Shortest distances.
- `class ResultFormatter(distances: dict[int, float])`
  - `format() -> str`: Sorted multiline string.
- `class DijkstraPipeline(graph_path: Path|str, source: int)`
  - `run() -> str`: Executes all stages and returns formatted output.

## Analysis Document
Further performance notes are in [docs/analysis.md](docs/analysis.md).

## Testing
```bash
pytest -q
```
The suite includes unit tests for the loader and the Dijkstra stage, covering normal operation and malformed input handling.

## Limitations
- Only supports directed graphs with non‑negative weights.
- Unreachable nodes are omitted from the output rather than shown with `inf`.
- Graph must fit in memory; no streaming support.

## Roadmap
- Add support for undirected graphs via a flag.
- Emit `inf` for unreachable vertices.
- Provide a streaming loader for very large edge lists.

## License
MIT License
