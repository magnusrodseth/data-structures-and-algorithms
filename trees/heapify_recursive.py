from typing import List


def swap(numbers: List[int], first: int, second: int):
    """
    Swaps two items in a list of numbers.
    :param numbers: is the list of numbers
    :param first: is the first index.
    :param second: is the second index.
    """
    placeholder = numbers[first]
    numbers[first] = numbers[second]
    numbers[second] = placeholder


def _heapify(numbers: List[int], index: int) -> None:
    """
    The implementation detail of converting a list of numbers into a heap recursively in-place.

    :param numbers: is the list of numbers to convert.
    :param index: is the current index.
    """
    # Assume the provided index is the grater index, and then compare later
    larger_index = index

    # Validate left index
    left_index = (index * 2) + 1
    if (left_index < len(numbers)) and (numbers[left_index] > numbers[larger_index]):
        larger_index = left_index

    # Validate right index
    right_index = (index * 2) + 2
    if (right_index < len(numbers)) and (numbers[right_index] > numbers[larger_index]):
        larger_index = right_index

    # Item is in the correct place
    if index == larger_index:
        return

    swap(numbers, index, larger_index)

    # Recursively determine the correct index for each item
    _heapify(numbers, larger_index)


def get_last_parent_index(numbers: List[int]) -> int:
    """
    Gets the last parent index of a list of numbers to convert into a heap.

    The reason we do this is to optimize the algorithm.
    There is no need to recursively call _heapify through the whole list of numbers.
    Rather, we only need to iterate up to the last parent index.

    :param numbers: is the list of numbers.
    :return: the index of the last parent node.
    """
    return (len(numbers) // 2) - 1


def heapify(numbers: List[int]) -> None:
    """
    Converts an array of numbers into a max heap in-place.

    :raise AttributeError: if the list is empty.
    :param numbers: is the list of numbers to convert into a heap.
    """
    if len(numbers) == 0:
        raise AttributeError("List is empty.")

    # See method documentation for get_last_parent_index for the reason why we iterate this way.
    for i in range(get_last_parent_index(numbers), -1, -1):
        _heapify(numbers, i)


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 1, 2]

    heapify(numbers)

    print(numbers)
