import pytest


@pytest.mark.parametrize("edge, connected, expected", [
    (1, [], []),
    (2, [1], 1),
    (3, [2], 2),
    (4, [1], 1),
    (5, [2], 2),
])
def test_graph_insert(empty_graph, edge, connected, expected):
    empty_graph.insert(edge, connected)
    for vertex in empty_graph.lookup(edge).adjacency_list:
        assert vertex.value == expected
