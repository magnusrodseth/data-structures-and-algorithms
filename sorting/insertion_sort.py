from typing import List


def insertion_sort(array: List[int]):
    """
    Performs an insertion sort on an array.
    :param array: is the array to sort.
    """
    for i in range(1, len(array)):
        current = array[i]

        j = i - 1

        # While j is within bounds and current should be shifted
        while j >= 0 and array[j] > current:
            # "Shift" the items to the right
            # Note that what we're really doing is copying values
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current


if __name__ == '__main__':
    array = [8, 2, 4, 1, 3]
    print(array)

    insertion_sort(array)

    print(array)
