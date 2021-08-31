from typing import Dict


def most_repeated_character(string: str) -> str:
    """
    Find the most repeated character in a string.
    :param string:
    :return:
    """
    map: Dict[str, int] = {}

    for letter in string:
        if letter not in map:
            map[letter] = 1
        else:
            map[letter] += 1

    return sorted(map.items(), key=lambda item: item[1], reverse=True)[0][0]


if __name__ == '__main__':
    print(most_repeated_character("Hellooo!!"))
