import pytest
from structures.hash_table import HashTable


@pytest.mark.parametrize("value, expected", [
    ('3120', 6),
    ('777', 56),
    (206, 6)
])
def test_hashing(value, expected):
    hashtable = HashTable()
    assert hashtable.hash(value) == expected


@pytest.mark.parametrize("test_init, expected_value", [
    (('3120', 6), 6),
    (('777', 56), 56),
])
def test_hash_table_insert_lookup(empty_hashtable, test_init,
                                  expected_value):
    key, value = test_init
    empty_hashtable.insert(key, value)
    assert empty_hashtable.lookup(key).value[0].value == expected_value
