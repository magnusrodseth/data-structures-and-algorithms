from typing import List


class MinStack:
    __size: int
    __counter: int = 0
    __stack: List[int or None] = 0
    __minimum: int or None = None

    def __init__(self, size: int):
        if size <= 0:
            raise AttributeError("Size of stack must be greater than 0.")

        self.__size = size
        self.__stack = [None] * self.__size

    def push(self, value: int):
        """
        Pushes an item at the top of the stack.
        If the new value is the minimum value, self.__minimum is updated to preserve O(1) runtime.

        :param value: is the item to push.
        :raise OverflowError: if the stack is full.
        """
        if self.is_full():
            raise OverflowError("Stack is full.")

        if not self.__minimum and self.is_empty():
            self.__minimum = value

        # Overwrite minimum value
        if value < self.__minimum:
            self.__minimum = value

        self.__stack[self.__counter] = value
        self.__counter += 1

    def pop(self):
        """
        Pops the top item off the stack and shrinks the stack by 1 item.

        :raise ValueError: if the stack is empty.
        :return: the popped value.
        """
        if self.is_empty():
            return

        popped = self.__stack[self.__counter - 1]

        new_stack: List[int or None] = [None] * self.__counter

        # Shrink stack by one item
        for i in range(self.__counter):
            new_stack[i] = self.__stack[i]

        self.__stack = new_stack
        self.__counter -= 1

        self.__minimum = self.__get_minimum()

        return popped

    def min(self):
        """
        Gets the minimum value of the stack.
        Time complexity: O(1).

        :return: the minimum value.
        """
        return self.__minimum

    def is_full(self):
        return self.__counter == len(self.__stack)

    def __get_minimum(self):
        """
        Calculates the minimum value of the stack.
        Time complexity: O(n).

        :return: the minimum value.
        """
        minimum = self.__stack[0]
        for i in range(self.__counter):
            if self.__stack[i] < minimum:
                minimum = self.__stack[i]
        return minimum

    def is_empty(self):
        return self.__counter == 0


if __name__ == '__main__':
    min_stack = MinStack(5)

    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(10)
    min_stack.push(1)

    print(min_stack.min())
    min_stack.pop()
    print(min_stack.min())
