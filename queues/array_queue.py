from typing import List


class ArrayQueue:
    __queue: List[int]
    __front: int
    __rear: int
    __counter: int

    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Size must be greater than 0.")

        self.__queue = [0] * size
        self.__front = 0
        self.__rear = 0
        self.__counter = 0

    def enqueue(self, item: int):
        """
        Enqueues an item at the back of the queue.

        :param item: is the item to be enqueued.
        :raise OverflowError: if the queue is full.
        """
        if self.is_full():
            raise OverflowError("Cannot enqueue more items, as queue is full.")

        # Add item to the back of the queue, and make queue circular
        self.__queue[self.__rear] = item
        self.__rear = (self.__rear + 1) % len(self.__queue)
        self.__counter += 1

    def dequeue(self) -> int:
        """
        Dequeues the first item in the queue.

        :return: the dequeued item.
        :raise AttributeError: if the queue is empty.
        """
        if self.is_empty():
            raise AttributeError("Cannot dequeue more items, as queue is empty.")

        item = self.__queue[self.__front]

        # "Empty" first item
        self.__queue[self.__front] = 0

        # Push queue back one space, and make it circular
        self.__front = (self.__front + 1) % len(self.__queue)

        return item

    def peek(self) -> int:
        """
        Peeks the first item in the queue, without removing it.

        :rtype: the first item in the queue.
        """
        return self.__queue[self.__front]

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: a boolean value determining if the queue is empty.
        """
        return self.__front == self.__rear

    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        :return: a boolean value determining if the queue is full.
        """
        return len(self.__queue) == self.__counter

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        print(*self.__queue, sep=", ")


if __name__ == '__main__':
    queue = ArrayQueue(3)

    queue.print()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.dequeue()

    queue.print()

    queue.enqueue(30)

    queue.print()

    queue.enqueue(40)

    queue.print()
