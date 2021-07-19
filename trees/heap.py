from typing import List


class Heap:
    __heap: List[int] = []

    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Size must be greater than 0.")

        self.__size = 0
        self.__heap = [0 for i in range(size)]

    def insert(self, item: int) -> None:
        """
        Inserts an item into the heap.
        In a heap, the value of every node is greater than or equal to the value of its children.

        :param item: is the item to be inserted.
        """
        if self.is_full():
            raise AttributeError("Heap is full.")

        self.__heap[self.__size] = item
        self.__size += 1

        # This violates the heap property, so the item should be bubbled up
        self.__bubble_up()

    def sort(self, numbers: List[int], descending=True) -> List[int]:
        """
        Takes in a list of numbers and sorts them using a heap.

        :param numbers: are the numbers to sort.
        :param descending: is a boolean value determining if the sort is ascending or descending.
        :return: a new list of sorted_numbers numbers.
        """
        # Create new heap
        heap = Heap(len(numbers))

        for item in numbers:
            heap.insert(item)

        if descending:
            for i in range(len(numbers)):
                numbers[i] = heap.remove()
        else:
            for i in range(len(numbers), -1, -1):
                numbers[i] = heap.remove()

        return numbers

    def __swap(self, first: int, second: int):
        """
        Swaps the values at two indices in the internal array.

        :param first: is the first index.
        :param second: is the second index.
        """
        placeholder = self.__heap[first]
        self.__heap[first] = self.__heap[second]
        self.__heap[second] = placeholder

    def __parent_index(self, index) -> int:
        """
        Calculates the parent index of a given index.

        :param index: is the child index to find the corresponding parent for.
        :return: the index of the parent.
        """
        return (index - 1) // 2

    def __bubble_up(self):
        """
        Swaps items at two indices in the internal array in order to preserve the heap property.
        """
        current_index = self.__size - 1

        while (current_index > 0) and (self.__heap[current_index] > self.__heap[self.__parent_index(current_index)]):
            self.__swap(current_index, self.__parent_index(current_index))

            current_index = self.__parent_index(current_index)

    def remove(self) -> int:
        """
        Removes the root node from the heap.
        :rtype: the root node after items have been properly bubbled down.
        """
        if self.is_empty():
            raise AttributeError("Heap is empty")

        root = self.__heap[0]
        # Last item becomes root node
        self.__heap[0] = self.__heap[self.__size - 1]
        self.__size -= 1

        self.__bubble_down()

        return root

    def __max_child_index(self, index) -> int:
        """
        Gets the index of the child with greater value given the index of a parent value.

        :param index: is the parent index.
        :return: is the index of the greater child value.
        """
        if not self.__has_left_child(index):
            return index

        if not self.__has_right_child(index):
            return self.__left_child_index(index)

        return self.__left_child_index(index) \
            if self.__left_child(index) > self.__right_child(index) \
            else self.__right_child_index(index)

    def __has_left_child(self, index: int) -> bool:
        """
        Checks if a parent value has a left child.

        :param index: is the parent index.
        :return: a boolean value determining if the parent value has a left child.
        """
        return self.__left_child_index(index) <= self.__size

    def __has_right_child(self, index: int) -> bool:
        """
        Checks if a parent value has a right child.

        :param index: is the parent index.
        :return: a boolean value determining if the parent value has a right child.
        """
        return self.__right_child_index(index) <= self.__size

    def __left_child(self, index):
        """
        Gets the left child value of a parent index.

        :param index: is the parent index.
        :return: the left child.
        """
        return self.__heap[self.__left_child_index(index)]

    def __right_child(self, index):
        """
        Gets the right child value of a parent index.

        :param index: is the parent index.
        :return: the right child.
        """
        return self.__heap[self.__left_child_index(index)]

    def __left_child_index(self, index: int) -> int:
        """
        Gets the left child index of a parent index.

        :param index: is the parent index.
        :return: the left child index.
        """
        return (index * 2) + 1

    def __right_child_index(self, index: int) -> int:
        """
        Gets the left child index of a parent index.

        :param index: is the parent index.
        :return: the left child index.
        """
        return (index * 2) + 2

    def is_full(self) -> bool:
        """
        Checks if the heap is full.
        :return: a boolean indicating whether the heap is full.
        """
        return self.__size == len(self.__heap)

    def is_empty(self):
        """
        Checks if the heap is empty.
        :return: a boolean indicating whether the heap is empty.
        """
        return self.__size <= 0

    def __is_valid_parent(self, index):
        """
        Checks if the value at the given index is a valid parent.

        :param index: is the index to inspect.
        :return: a boolean indicating whether the value at index is a valid parent.
        """
        if not self.__has_left_child(index):
            return True

        is_valid: bool = self.__heap[index] >= self.__left_child(index)

        if self.__has_right_child(index):
            is_valid = is_valid and self.__heap[index] >= self.__right_child(index)

        return is_valid

    def __bubble_down(self) -> None:
        """
        Swaps items at two indices in the internal array in order to preserve the heap property.
        """
        current_index = 0

        while not self.__is_valid_parent(current_index) and current_index <= self.__size:
            # Determine the max value child
            max_child_index = self.__max_child_index(current_index)

            self.__swap(current_index, max_child_index)

            # Continuously bubble down the index
            current_index = max_child_index


if __name__ == '__main__':
    heap = Heap(20)
    sorted_numbers = heap.sort([5, 3, 10, 1, 4, 2])

    print(sorted_numbers)
