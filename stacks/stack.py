from typing import List


class Stack:
    __size: int
    __stack: List[int or None]
    __counter: int = 0

    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Size of stack must be greater than 0.")

        self.__size = size

        # Initialize stack with None values
        self.__stack = [0] * self.__size

    def push(self, item: int) -> None:
        """
        Pushes an item at the top of the stack.
        
        :param item: is the item to push.
        :raise OverflowError: if the stack is full.
        """
        if self.__counter == len(self.__stack):
            raise OverflowError("The stack is overflowed.")

        self.__stack[self.__counter] = item
        self.__counter += 1

    def pop(self):
        """
        Pops the top item off the stack and shrinks the stack by 1 item.

        :raise ValueError: if the stack is empty.
        :return: the popped value.
        """
        if self.is_empty():
            raise ValueError("There are no items to pop, because the stack is empty.")

        popped = self.__stack[self.__counter - 1]

        new_stack: List[int] = [0] * self.__counter

        # Shrink stack by one item
        for i in range(self.__counter):
            new_stack[i] = self.__stack[i]

        self.__stack = new_stack
        self.__counter -= 1

        return popped

    def peek(self):
        """
        Peeks the top item in the stack. Does not shrink the stack.

        :return: the peeked value.
        """
        return self.__stack[self.__counter - 1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: a boolean value determining if the stack is empty.
        """
        return self.__counter == 0

    def __double_size(self) -> List[int]:
        """
        Copies the existing stack, and doubles the stack size.

        :rtype: the copied stack with doubled space.
        """
        copy = [0] * (self.__counter * 2)

        for i in range(self.__counter):
            copy[i] = self.__stack[i]

        return copy

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(self.__counter):
            if i == self.__counter - 1:
                s += f'{str(self.__stack[i])}'
            else:
                s += f'{str(self.__stack[i])}, '

        s += "]"

        print(s)


if __name__ == "__main__":
    stack = Stack(5)

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.print()

    popped = stack.pop()
    print(f'Popped: {popped}')

    stack.print()

    popped = stack.pop()
    print(f'Popped: {popped}')

    stack.print()

    peeked = stack.peek()
    print(f'Peeked: {peeked}')

    stack.print()

    stack.pop()

    print(f'Is empty? Should be true: {stack.is_empty()}')
