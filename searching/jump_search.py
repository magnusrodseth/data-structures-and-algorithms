import math
from typing import List


def jump_search(array: List[int], value: int) -> int:
    """
    Performs a jump search on a list of integers.
    :param array: is the array to search.
    :param value: is the value to search.
    :return: the index of the value, or -1 if it doesn't exist.'
    """
    if len(array) == 0:
        return -1
    block_size = get_block_size(array)

    # Pointers for traversing the array
    start_pointer = 0
    next_pointer = block_size

    while (start_pointer < len(array)) and (array[next_pointer - 1] < value):
        start_pointer = next_pointer
        next_pointer += block_size

        # Prevent next from going out of bounds
        if next_pointer > len(array):
            next_pointer = len(array)

    # Linear search through the relevant block
    for i in range(start_pointer, next_pointer):
        if array[i] == value:
            return i

    return -1


def get_block_size(array: List[int]) -> int:
    """
    Gets the block size of an array for jump search.
    The block size is the square root of the length of the array.

    We then calculate the absolute value of this block size, because we're using the value as
    index pointer, and negative values do not make sense here.

    This value is then floored to act as index pointer in the array.
    :param array: is the array to search.
    :return: the block size to be used in jump search.
    """
    return math.floor(abs(math.sqrt(len(array))))


if __name__ == '__main__':
    # Array must be sorted in order for binary search to work
    array = [3, 5, 6, 9, 11, 18, 20, 21, 24, 30]
    print(array)

    index = jump_search(array, 31)

    print(index)
