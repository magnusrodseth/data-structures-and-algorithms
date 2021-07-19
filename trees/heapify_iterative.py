from typing import List


def get_max_item(numbers: List[int], first: int, second: int) -> (int, int):
    """
    Gets the maximum value and corresponding index between two items in a given array.

    :param numbers: is the array of items.
    :param first: is the first item to compare.
    :param second: is the second item to compare.
    :return: a tuple representation of the greater item with the structure: (value, index)
    """
    return (first, numbers.index(first)) \
        if first > second \
        else (second, numbers.index(second))


def heapify(numbers: List[int]) -> None:
    """
    Converts an array of numbers into a max heap in-place.

    :raise AttributeError: if the list is empty.
    :param numbers: is the list of numbers to convert into a heap.
    """
    if len(numbers) == 0:
        raise AttributeError("Cannot heapify an empty list.")

    for i in range(len(numbers) - 2):
        current = numbers[i]
        left_child, right_child = numbers[i + 1], numbers[i + 2]

        if current < left_child or current < right_child:
            # Bubble item to correct index
            max_child, max_child_index = get_max_item(numbers, left_child, right_child)
            numbers[max_child_index] = current
            numbers[i] = max_child


if __name__ == '__main__':
    numbers = [5, 3, 8, 4, 1, 2]

    heapify(numbers)

    print(numbers)
