from trees.heap import Heap


# Notice how this class is essentially a wrapper around an existing heap.
# It simply gives us another interface (more queue-like) to work with.
class PriorityQueueWithHeap:
    # This implementation uses our custom heap.
    # This can also use built-in implementations from Python.
    __heap = Heap(10)

    def enqueue(self, item: int):
        self.__heap.insert(item)

    def dequeue(self):
        return self.__heap.remove()

    def is_full(self):
        return self.__heap.is_full()

    def is_empty(self):
        return self.__heap.is_empty()
