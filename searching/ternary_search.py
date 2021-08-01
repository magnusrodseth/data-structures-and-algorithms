from typing import List

from sorting.merge_sort import merge_sort


def ternary_search(array: List[int], value: int) -> int:
    """
    A recursive implementation of ternary search.
    :param array: is the array to search.
    :param value: is the value to search for.
    :return: the index of the value
    """
    return _ternary_search(array, value, 0, len(array) - 1)


def _ternary_search(array: List[int], value, low: int, high: int) -> int:
    """
    The implementation detail of the recursive implementation of ternary search.
    :param array: is the array to search.
    :param value: is the value to search for.
    :param low: is the lower bound of the partition.
    :param high: is the upper bound of the partition.
    :return: the index of the value, or -1 if it doesn't exist.
    """
    if high < low:
        return -1

    # Ternary search has two middle pointers.
    partition_size = (high - low) // 3

    middle_1 = low + partition_size
    middle_2 = high - partition_size

    if value == array[middle_1]:
        return middle_1
    if value == array[middle_2]:
        return middle_2
    if value < array[middle_1]:
        return _ternary_search(array, value, low, middle_1 - 1)
    if value > array[middle_2]:
        return _ternary_search(array, value, middle_2 + 1, high)

    return _ternary_search(array, value, middle_1 + 1, middle_2 - 1)


if __name__ == '__main__':
    # Array must be sorted in order for binary search to work
    array = [21, 4, 6, 3, 24, 56, 78, 765, 432, 1234, 56, 78]

    array = merge_sort(array)
    print(array)

    index = ternary_search(array, 24)
    print(index)
