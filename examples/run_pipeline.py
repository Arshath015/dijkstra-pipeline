"""Demo script executing the Dijkstra pipeline.

It creates a temporary edge list, runs the pipeline, and prints the result.
"""

import pathlib
import tempfile

from pipeline.orchestrator import DijkstraPipeline


def main() -> None:
    edge_data = """1 2 2.5\n2 3 1.0\n1 3 5.0\n3 4 2.2\n"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as f:
        f.write(edge_data)
        graph_path = pathlib.Path(f.name)
    pipeline = DijkstraPipeline(graph_path, source=1)
    result = pipeline.run()
    print("Shortest distances from node 1:\n" + result)


if __name__ == "__main__":
    main()
