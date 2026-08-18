"""Dijkstra Stage

Executes Dijkstra's algorithm on a graph using a binary heap.
The stage receives an adjacency list and a source node, and returns a dict of
shortest distances.
"""

from __future__ import annotations

import heapq
from typing import Dict, List, Tuple

Adjacency = Dict[int, List[Tuple[int, float]]]

class DijkstraStage:
    """Stage that computes shortest paths.

    Parameters
    ----------
    adjacency: Adjacent
        Graph adjacency list.
    source: int
        Starting node for the algorithm.
    """

    def __init__(self, adjacency: Adjacent, source: int) -> None:
        self.graph = adjacency
        self.source = source

    def run(self) -> Dict[int, float]:
        """Return a mapping node -> shortest distance from source.

        Uses a binary heap (heapq) for the priority queue.
        Unreachable nodes are omitted from the result.
        """
        dist: Dict[int, float] = {self.source: 0.0}
        visited: set[int] = set()
        heap: List[Tuple[float, int]] = [(0.0, self.source)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in self.graph.get(node, []):
                nd = d + weight
                if neighbor not in dist or nd < dist[neighbor]:
                    dist[neighbor] = nd
                    heapq.heappush(heap, (nd, neighbor))
        return dist
