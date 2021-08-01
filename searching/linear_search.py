from typing import List


def linear_search(array: List[int], value: int):
    """
    Performs linear search sort on an array, looking for a value.
    :param array: is the array to search.
    :param value: is the value to search for.
    :return: the index of the value, or -1 if it is not found.
    """
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


if __name__ == '__main__':
    array = [2, 34, 56, 34, 5, 65, 42, 3, 6]

    index = linear_search(array, 65)

    print(index)
