"""Graph Loader Stage

Loads a weighted directed graph from an edge list file.
Each line in the file should contain three values: src dst weight.
The graph is stored as an adjacency list: dict[int, list[tuple[int,float]]].
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

Adjacency = Dict[int, List[Tuple[int, float]]]

class GraphLoader:
    """Stage that reads a graph definition from disk.

    Parameters
    ----------
    path: Path | str
        Path to the edge list file.
    """

    def __init__(self, path: Path | str) -> None:
        self.path = Path(path)

    def load(self) -> Adjacent:
        """Parse the file and return an adjacency list.

        Returns
        -------
        Adjacent
            Mapping of node -> list of (neighbor, weight).
        """
        adjacency: Adjacent = {}
        with self.path.open() as f:
            for line_no, raw in enumerate(f, 1):
                stripped = raw.strip()
                if not stripped or stripped.startswith('#'):
                    continue
                parts = stripped.split()
                if len(parts) != 3:
                    raise ValueError(f"Invalid line {line_no}: '{raw.rstrip()}'")
                src, dst, weight = parts
                src_i = int(src)
                dst_i = int(dst)
                w = float(weight)
                adjacency.setdefault(src_i, []).append((dst_i, w))
                adjacency.setdefault(dst_i, [])  # ensure isolated nodes appear
        return adjacency
