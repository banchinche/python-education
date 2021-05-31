import pytest
from algorithms.binary_search import binary_search


@pytest.mark.parametrize('array, value, expected',
                         [([2, 3, 4, 10, 40], 10, 3),
                          ((2, 5, 6, 9, 40), 9, 3),
                          ((2, 5, 6, 9, 40), 0, 'There is no such element!'),
                          ([2, 3, 4, 10, 40], 2, 0),
                          ((2, 5, 6, 9, 40), 3, 'There is no such element!'),
                          ([2, 3, 4, 10, 40], 3, 1),
                          (range(10), 9, 9),
                          ])
def test_binary_search(array, value, expected):
    assert type(binary_search(array, value)) == int or\
           type(binary_search(array, value)) == str
    assert binary_search(array, value) == expected
