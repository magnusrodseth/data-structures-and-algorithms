from typing import List

from sorting.merge_sort import merge_sort


def binary_search_recursive(array: List[int], value: int) -> int:
    """
    A recursive implementation of binary search.
    :param array: is the array to search.
    :param value: is the value to search for.
    :return: the index of the value
    """
    return _binary_search_recursive(array, value, 0, len(array) - 1)


def _binary_search_recursive(array: List[int], value: int, low: int, high: int) -> int:
    """
    The implementation detail of the recursive implementation of binary search.
    :param array: is the array to search.
    :param value: is the value to search for.
    :param low: is the lower bound of the partition.
    :param high: is the upper bound of the partition.
    :return: the index of the value, or -1 if it doesn't exist.
    """
    if high < low:
        return -1

    middle = (low + high) // 2

    if array[middle] == value:
        return middle
    if value < array[middle]:
        return _binary_search_recursive(array, value, low, middle - 1)
    return _binary_search_recursive(array, value, middle + 1, high)


if __name__ == '__main__':
    # Array must be sorted in order for binary search to work
    array = [21, 4, 6, 3, 24, 56, 78, 765, 432, 1234, 56, 78]

    array = merge_sort(array)
    print(array)

    index = binary_search_recursive(array, 12345)

    print(index)
