from typing import List

from searching.binary_search_recursive import _binary_search_recursive


def exponential_search(array: List[int], value: int) -> int:
    """
    Performs an exponential search on an array of integers.
    :param array: is the array to search.
    :param value: is the value to search for.
    :return: the index of the value, or -1 if the value does not exist.
    """
    bound = 1

    while (bound < len(array)) and (array[bound] < value):
        bound *= 2

    low = bound // 2
    high = min(bound, len(array) - 1)

    return _binary_search_recursive(array, value, low, high)


if __name__ == '__main__':
    # Array must be sorted in order for binary search to work
    array = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30]
    print(array)

    index = exponential_search(array, 5)

    print(index)
