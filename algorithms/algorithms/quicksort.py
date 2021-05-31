"""
Module with quick sort realization
"""
from typing import Union


def quick_sort(array: Union[list, tuple]) -> Union[list, tuple]:
    """
    Return sorted list copy of given list/tuple
    :param array: list or tuple
    :return: list or tuple
    """
    def partition(arr, low, high) -> int:
        """
        Sets pivot at the right place and sort this half according to
        element < pivot or element > pivot
        :param arr: half of the array to sort
        :param low: low index of the array
        :param high: high index of the array
        :return: index of the pivot in source array
        """
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if isinstance(array, list):
        new_array = array.copy()
    else:
        new_array = list(array)
    first, last = 0, len(new_array) - 1
    size = last - first + 1
    stack, top = [0] * size,  1
    stack[top - 1], stack[top] = first, last
    while top >= 0:
        last = stack[top]
        top -= 1
        first = stack[top]
        top -= 1
        p = partition(new_array, first, last)
        if p - 1 > first:
            top += 1
            stack[top] = first
            top += 1
            stack[top] = p - 1
        if p + 1 < last:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = last
    if isinstance(array, list):
        return new_array
    else:
        return tuple(new_array)


list1 = [4, 3, 5, 2, 1, 3, 2, 3]
tuple1 = (4, 3, 5, 2, 1, 3, 2, 3)
print(quick_sort(list1))
print(quick_sort(tuple1))
print(tuple1)
