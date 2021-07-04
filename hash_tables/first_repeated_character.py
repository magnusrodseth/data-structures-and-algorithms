from typing import Set


def first_repeated_character(string: str) -> str or None:
    """
    Finds the first repeated character in a string using a set.

    :param string: is the string to find the first repeating character.
    :return: the first repeating character, or None if no characters occurs several times.
    """

    string = string.lower()

    # Initialize set. Even if we pass in an empty string (""), we return None.
    character_set: Set[str] = {""}

    for letter in string:
        # We have a duplicate value
        if letter in character_set:
            return letter
        # We do not have a duplicate value
        else:
            character_set.add(letter)

    return None


if __name__ == '__main__':
    chr = first_repeated_character("green apple")
    print(chr)
