from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """
    Performs a merge sort on an array.
    :param array: is the array to sort.
    :return: the sorted array.
    """

    # Base case: The sublist cannot be split any more
    if len(array) <= 1:
        return array

    # Split the array in the middle
    middle = len(array) // 2

    left = array[0:middle]
    right = array[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two sublists together, one left and one right.
    Used as implementation detail for the merge_sort method.
    :param left: is the left sublist.
    :param right: is the right sublist.
    :return: the sorted result of these two sublists.
    """

    result: List[int] = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            # Left is now the rest of the left array
            left = left[1:]
        else:
            result.append(right[0])
            # Right is now the rest of the right array
            right = right[1:]

    # Both sublists may still have items left
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]

    return result


if __name__ == '__main__':
    array = [8, 2, 4, 1, 3]
    print(array)

    sorted_array = merge_sort(array)

    print(sorted_array)
