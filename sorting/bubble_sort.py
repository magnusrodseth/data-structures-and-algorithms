from typing import List


def bubble_sort(array: List[int]):
    """
    Performs a bubble sort on the array.
    :param array: is the array to sort.
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                swap(array, j + 1, j)


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

    bubble_sort(array)

    print(array)
