from typing import List


def quick_sort(array: List[int], low: int, high: int):
    """
    Performs a quick_sort sort on the array.
    :param array: is the array to sort.
    :param low: is the lower bound of the partition.
    :param high: is the higher bound of the partition.
    """
    if low >= 0 and high >= 0:
        if low < high:
            # Find index of pivot item
            pivot = partition(array, low, high)

            # Quick sort left and right partitions
            quick_sort(array, low, pivot - 1)
            quick_sort(array, pivot + 1, high)


def partition(array: List[int], low: int, high: int) -> int:
    """
    Gets the index of the pivot item in a partition.
    :param array: is the array to sort.
    :param low: is the lower bound of the partition.
    :param high: is the higher bound of the partition.
    :return: the index of the pivot item.
    """
    # Get last item of array
    pivot = array[high]

    # Marks the boundary of partitions
    boundary = low - 1

    for i in range(low, high):
        # If current value is less than or equal to pivot value, swap it
        if array[i] <= pivot:
            boundary += 1
            swap(array, boundary, i)

    swap(array, boundary + 1, high)

    return boundary + 1


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
    array = [15, 6, 3, 1, 22, 10, 13]
    print(array)

    quick_sort(array, 0, len(array) - 1)

    print(array)
