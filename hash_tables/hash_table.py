from typing import List


class _Node:
    __key: int
    __value: str
    _next = None  # Reference to next Node

    def __init__(self, key, value):
        """
        A node holds the key and value of an item in the hash table.
        """
        self.__key = key
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self._next


class _LinkedList:
    __first: _Node or None = None  # Reference to head Node
    __last: _Node or None = None  # Reference to tail Node
    __size: int = 0

    @property
    def size(self):
        return self.__size

    def add_last(self, key: int, value: str) -> None:
        """
        Adds a node at the end of the linked list.

        :param key: is the key.
        :param value: is the value.
        """

        node = _Node(key, value)

        # List has no items
        if self.__is_empty():
            self.__first = node
            self.__last = node
        # List has last item
        else:
            self.__last._next = node
            self.__last = node

        self.__size += 1

    def __is_empty(self) -> bool:
        """
        Checks if a linked list is empty.

        :return: a boolean representation of whether or not the linked list is empty.
        """

        return self.__first is None

    def contains(self, key: int) -> bool:
        """
        Checks if the linked list contains a node with a given key.

        :param key: is the key to inspect if the linked list contains.
        :return: a boolean representation of whether the linked list contains the given value or not.
        """

        return self.index_of(key) != -1

    def index_of(self, key: int) -> int:
        """
        Gets the index of a given key from the linked list.
        Time complexity: O(n).

        :param key: is the key to find the index of.
        :return: the index of the key, or -1 if it does not exist.
        """
        index = 0

        current_node = self.__first

        while current_node:
            if current_node.key == key:
                return index

            index += 1
            current_node = current_node.next

        return -1

    def get_node(self, key: int) -> _Node or None:
        """
        Gets a node with a given key. A key is a unique identifier.
        Time complexity: O(n).

        :param key: is the key in the key-value pair.
        :return: the Node with the given key, or None if no such Node exists.
        """
        current_node = self.__first

        while current_node:
            if current_node.key == key:
                return current_node
            current_node = current_node.next

        return None

    def remove(self, key: int):
        """
        Removes the node with the given key from the linked list.

        :raise AttributeError: if the list is empty.
        """
        if self.__is_empty():
            raise AttributeError(
                "Linked list is empty and has no last element.")

        # List has only one element
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
            self.__size = 0
            return

        index = self.index_of(key)

        # Key-value pair does not exist in linked list
        if index == -1:
            return None

        nth_from_the_end = self.get_nth_node_from_end(self.__size - index)

        previous: _Node or None = self.__get_previous_node(nth_from_the_end)

        # Unlink what was previously the nth node from the end
        nth_from_the_end = previous
        nth_from_the_end._next = None
        self.__size -= 1

    def __get_previous_node(self, node: _Node) -> _Node or None:
        current_node = self.__first

        while current_node.next is not None:
            # Currently at second last node in list
            if current_node.next == node:
                return current_node
            current_node = current_node.next

        return None

    def get_nth_node_from_end(self, n: int) -> _Node:
        """
        Finds the n-th node from the end of the linked list in one pass.

        :rtype: the n-th node from the end.
        :param n: is the index from the end of the node we want to find
        """

        if self.__is_empty():
            raise AttributeError("The linked list is empty.")

        first_pointer = self.__first

        # Second pointer will get moved along n amount of spots
        second_pointer: _Node = first_pointer

        # Move second pointer along n amount of items in the list
        for i in range(n - 1):
            second_pointer = second_pointer.next
            if second_pointer is None:
                # Assuming we don't know the size of the linked list
                raise AttributeError(
                    "The value n is greater than the amount of items in the linked list.")

        while second_pointer:
            if second_pointer.next is None:
                return first_pointer

            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

    def print(self):
        current_node = self.__first

        while current_node:
            print(f"\t[Node(key={current_node.key}, value={current_node.value})]")

            current_node = current_node.next


class HashTable:
    __table: List[_LinkedList or None]

    def __init__(self, size):
        """
        An implementation of a hash table, with integer keys and string values.
        We use chaining for handling collisions.
        This means that instead of storing the key-value pairs inside each slot in the internal array,
        we store them in linked lists.

        This means that the internal array consists of _LinkedList instances,
        where each node is of type _Node.

        :param size: is the size of the internal array.
        :raise AttributeError: if the size is less than or equal to 0.
        """

        if size <= 0:
            raise AttributeError("Size must be greater than zero.")

        self.__table = [_LinkedList() for i in range(size)]

    def put(self, key: int, value: str):
        """
        Puts a key-value pair into the hash table.

        :param key: is the key.
        :param value: is the value.
        """
        index = self.__hash(key)

        linked_list = self.__table[index]

        linked_list.add_last(key, value)

    def get(self, key: int) -> str or None:
        """
        Gets a key-value pair from the hash table.

        :param key: is the key of the key-value pair.
        :return: the value of the key-value pair, or None if the linked list does not contain the key-value pair.
        """
        index = self.__hash(key)

        linked_list = self.__table[index]

        if linked_list.contains_iterative(key):
            return linked_list.get_node(key)

        return None

    def remove(self, key: int):
        """
        Removes a Node entry from the hash table.

        :param key: is the key in the key-value pair.
        """
        index = self.__hash(key)

        linked_list = self.__table[index]

        if linked_list is None:
            raise AttributeError("The linked list is undefined.")

        if linked_list.contains_iterative(key):
            linked_list.remove(key)

    def __hash(self, key: int) -> int:
        """
        A very simple hash function for calculating the index of the relevant key-value pair.
        Chaining is later used to handling collisions.

        :param key: is the key of the key-value pair to be put into the hash table.
        :return: the index of the relevant key-value pair in the hash table.
        """

        return key % len(self.__table)

    def print(self):
        for i in range(len(self.__table)):
            print(f"Linked list at index: {i}")

            self.__table[i].print()
            print()


if __name__ == '__main__':
    hash_table = HashTable(5)

    hash_table.put(2, "Hello")
    hash_table.put(4, "World")
    hash_table.put(9, "Dolor")
    hash_table.put(5, "Lorem")
    hash_table.put(5, "Ipsum")
    hash_table.put(56483721657860, "Abnormally large number")

    hash_table.print()

    print(f'Node value with key 9: {hash_table.get(9).value}')
    print(f'Node value with key 2: {hash_table.get(2).value}')
    print(f'Node value with key 56483721657860: {hash_table.get(56483721657860).value}')
    print(f'Node value with key that does not exist: {hash_table.get(14563236251)}')

    hash_table.remove(5)

    print(f'Node value from key (5) that was just removed: {hash_table.get(5)}')
