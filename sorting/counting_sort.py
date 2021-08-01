from typing import List


def counting_sort(array: List[int]):
    """
    Performs a counting sort on an array.
    :param array: is the array to sort.
    """
    if len(array) == 0:
        return

    # Each index corresponds to a value in the array.
    # Its value holds the frequency of the value in the array.
    frequency = [0 for _ in range(0, max(array) + 1)]

    for item in array:
        frequency[item] += 1

    # Iterate over frequency and overwrite values in the original array based on their frequency
    count = 0
    for i in range(len(frequency)):
        for j in range(frequency[i]):
            array[count] = i
            count += 1


if __name__ == '__main__':
    array = [5, 3, 2, 5, 4, 4, 5]
    print(array)

    counting_sort(array)

    print(array)
