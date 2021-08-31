def reverse_string(string: str) -> str:
    """
    Reverse a string.
    :param string:
    :return:
    """
    reversed = ""

    for i in range(len(string) - 1, -1, -1):
        reversed += string[i]

    return reversed


if __name__ == "__main__":
    print(reverse_string("hello"))
