from typing import List


def selection_sort(array: List[int]):
    """
    Performs a selection sort on an array.
    :param array: is the array to sort.
    """
    for i in range(len(array)):
        # Stores the index of the current pass' minimum value.
        # Assume the minimum value is the first value
        min_index = i

        # Test against items after i to find the minimum value
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                # We found a new minimum value, and store its index
                min_index = j

        # If we found a new minimum value, swap them
        if array[min_index] != array[i]:
            swap(array, i, min_index)


def swap(array: List[int], first: int, second: int):
    """
    Swaps two items in an array.
    :param array: is the array to swap items in.
    :param first: is the index of the first item.
    :param second: is the index of the second item.
    """
    temp = array[first]
    array[first] = array[second]
    array[second] = temp


if __name__ == '__main__':
    array = [5, 12, 1, 37, 9, 83, 1, 4, 689, 7, 421]
    print(array)

    selection_sort(array)

    print(array)
