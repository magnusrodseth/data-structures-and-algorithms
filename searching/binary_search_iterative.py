from typing import List

from sorting.merge_sort import merge_sort


def binary_search_iterative(array: List[int], value: int) -> int:
    """
    An iterative implementation of binary search.
    :param array: is the array to search.
    :param value: is the value to search for.
    :return: the index of the value, or -1 if it does not exist.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2

        if array[middle] == value:
            return middle
        if array[middle] < value:
            low = middle + 1
        if array[middle] > value:
            high = middle + -1

    return -1


if __name__ == '__main__':
    # Array must be sorted in order for binary search to work
    array = [21, 4, 6, 3, 24, 56, 78, 765, 432, 1234, 56, 78]

    array = merge_sort(array)
    print(array)

    index = binary_search_iterative(array, 78)

    print(index)
