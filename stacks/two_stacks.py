from typing import List

from stacks.stack import Stack


class TwoStacks:
    """
    An implementation of 2 stacks in 1 array.
    The methods below uses the already implemented Stack class to efficiently
    utilize the functionality of a stack without wasting space.
    """
    __first_stack: Stack
    __second_stack: Stack
    __combined_stack: List[int]

    def __init__(self, size_1, size_2):
        if size_1 <= 0 or size_2 <= 0:
            raise AttributeError("Size of stack must be greater than 0.")

        self.__first_stack = Stack(size_1)
        self.__second_stack = Stack(size_2)

        self.__combine_stacks()

    def push_1(self, item):
        self.__first_stack.push(item)
        self.__combine_stacks()

    def push_2(self, item):
        self.__second_stack.push(item)
        self.__combine_stacks()

    def pop_1(self) -> int:
        popped = self.__first_stack.pop()
        self.__combine_stacks()

        return popped

    def pop_2(self):
        popped = self.__second_stack.pop()
        self.__combine_stacks()

        return popped

    def is_empty_1(self):
        return self.__first_stack.is_empty()

    def is_empty_2(self):
        return self.__second_stack.is_empty()

    def is_full_1(self):
        return len(self.__first_stack.stack) == self.__first_stack.counter

    def is_full_2(self):
        return len(self.__second_stack.stack) == self.__second_stack.counter

    def __combine_stacks(self):
        self.__combined_stack = self.__first_stack.stack + self.__second_stack.stack

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(self.__first_stack.counter + self.__second_stack.counter):
            if i == self.__first_stack.counter + self.__second_stack.counter - 1:
                s += f'{str(self.__combined_stack[i])}'
            else:
                s += f'{str(self.__combined_stack[i])}, '

        s += "]"

        print(s)


if __name__ == "__main__":
    stack = TwoStacks(2, 3)

    stack.print()

    stack.push_1(1)
    stack.push_1(2)

    stack.print()

    stack.push_2(3)
    stack.push_2(4)

    stack.print()

    print(f'1 is full, should be true: {stack.is_full_1()}')
    print(f'2 is full, should be false: {stack.is_full_2()}')

    print()

    print(f'1 is empty, should be false: {stack.is_empty_1()}')
    print(f'2 is empty, should be false: {stack.is_empty_2()}')
