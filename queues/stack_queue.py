from stacks.stack import Stack


class StackQueue:
    __first_stack: Stack
    __second_stack: Stack

    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Size must be greater than 0.")

        self.__first_stack = Stack(size)
        self.__second_stack = Stack(size)

    def enqueue(self, item: int):
        """
        Enqueues an item at the back of the queue. Complexity: O(1).

        :param item: is the item to be enqueued.
        """
        self.__first_stack.push(item)

    def dequeue(self) -> int:
        """
        Dequeues the first item in the queue. Complexity: O(n).

        :return: the dequeued item.
        :raise AttributeError: if the queue is empty.
        """
        if self.is_empty():
            raise AttributeError("Cannot dequeue more items, as queue is empty.")

        # Move items from first to second stack only if the second stack is empty
        self.__move_first_stack_to_second_stack()

        return self.__second_stack.pop()

    def __move_first_stack_to_second_stack(self):
        if self.__second_stack.is_empty():
            while not self.__first_stack.is_empty():
                self.__second_stack.push(self.__first_stack.pop())

    def peek(self) -> int:
        """
        Peeks the first item in the queue, without removing it.

        :rtype: the first item in the queue.
        """
        if self.is_empty():
            raise AttributeError("Cannot dequeue more items, as queue is empty.")

        # Only move items from first to second stack only if the second stack is empty
        self.__move_first_stack_to_second_stack()

        return self.__second_stack.pop()

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: a boolean value determining if the queue is empty.
        """
        return self.__first_stack.is_empty() and self.__second_stack.is_empty()


if __name__ == '__main__':
    queue = StackQueue(3)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    item1 = queue.dequeue()
    print(f'Dequeued: {item1}')

    item2 = queue.dequeue()
    print(f'Dequeued: {item2}')

    item3 = queue.dequeue()
    print(f'Dequeued: {item3}')
