from typing import List


def two_sum(array: List[int], target: int) -> List[int] or None:
    """
    Given an array of integers,
    return indices of the two numbers such that they add up to a specific target.
    Assume that each input has exactly one solution, and you may not use the same element twice.
    Time complexity: O(n).

    :param array: is the array to iterate over
    :param target: is the target difference.
    :return: a list of indices of the two numbers such that they add up to a specific target,
    or None if it doesn't exist..
    """
    table = {}

    for i in range(len(array)):
        difference = target - array[i]
        if difference in table:
            return [table[difference], i]
        table[array[i]] = i

    return None


if __name__ == '__main__':
    array = [2, 7, 11, 15]

    result = two_sum(array, 9)
    print(result)
