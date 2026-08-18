"""Result Formatter Stage

Converts the raw distance dictionary into a human‑readable string.
"""

from __future__ import annotations

from typing import Dict

class ResultFormatter:
    """Stage that formats Dijkstra output.

    Parameters
    ----------
    distances: Dict[int, float]
        Mapping of node to shortest distance.
    """

    def __init__(self, distances: Dict[int, float]) -> None:
        self.distances = distances

    def format(self) -> str:
        """Return a sorted, multiline string of distances.

        Nodes are listed in ascending order. Distance is shown with two
        decimal places.
        """
        lines = []
        for node in sorted(self.distances):
            lines.append(f"{node}: {self.distances[node]:.2f}")
        return "\n".join(lines)
