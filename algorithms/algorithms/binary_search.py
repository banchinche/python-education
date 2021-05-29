"""
Module with binary search realization
"""
from typing import Sequence, Union


def binary_search(sequence: Sequence, value: int) -> Union[int, str]:
    """
    Returns index of the first value occurrence in sequence
    :param sequence: source sequence where to find
    :param value: value to find
    :return: index of the value in sequence
    """
    first, last = 0, len(sequence) - 1
    while first <= last:
        middle = (last + first) // 2
        if sequence[middle] < value:
            first = middle + 1
        elif sequence[middle] > value:
            last = middle - 1
        else:
            return middle
    return 'There is not such element!'


arr = [2, 3, 4, 10, 40]
tup2 = (2, 5, 6, 9, 40)
ran1 = range(10)
x = 10
print(binary_search(arr, x))
print(binary_search(tup2, 9))
print(binary_search(tup2, 0))
print(binary_search(arr, 2))
print(binary_search(tup2, 3))
print(binary_search(arr, 3))
print(binary_search(ran1, 9))
