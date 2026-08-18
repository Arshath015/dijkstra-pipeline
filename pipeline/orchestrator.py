"""Pipeline Orchestrator

Coordinates the three stages: loading, computation, and formatting.
"""

from __future__ import annotations

from pathlib import Path

from .stages.graph_loader import GraphLoader
from .stages.dijkstra_stage import DijkstraStage
from .stages.result_formatter import ResultFormatter

class DijkstraPipeline:
    """High‑level façade for the staged Dijkstra pipeline.

    Parameters
    ----------
    graph_path: Path | str
        Path to the edge list file.
    source: int
        Source node for shortest‑path computation.
    """

    def __init__(self, graph_path: Path | str, source: int) -> None:
        self.graph_path = Path(graph_path)
        self.source = source

    def run(self) -> str:
        """Execute the pipeline and return the formatted result string."""
        loader = GraphLoader(self.graph_path)
        adjacency = loader.load()
        dijkstra = DijkstraStage(adjacency, self.source)
        distances = dijkstra.run()
        formatter = ResultFormatter(distances)
        return formatter.format()
