import pytest
from algorithms.quicksort import quick_sort


@pytest.mark.parametrize('array, expected', [
    ((4, 3, 5, 2, 1, 3, 2, 3), (1, 2, 2, 3, 3, 3, 4, 5)),
    ([4, 700, 5, 2, 14, 3, 2, 0], [0, 2, 2, 3, 4, 5, 14, 700])
])
def test_quick_sort_different_types(array, expected):
    assert quick_sort(array) == expected
    array_type = type(array)
    assert type(quick_sort(array)) == array_type


def test_quick_sort_with_sorting(create_set):
    assert quick_sort(create_set) == sorted(create_set)
