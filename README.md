# Code with Mosh: Data Structures and Algorithms

## The boring stuff 💭

### What is it ❓

This repository serves as a collection of code snippets from "The Ultimate Data Structures and Algorithms", a course by
Code with Mosh. An overview of his courses can be found [here](https://codewithmosh.com/courses).

### Developer Information 🙋🏼‍♂️

Developed and written by Magnus Rødseth.

## The Big O Notation

### O(1)

```python
print("Hello, world!")  # O(1)
print("Hello, world again!")
# --> O(2) --> O(1) --> Constant time
```

### O(n)

```python
# ----- Example 1 -----
print("Hello, world!")  # O(1)

for i in range(10):  # O(n)
    print(i)

print("Bye, world!")  # O(1)

# ==> O(2 + n) ==> O(n)

# ----- Example 2 -----
numbers = [1, 2, 3]
names = ["John", "Adam", "Eve"]

for num in numbers:  # O(n)
    print(num)

for name in names:  # O(m)
    print(name)

# ==> O(n + m) ==> O(n)
# Still linear growth
```

### O(n^2)

```python
numbers = [1, 2, 3]

for first in numbers:  # O(n)
    for second in numbers:  # O(n)
        print(first + second)
# ==> O(n^2)

for num in numbers:  # O(n)
    print(num)
# ==> O(n + n^2) ==> O(n^2)

for first in numbers:  # O(n)
    for second in numbers:  # O(n)
        for third in numbers:  # O(n)
            print(first + second + third)
# ==> O(n^3)
```

### O(log n)

**Insert content here after learning about graphs and trees.**

### O(2^n)

**Insert content here after learning more.**

## Arrays

### Exercise: Building an Array class

```python
from typing import List


class Array:
    __length: int
    __array: List[int]
    __counter: int = 0

    def __init__(self, length: int):
        """
        Initializes an instance of the Array class.
        By default, an array is filled with 0 until items are inserted.

        :param length: is the number of items in the array.
        """

        if length < 0:
            raise ValueError("Length must be greater than or equal to 0.")

        self.__length = length
        self.__array = [0] * self.__length

    def insert(self, item: int):
        """
        Inserts an item at the end of the array,
        or the first available spot if the array is not yet filled up.

        :param item: is the item to be inserted.
        """

        if self.__counter == len(self.__array):
            self.__array = self.__double_size()

        # __counter is inside __array bounds
        try:
            self.__array[self.__counter] = item
            self.__counter += 1
        except IndexError:
            return

    def remove_at(self, index: int):
        """
        Removes the item at the provided index.

        :param index: is the index of the item to remove.
        """
        if index < 0 or index >= self.__counter:
            raise ValueError(
                "Index must be grater than or equal to 0, and less than or equal to the size of the array.")

        # Shift items to the left
        for i in range(index, self.__counter):
            self.__array[i] = self.__array[i + 1]

        self.__counter -= 1

    def index_of(self, item: int) -> int:
        """
        Gets the index of a given item in the array.
        
        :rtype: the index of the provided item, or -1 if it is not found.
        :param item: is the item to find the corresponding index for. 
        """

        for i in range(len(self.__array)):
            if self.__array[i] == item:
                return i

        return -1

    def max(self) -> int:
        """
        Finds the maximum value in the array.
        Runtime complexity: O(n).

        :return: the maximum value in the array.
        """

        max_value = self.__array[0]

        for num in self.__array:
            if num >= max_value:
                max_value = num

        return max_value

    def reverse(self) -> List[int]:
        """
        Reversed this array.
        Runtime complexity: O(n).

        :return: the reversed array
        """
        reversed = [0] * self.__counter

        counter = 0
        for i in range(self.__counter - 1, -1, -1):
            reversed[counter] = self.__array[i]
            counter += 1

        return reversed

    def print(self) -> None:
        """
        Prints the content of the array.
        Note that an array should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(self.__counter):
            if i == self.__counter - 1:
                s += f'{str(self.__array[i])}'
            else:
                s += f'{str(self.__array[i])}, '

        s += "]"

        print(s)

    def __double_size(self) -> List[int]:
        """
        Copies the existing array, and doubles the array size.

        :rtype: the copied array with doubled space.
        """
        copy = [0] * (self.__counter * 2)

        for i in range(self.__counter):
            copy[i] = self.__array[i]

        return copy
```

## Linked Lists

### Exercise: Building a LinkedList class

```python
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

        :param item: is the item to be inserted at the head.
        """

        node = _Node(item)

        # List has no items
        if self.__is_empty():
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

        :param item: is the item to be inserted at the tail.
        """

        node = _Node(item)

        # List has no items
        if self.__is_empty():
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

        :raise AttributeError: if the list is empty.
        """
        if self.__is_empty():
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

        :raise AttributeError: if the list is empty.
        """
        if self.__is_empty():
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
        """

        if self.__is_empty():
            return

        current: _Node = self.__first
        previous: _Node or None = None

        while current is not None:
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

        :return: the middle node or nodes.
        """

        if self.__is_empty():
            raise AttributeError("The list is empty")

        first_pointer = self.__first
        second_pointer: _Node = self.__first

        while (second_pointer != self.__last) and (second_pointer.next != self.__last):
            second_pointer = second_pointer.next._next
            first_pointer = first_pointer.next

        is_even: bool = second_pointer is None

        if is_even:
            return first_pointer, first_pointer.next

        return first_pointer

    def has_loop(self):
        first_pointer = self.__first
        second_pointer = self.__first
        found_loop = False

        while second_pointer is not None:
            second_pointer = second_pointer.next

            if second_pointer is not None:
                second_pointer = second_pointer.next
                first_pointer = first_pointer.next

            if first_pointer == second_pointer:
                found_loop = True
                break

        return found_loop

    def __is_empty(self) -> bool:
        """
        Checks if a linked list is empty.

        :return: a boolean representation of whether or not the linked list is empty.
        """

        return self.__first is None

    def __get_previous_node(self, node: _Node) -> _Node or None:
        current_node = self.__first

        while current_node.next is not None:
            # Currently at second last node in list
            if current_node.next == node:
                return current_node
            current_node = current_node.next

        return None
```