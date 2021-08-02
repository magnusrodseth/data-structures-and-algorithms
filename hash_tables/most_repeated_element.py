def most_repeated_element(array):
    """
    Fins the most repeated element and its frequency in an array using a hash table.
    Time complexity: O(n + m).

    :param array: is the array to find the most repeated element in.
    :return: a tuple containing the most repeated element and its frequency.
    """
    table = {}

    for item in array:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1

    (most_repeated_key, most_repeated_value) = (array[0], table[array[0]])
    for key in table:
        if table[key] > most_repeated_value:
            (most_repeated_key, most_repeated_value) = key, table[key]

    return most_repeated_key, most_repeated_value


if __name__ == '__main__':
    array = [1, 2, 2, 3, 3, 3, 3, 3, 4]

    element, frequency = most_repeated_element(array)

    print(f'element: %s frequency: %s' % (element, frequency))
