import pytest
from structures.hash_table import HashTable
from structures.graph import Graph


@pytest.fixture
def empty_hashtable():
    return HashTable()


@pytest.fixture
def empty_graph():
    return Graph()
