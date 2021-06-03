import pytest
from structures.hash_table import HashTable


@pytest.fixture
def empty_hashtable():
    return HashTable()
