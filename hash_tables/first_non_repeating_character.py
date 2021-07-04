from typing import Dict


def first_non_repeating_character(string: str) -> str or None:
    """
    Finds the first non-repeating character in a string using a hash table (in Python: dictionary).

    :param string: is the string to find the first non-repeating character.
    :return: the first non-repeating character, or None if no characters only occur once.
    """

    string = string.lower()

    character_dict: Dict[str, int] = {}

    for letter in string:
        # Fetch the number of occurrences of this letter if it exists in the dictionary,
        # or 0 if it does not exist
        count = character_dict[letter] if letter in character_dict else 0

        # Set the number of occurrences of given letter
        character_dict[letter] = count + 1

    for letter in string:
        if character_dict[letter] == 1:
            return letter

    return None


if __name__ == '__main__':
    char = first_non_repeating_character("A Green Apple")
    print(char)
