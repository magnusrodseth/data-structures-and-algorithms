from typing import List


class PriorityQueue:
    __queue: List[int]
    __counter: int = 0

    def __init__(self, size):
        """
        A simple implementation of a priority queue of integers in ascending order.
        :param size: is the size of the queue.
        :raise AttributeError: if the size of the queue is less than or equal to 0.
        """
        
        if size <= 0:
            raise AttributeError("Size of queue must be greater than 0.")

        self.__queue = [0] * size
        self.__counter = 0

    def add(self, item):
        """
        Adds an item to the priority queue.

        :param item: is the item to add.
        :raise AttributeError: if the queue is full.
        """
        if self.is_full():
            raise AttributeError("Queue is full.")

        # Store index of the item to add
        index = self.__shift(item)

        self.__queue[index + 1] = item
        self.__counter += 1

    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        :return: a boolean value determining if the queue is full.
        """
        return self.__counter == len(self.__queue)

    def __shift(self, item: int) -> int:
        """
        Shifts the queue to the right to sort the provided item.

        :param item: is the item to add to the priority queue.
        :return: the index where we want to insert the item.
        """
        index = -1

        for i in range(self.__counter, -1, -1):
            if self.__queue[i] > item:
                self.__queue[i + 1] = self.__queue[i]
            else:
                index = i
                break

        return index

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        print(*self.__queue, sep=", ")


if __name__ == '__main__':
    queue = PriorityQueue(5)

    queue.add(5)
    queue.add(3)
    queue.add(7)
    queue.add(1)

    queue.print()
