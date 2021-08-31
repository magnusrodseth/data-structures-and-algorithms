def count_vowels(string: str) -> int:
    """
    Find the number of vowels in a string. Vowels in English are A, E, I, O, U, Y
    :param string:
    :return:
    """
    vowels = "aeiouy"

    counter = 0
    for letter in string.lower():
        if letter in vowels:
            counter += 1

    return counter


if __name__ == '__main__':
    print(count_vowels("hello"))
