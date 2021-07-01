from typing import List


def reverse_string(string: str) -> str:
    """
    Reverses a string using a stack.

    :param string: is the string to be reversed.
    :raise AttributeError: if the input is None.
    :return: is the reversed string.
    """
    if string is None:
        raise AttributeError("The input cannot be null.")

    stack: List[str] = []

    for letter in string:
        stack.append(letter)

    reversed = ""

    while not is_empty(stack):
        reversed += stack.pop()

    return reversed


def is_empty(stack: List[str]) -> bool:
    """
    Check if a stack is empty.
    We add this custom method, as Python does not have a built-in is_empty() method.

    :param stack: is the stack to inspect.
    :return: a boolean value determining whether the stack is empty or not.
    """
    return len(stack) == 0


if __name__ == '__main__':
    print(reverse_string("Hello, world!"))
