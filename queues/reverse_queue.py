from queue import Queue


def reverse_queue(queue: Queue) -> Queue:
    """
    Reverses a queue using a stack.

    :param queue: is the queue to be reversed.
    :return: the reversed queue.
    """
    stack = []

    while not queue.empty():
        # Append the first item from queue to top of stack
        stack.append(queue.get())

    while len(stack) > 0:
        queue.put(stack.pop())

    return queue


if __name__ == '__main__':
    queue = Queue(3)

    queue.put(10)
    queue.put(20)
    queue.put(30)

    reversed = reverse_queue(queue)

    print(reversed.queue)
