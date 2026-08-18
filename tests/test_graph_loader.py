import pathlib
import tempfile

from pipeline.stages.graph_loader import GraphLoader


def test_loader_basic():
    data = """# simple graph\n1 2 1.5\n2 3 2.0\n3 1 4.0\n"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as f:
        f.write(data)
        f_path = pathlib.Path(f.name)
    loader = GraphLoader(f_path)
    adj = loader.load()
    assert adj[1] == [(2, 1.5), (3, 4.0)]
    assert adj[2] == [(1, 1.5), (3, 2.0)]
    assert adj[3] == [(2, 2.0), (1, 4.0)]


def test_loader_invalid_line():
    data = """1 2\n"""
    with tempfile.NamedTemporaryFile('w+', delete=False) as f:
        f.write(data)
        f_path = pathlib.Path(f.name)
    loader = GraphLoader(f_path)
    try:
        loader.load()
    except ValueError as e:
        assert "Invalid line" in str(e)
    else:
        assert False, "Expected ValueError for malformed line"
