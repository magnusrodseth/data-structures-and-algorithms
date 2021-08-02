from typing import List


def count_pairs(array: List[int], difference: int) -> int:
    """
    Given an array of integers, count the number of unique pairs of integers that have a given difference.
    These pairs are stored in a set in order to remove duplicates.
    Time complexity: O(n^2).

    :param array: is the array to count.
    :param difference: is the difference between two elements.
    :return: the number of unique pairs of integers that have a given difference.
    """
    pairs = set()

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] - array[j] == difference:
                pairs.add((array[i], array[j]))

    return len(pairs)


if __name__ == '__main__':
    array = [1, 7, 5, 9, 2, 12, 3]

    pairs_count = count_pairs(array, 2)

    print(pairs_count)
