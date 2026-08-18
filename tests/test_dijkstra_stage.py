from pipeline.stages.dijkstra_stage import DijkstraStage


def test_dijkstra_simple():
    graph = {1: [(2, 1), (3, 4)], 2: [(3, 2)], 3: []}
    stage = DijkstraStage(graph, 1)
    distances = stage.run()
    assert distances == {1: 0.0, 2: 1.0, 3: 3.0}


def test_dijkstra_unreachable():
    graph = {1: [(2, 5)], 2: [], 3: []}
    stage = DijkstraStage(graph, 1)
    distances = stage.run()
    # Node 3 is unreachable and should not appear
    assert 3 not in distances
    assert distances[2] == 5.0
