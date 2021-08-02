from typing import List


class _Node:
    __value: int
    _next = None  # Reference to next Node

    def __init__(self, value):
        self.__value = value

    @property
    def next(self):
        return self._next

    @property
    def value(self):
        return self.__value


class LinkedList:
    __first: _Node or None = None  # Reference to head Node
    __last: _Node or None = None  # Reference to tail Node
    __size: int = 0

    def add_first(self, item: int) -> None:
        """
        Adds a node in the beginning of the linked list.
        Time complexity: O(1).
        Space complexity: O(n).

        :param item: is the item to be inserted at the head.
        """

        node = _Node(item)

        # List has no items
        if self.is_empty():
            self.__first = node
            self.__last = node
        # List has first item
        else:
            node._next = self.__first
            self.__first = node

        self.__size += 1

    def add_last(self, item: int) -> None:
        """
        Adds a node at the end of the linked list.
        Time complexity: O(1).
        Space complexity: O(n).

        :param item: is the item to be inserted at the tail.
        """

        node = _Node(item)

        # List has no items
        if self.is_empty():
            self.__first = node
            self.__last = node
        # List has last item
        else:
            self.__last._next = node
            self.__last = node

        self.__size += 1

    def remove_first(self) -> None:
        """
        Removes the first node in the list.
        Time complexity: O(1).
        Space complexity: O(n).

        :raise AttributeError: if the list is empty.
        """
        if self.is_empty():
            raise AttributeError("Linked list is empty and has no first element.")

        # List has only one element
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
            self.__size = 0
            return

        second = self.__first.next
        self.__first._next = None
        self.__first = second
        self.__size -= 1

    def remove_last(self) -> None:
        """
        Removed the last node in the linked list.
        Time complexity: O(1).
        Space complexity: O(n).

        :raise AttributeError: if the list is empty.
        """
        if self.is_empty():
            raise AttributeError("Linked list is empty and has no last element.")

        # List has only one element
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
            self.__size = 0
            return

        previous: _Node or None = self.__get_previous_node(self.__last)

        # Unlink what was previously the last node
        self.__last = previous
        self.__last._next = None
        self.__size -= 1

    def contains(self, value: int) -> bool:
        """
        Checks if the linked list contains a node with a given value.

        :param value: is the value to inspect if the linked list contains.
        :return: a boolean representation of whether the linked list contains the given value or not.
        """

        return self.index_of(value) != -1

    def size(self) -> int:
        """
        Gets the amount of nodes in the linked list.
        Runtime complexity: O(1).
        Note that if we were to traverse the entire list each time this method was called,
        and add up the size, the runtime complexity would be O(n).

        :return: the size of the list.
        """
        return self.__size

    def index_of(self, value: int) -> int:
        """
        Gets the index of a given value from the linked list.
        Time complexity: O(n).
        Space complexity: O(n).

        :param value: is the value to find the index of.
        :return: the index of the value, or -1 if it does not exist.
        """
        index = 0

        current_node = self.__first

        while current_node:
            if current_node.value == value:
                return index

            index += 1
            current_node = current_node.next

        return -1

    def to_array(self) -> List[int]:
        """
        Converts the linked list into an array of integer values.
        Time complexity: O(n).
        Space complexity: O(n).

        :return: the array.
        """
        array = [0] * self.size()

        current_node = self.__first
        index = 0

        while current_node:
            array[index] = current_node.value
            index += 1
            current_node = current_node.next

        return array

    def reverse(self) -> None:
        """
        Reverses the linked list in place.
        Time complexity: O(n).
        Space complexity: O(n).
        """

        if self.is_empty():
            return

        current: _Node = self.__first
        previous: _Node or None = None

        while current:
            next_node = current.next
            # This is where the reversal happens
            current._next = previous
            previous = current
            current = next_node

        # Reversed linked list starts at "last" item
        self.__first = previous

    def get_nth_node_from_end(self, n: int) -> _Node:
        """
        Finds the n-th node from the end of the linked list in one pass.
        Example where n = 3:
        [10, 20, 30, 40, 50]

        1. Create first and second pointers

        [10, 20, 30, 40, 50]
         *       *

        2. Advance pointers while second pointer is defined

        [10, 20, 30, 40, 50]
                   *       *

        Now, the first pointer points to the target node.

        Time complexity: O(n + m).
        Space complexity: O(n).

        :rtype: the n-th node from the end.
        :param n: is the index from the end of the node we want to find
        """

        if self.is_empty():
            raise AttributeError("The linked list is empty.")

        first_pointer = self.__first

        # Second pointer will get moved along n amount of spots
        second_pointer: _Node = first_pointer

        # Move second pointer along n amount of items in the list
        for i in range(n - 1):
            second_pointer = second_pointer.next
            if second_pointer is None:
                # Assuming we don't know the size of the linked list
                raise AttributeError("The value n is greater than the amount of items in the linked list.")

        while second_pointer:
            if second_pointer.next is None:
                return first_pointer

            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

    def get_middle_node(self) -> _Node or (_Node, _Node):
        """
        Gets the middle node if the size of the linked list is odd,
        or the two middle nodes if the size of the linked list is even.
        Time complexity: O(n).
        Space complexity: O(n).

        :return: the middle node or nodes.
        """

        if self.is_empty():
            raise AttributeError("The list is empty")

        first_pointer = self.__first
        second_pointer: _Node = self.__first

        while (second_pointer != self.__last) and (second_pointer.next != self.__last):
            # This is simply a discovered pattern; move second pointer twice and first pointer once
            second_pointer = second_pointer.next.next
            first_pointer = first_pointer.next

        is_even: bool = second_pointer is None

        if is_even:
            return first_pointer, first_pointer.next

        return first_pointer

    def has_loop(self) -> bool:
        """
        Checks if the linked list contains a loop.
        Time complexity: O(n).
        Space complexity: O(n).

        :return: a boolean indicating whether the linked list contains a loop.
        """
        first_pointer = self.__first
        second_pointer = self.__first
        found_loop = False

        while second_pointer is not None:
            second_pointer = second_pointer.next

            if second_pointer is not None:
                # Advance second pointer twice
                second_pointer = second_pointer.next
                first_pointer = first_pointer.next

            if first_pointer == second_pointer:
                found_loop = True
                break

        return found_loop

    def is_empty(self) -> bool:
        """
        Checks if a linked list is empty.
        Time complexity: O(1).
        Space complexity: O(n).

        :return: a boolean representation of whether or not the linked list is empty.
        """

        return self.__first is None

    def __get_previous_node(self, node: _Node) -> _Node or None:
        """
        Gets the previous node, given a node.
        Time complexity: O(n).
        Space complexity: O(n).

        :param node: is the given node
        :return: the previous node of the node given in the parameter.
        """
        current_node = self.__first

        while current_node.next is not None:
            # Currently at second last node in list
            if current_node.next == node:
                return current_node
            current_node = current_node.next

        return None


if __name__ == '__main__':
    linked_list = LinkedList()
