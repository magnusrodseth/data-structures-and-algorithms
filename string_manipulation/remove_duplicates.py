def remove_duplicates(string: str) -> str:
    """
    Remove duplicate characters in a string
    :param string:
    :return:
    """
    without_duplicates = ""

    for letter in string:
        if letter not in without_duplicates:
            without_duplicates += letter

    return without_duplicates


if __name__ == '__main__':
    print(remove_duplicates("Hellooo!!"))
