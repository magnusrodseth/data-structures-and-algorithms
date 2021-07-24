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

## Stacks

### Exercise: Reversing a string using a stack

```python
from typing import List


def reverse_string(string: str) -> str:
    """
    Reverses a string using a stack.

    :param string: is the string to be reversed.
    :raise AttributeError: if the input is None.
    :return: is the reversed string.
    """
    if string is None:
        raise AttributeError("The input cannot be null.")

    stack: List[str] = []

    for letter in string:
        stack.append(letter)

    reversed = ""

    while not is_empty(stack):
        reversed += stack.pop()

    return reversed


def is_empty(stack: List[str]) -> bool:
    """
    Check if a stack is empty.
    We add this custom method, as Python does not have a built-in is_empty() method.

    :param stack: is the stack to inspect.
    :return: a boolean value determining whether the stack is empty or not.
    """
    return len(stack) == 0
```

### Exercise: Evaluating if an expression is balanced using a stack

```python
from typing import List


def is_balanced(expression: str) -> bool:
    """
    Checks if a string is balanced.
    A string is balanced if the types of brackets line up.

    :param expression: is the expression to evaluate.
    :raise AttributeError: if the expression is None.
    :return: a boolean value determining if the string is balanced.
    """
    if expression is None:
        raise AttributeError("Expression cannot be None.")

    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    stack: List[str] = []
    balanced: bool = False

    for letter in expression:
        # We have a matching opening bracket
        if letter in bracket_map:
            stack.append(letter)

        if len(stack) >= 1:
            previous = peek(stack)

            # We have a matching ending bracket
            if bracket_map[previous] == letter:
                popped = stack.pop(len(stack) - 1)
                balanced = True
            else:
                balanced = False

    return balanced


def peek(stack: List[str]) -> str:
    """
    Peeks the top item in the stack,

    :param stack: is the stack to peek.
    :return: is the item at the top of the stack, without removing it.
    """
    return stack[len(stack) - 1]
```

### Exercise: Building a stack from scratch

```python
from typing import List


class Stack:
    __size: int
    __stack: List[int]
    __counter: int = 0

    def __init__(self, size):
        if size <= 0:
            raise AttributeError("Size of stack must be greater than 0.")

        self.__size = size

        # Initialize stack with 0 values
        self.__stack = [0] * self.__size

    def push(self, item: int) -> None:
        """
        Pushes an item at the top of the stack.

        :param item: is the item to push.
        :raise OverflowError: if the stack is full.
        """
        if self.__counter == len(self.__stack):
            raise OverflowError("The stack is overflowed.")

        self.__stack[self.__counter] = item
        self.__counter += 1

    def pop(self):
        """
        Pops the top item off the stack and shrinks the stack by 1 item.

        :raise ValueError: if the stack is empty.
        :return: the popped value.
        """
        if self.is_empty():
            raise ValueError("There are no items to pop, because the stack is empty.")

        popped = self.__stack[self.__counter - 1]

        new_stack: List[int] = [0] * self.__counter

        # Shrink stack by one item
        for i in range(self.__counter):
            new_stack[i] = self.__stack[i]

        self.__stack = new_stack
        self.__counter -= 1

        return popped

    def peek(self):
        """
        Peeks the top item in the stack. Does not shrink the stack.

        :return: the peeked value.
        """
        return self.__stack[self.__counter - 1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: a boolean value determining if the stack is empty.
        """
        return self.__counter == 0

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(self.__counter):
            if i == self.__counter - 1:
                s += f'{str(self.__stack[i])}'
            else:
                s += f'{str(self.__stack[i])}, '

        s += "]"

        print(s)
```

### Exercise: Implement two stacks in one array

```python
from typing import List

from stacks.stack import Stack


class TwoStacks:
    """
    An implementation of 2 stacks in 1 array.
    The methods below uses the already implemented Stack class to efficiently
    utilize the functionality of a stack without wasting space.
    """
    __first_stack: Stack
    __second_stack: Stack
    __combined_stack: List[int]

    def __init__(self, size_1, size_2):
        if size_1 <= 0 or size_2 <= 0:
            raise AttributeError("Size of stack must be greater than 0.")

        self.__first_stack = Stack(size_1)
        self.__second_stack = Stack(size_2)

        self.__combine_stacks()

    def push_1(self, item):
        self.__first_stack.push(item)
        self.__combine_stacks()

    def push_2(self, item):
        self.__second_stack.push(item)
        self.__combine_stacks()

    def pop_1(self) -> int:
        popped = self.__first_stack.pop()
        self.__combine_stacks()

        return popped

    def pop_2(self):
        popped = self.__second_stack.pop()
        self.__combine_stacks()

        return popped

    def is_empty_1(self):
        return self.__first_stack.is_empty()

    def is_empty_2(self):
        return self.__second_stack.is_empty()

    def is_full_1(self):
        return len(self.__first_stack.stack) == self.__first_stack.counter

    def is_full_2(self):
        return len(self.__second_stack.stack) == self.__second_stack.counter

    def __combine_stacks(self):
        self.__combined_stack = self.__first_stack.stack + self.__second_stack.stack

    def print(self) -> None:
        """
        Prints the content of the stack.
        Note that a stack should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(self.__first_stack.counter + self.__second_stack.counter):
            if i == self.__first_stack.counter + self.__second_stack.counter - 1:
                s += f'{str(self.__combined_stack[i])}'
            else:
                s += f'{str(self.__combined_stack[i])}, '

        s += "]"

        print(s)
```

## Queues

### Exercise: Reversing a queue

```python
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
```

### Exercise: Implementing a queue using an array

```python
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
```

### Exercise: Building a queue from 2 stacks

```python
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
```

### Exercise: Build a priority queue

```python
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
```

## Hash tables

### Exercise: First non-repeating character

```python
from typing import Dict


def first_non_repeating_character(string: str) -> str or None:
    """
    Finds the first non-repeating character in a string using a hash table (in Python: dictionary).

    :param string: is the string to find the first non-repeating character.
    :return: the first non-repeating character, or None if no characters only occur once.
    """

    string = string.lower()

    character_dict: Dict[str, int] = {}

    for letter in string:
        # Fetch the number of occurrences of this letter if it exists in the dictionary,
        # or 0 if it does not exist
        count = character_dict[letter] if letter in character_dict else 0

        # Set the number of occurrences of given letter
        character_dict[letter] = count + 1

    for letter in string:
        if character_dict[letter] == 1:
            return letter

    return None
```

### Exercise: First repeated character using set

```python
from typing import Set


def first_repeated_character(string: str) -> str or None:
    """
    Finds the first repeated character in a string using a set.

    :param string: is the string to find the first repeating character.
    :return: the first repeating character, or None if no characters occurs several times.
    """

    string = string.lower()

    # Initialize set. Even if we pass in an empty string (""), we return None.
    character_set: Set[str] = {""}

    for letter in string:
        # We have a duplicate value
        if letter in character_set:
            return letter
        # We do not have a duplicate value
        else:
            character_set.add(letter)

    return None
```

### Exercise: Building a hash table from scratch

```python
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

        if linked_list.contains(key):
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

        if linked_list.contains(key):
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
```

## Trees

### Exercise: Build a binary tree from scratch

```python
from typing import List

# These constants are later used to validate a binary search tree
NEGATIVE_INFINITY = float('-inf')
POSITIVE_INFINITY = float('inf')


class _Node:
    __value: int
    _left_child = None
    _right_child = None

    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    def __str__(self):
        return str(self.__value)


class Tree:
    __root: _Node or None = None

    @property
    def root(self):
        return self.__root

    def insert(self, value: int) -> None:
        """
        Inserts a value into the binary tree. The value is wrapped in a _Node.

        :param value: is the value to be inserted
        """

        # Tree is empty
        if self.__root is None:
            self.__root = _Node(value)
            return

        # Tree has root and potentially children
        current = self.__root

        while current:
            if value < current.value:
                if not current.left_child:
                    current._left_child = _Node(value)
                    return
                else:
                    current = current.left_child
            elif value > current.value:
                if not current.right_child:
                    current._right_child = _Node(value)
                    return
                else:
                    current = current.right_child

    def contains(self, value: int) -> bool:
        """
        Checks if the binary tree contains the value.

        :param value: is the value to find.
        :return: a boolean value determining if the binary tree contains the value.
        """

        # Tree is empty
        if self.__root is None:
            return False

        current = self.__root

        while current:
            # Found value in tree
            if value == current.value:
                return True

            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child

        return False

    def equals(self, tree) -> bool:
        """
        Checks this and another tree for equality recursively.

        :param tree: is the tree to check for equality.
        :return: a boolean value determining if the trees are equal.
        """
        if tree is None:
            return False

        return self.__equals(self.__root, tree.__root)

    def __equals(self, first: _Node, second: _Node) -> bool:
        """
        The implementation detail to check this and another tree for equality recursively,
        using depth-first search pre-order traversal.

        :param first: is the first node to check.
        :param second: is the second node to check.
        :return: a boolean value determining if the trees are equal.
        """

        # Both trees are empty
        if first is None and second is None:
            return True

        # Both trees have defined nodes and we should check left and right subtrees for equality
        if first and second:
            return first.value == second.value
                   and self.__equals(first.left_child, second.left_child)
                   and self.__equals(first.right_child, second.right_child)

        # These nodes are not equal
        return False

    def is_binary_search_tree(self) -> bool:
        """
        Checks if this tree is a binary search tree recursively.
        A tree is a binary search tree if all nodes in the left subtree is less than the root node,
        and all nodes in the right subtree is greater than the root node.

        :return: a boolean value determining if the tree is a binary search tree.
        """

        # The minimum value for a root node is negative infinity.
        # The maximum value for a root node is positive infinity.
        return self.__is_binary_search_tree(self.__root, NEGATIVE_INFINITY, POSITIVE_INFINITY)

    def __is_binary_search_tree(self, node: _Node, min_value: float, max_value: float) -> bool:
        """
        The implementation detail of checking if this tree is a binary search tree recursively.
        A tree is a binary search tree if all nodes in the left subtree is less than the root node,
        and all nodes in the right subtree is greater than the root node.

        :param node: is the node to validate
        :param min_value: is the node's minimum value.
        :param max_value: is the node's maximum value.
        :return: a boolean value determining if the tree is a binary search tree.
        """
        if node is None:
            return True

        # Node value is out of bounds
        if node.value < min_value or node.value > max_value:
            return False

        return self.__is_binary_search_tree(node.left_child, min_value, node.value - 1)
               and self.__is_binary_search_tree(node.right_child, node.value + 1, max_value)

    def get_nodes_with_distance(self, n: int) -> List[_Node]:
        """
        Gets nodes with distance n from the root of the tree recursively.

        :param n: is the distance from the root. Note that the root node has distance 0 from itself.
        :return: a list of nodes with distance n from the root node.
        """

        nodes: List[_Node] = []

        # Recursively add nodes with distance n from root node.
        self.__get_nodes_with_distance(self.__root, n, nodes)

        return nodes

    def __get_nodes_with_distance(self, node: _Node, n: int, nodes: List[_Node]):
        """
        The implementation detail of getting nodes with distance n from the root node.

        :param node: is the current node to compare.
        :param n: is the current distance from root.
        :param nodes: is the list of nodes with distance n from the root node.
        """
        if node is None:
            return

        if n == 0:
            nodes.append(node)
            return

        # Recursively find the nodes with distance n from the root node.
        if node.left_child:
            self.__get_nodes_with_distance(node.left_child, n - 1, nodes)
        if node.right_child:
            self.__get_nodes_with_distance(node.right_child, n - 1, nodes)

    def minimum_value(self) -> int:
        """
        Finds the minimum value in a binary tree. O(n).
        :return: the minimum value in the tree.
        """
        if self.__root is None:
            raise AttributeError("Tree is empty and has no minimum value.")

        return self.__minimum_value(self.__root)

    def __minimum_value(self, root: _Node) -> int:
        """
        The implementation detail of finding the minimum value in a binary tree. O(n).

        :rtype: the minimum value in the binary tree.
        """
        if self.__is_leaf_node(root):
            return root.value

        # Find minimum value of left subtree
        minimum_value_left = self.__minimum_value(self.__root.left_child)

        # Find minimum value of right subtree
        minimum_value_right = self.__minimum_value(self.__root.right_child)

        # Find minimum value in subtrees
        minimum_value_subtree = min(minimum_value_left, minimum_value_right)

        return min(minimum_value_subtree, root.value)

    def minimum_value_in_binary_search_tree(self) -> int:
        """
        Finds the minimum value in a binary search tree. Recall that in a binary search tree, the left subtree's
        values will always be less than the right subtree's values. O(log n).

        :return: the minimum value in the binary search tree.
        """
        if self.__root is None:
            raise AttributeError(
                "Binary search tree is empty, and has no minimum value.")

        current = self.__root
        last = current.left_child

        while current:
            last = current

            # In a binary search tree, the leftmost leaf node will always be the minimum value.
            current = current.left_child

        return last.value

    def maximum_value_in_binary_search_tree(self) -> int:
        """
        Finds the maximum value in a binary search tree. Recall that in a binary search tree, the left subtree's
        values will always be less than the right subtree's values. O(log n).

        :return: the maximum value in the binary search tree.
        """
        if self.__root is None:
            raise AttributeError(
                "Binary search tree is empty, and has no maximum value.")

        current = self.__root
        last = current.right_child

        while current:
            last = current

            # In a binary search tree, the rightmost leaf node will always be the maximum value.
            current = current.right_child

        return last.value

    def __is_leaf_node(self, node: _Node) -> bool:
        """
        Checks if a node is a leaf node.

        :rtype: a boolean value determining if the node is a leaf node.
        """
        return (node.left_child is None) and (node.right_child is None)

    def height(self) -> int:
        """
        Calculates the height of the binary tree using recursion.

        :return: the height of the tree, -1 if the tree is empty.
        """

        # Tree is empty
        if self.__root is None:
            return -1

        return self.__height(self.__root)

    def __height(self, root: _Node) -> int:
        """
        The implementation detail of calculating the height of the binary tree using recursion.

        :param root: is the current node.
        :return: the height of the tree.
        """
        if self.__is_leaf_node(root):
            return 0

        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))

    def traverse_pre_order(self) -> None:
        """
        An implementation of pre-order traversal of a tree using recursion.
        """
        self.__traverse_pre_order(self.__root)

    def __traverse_pre_order(self, root: _Node) -> None:
        """
        The implementation detail of pre-order traversal of a tree using recursion.

        :param root: is the current Node, or None if there are no more child nodes.
        """

        # Base condition
        if root is None:
            return

        # Root, left, right
        print(root)
        self.__traverse_pre_order(root.left_child)
        self.__traverse_pre_order(root.right_child)

    def traverse_in_order(self) -> None:
        """
        An implementation of in-order traversal of a tree using recursion.
        """

        self.__traverse_in_order(self.__root)

    def __traverse_in_order(self, root: _Node) -> None:
        """
        The implementation detail of in-order traversal of a tree using recursion.

        :param root: is the current Node, or None if there are no more child nodes.
        """

        if root is None:
            return

        # Left, root, right
        self.__traverse_in_order(root.left_child)
        print(root)
        self.__traverse_in_order(root.right_child)

    def traverse_post_order(self) -> None:
        """
        An implementation of post-order traversal of a tree using recursion.
        """

        self.__traverse_post_order(self.__root)

    def __traverse_post_order(self, root: _Node) -> None:
        """
        The implementation detail of post-order traversal of a tree using recursion.

        :param root: is the current Node, or None if there are no more child nodes.
        """
        if root is None:
            return

        # Left, right, root
        self.__traverse_post_order(root.left_child)
        self.__traverse_post_order(root.right_child)
        print(root)

    def traverse_level_order(self):
        for i in range(self.height() + 1):
            for node in self.get_nodes_with_distance(i):
                print(node)
```

## AVL Trees

### Exercise: Building an AVL tree from scratch

```python
class _AVLNode:
    __value: int
    _left_child = None
    _right_child = None
    _height: int = 1

    def __init__(self, value: int):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    @property
    def height(self):
        return self._height

    def __str__(self):
        return str(self.__value)


class AVLTree:
    __root: _AVLNode or None = None

    @property
    def root(self):
        return self.__root

    def insert(self, value: int) -> None:
        """
        Inserts a value into the AVL tree recursively.

        :param value: is the value to be inserted.
        """
        self.__root = self.__insert(self.__root, value)

    def __insert(self, node: _AVLNode, value: int) -> _AVLNode:
        """
        The implementation detail of inserting a value into the AVL tree recursively.

        :param node: is the current node.
        :param value: is the value to be inserted.
        :return: the new _AVLNode with the value.
        """
        # Tree is empty
        if node is None:
            return _AVLNode(value)

        # Determine which subtree to insert the node in
        if value < node.value:
            self.__root._left_child = self.__insert(node.left_child, value)
        else:
            self.__root._right_child = self.__insert(node.right_child, value)

        self.__set_height(node)

        # Balances the node by rotating it the correct way
        return self.__balance(node)

    def __balance(self, node: _AVLNode) -> _AVLNode:
        """
        Balances the AVL tree by determining if it is left-heavy or right-heavy,
        and then using the balance difference to rotate nodes either left or right.

        :param node: is the current node.
        :return: the new balanced node.
        """
        if self.__is_left_heavy(node):
            if self.__get_balance_difference(node.left_child) < 0:
                node._left_child = self.__left_rotate(node.left_child)
            return self.__right_rotate(node)

        if self.__is_right_heavy(node):
            if self.__get_balance_difference(node.right_child) > 0:
                node._right_child = self.__right_rotate(node.right_child)

            return self.__left_rotate(node)

        return node

    def __left_rotate(self, node: _AVLNode) -> _AVLNode:
        """
        Rotates a node left and determines its enw relationship to other nodes.

        :param node: is the current node.
        :return: the rotated node.
        """
        new_root: _AVLNode = node.right_child

        node._right_child = new_root.left_child
        new_root._left_child = node

        self.__set_height(node)
        self.__set_height(new_root)

        return new_root

    def __right_rotate(self, node: _AVLNode) -> _AVLNode:
        """
        Rotates a node right and determines its enw relationship to other nodes.

        :param node: is the current node.
        :return: the rotated node.
        """
        new_root: _AVLNode = node.left_child

        node._left_child = new_root.right_child
        new_root._right_child = node

        self.__set_height(node)
        self.__set_height(new_root)

        return new_root

    def __set_height(self, node: _AVLNode) -> None:
        """
        Sets the height of a node

        :param node: is the node to update the height of.
        """
        node._height = max(
            self.__height(node.left_child),
            self.__height(node.right_child)
        ) + 1

    def __height(self, node: _AVLNode) -> int:
        """
        Calculates the height of a subtree using recursion.

        :param node: is the current node.
        :return: the height of the subtree.
        """

        return 0 if node is None else node.height

    def __get_balance_difference(self, node: _AVLNode) -> int:
        """
        Gets the balance difference of a given node and its subtree(s).

        :param node: is the current node.
        :return: the balance difference.
        """
        return 0 if node is None else \
            self.__height(node.left_child) - self.__height(node.right_child)

    def __is_left_heavy(self, node: _AVLNode) -> bool:
        """
        Checks if a subtree is left-heavy.

        :param node: is the root node of the subtree.
        :return: a boolean value determining if the subtree is left-heavy.
        """
        return self.__get_balance_difference(node) > 1

    def __is_right_heavy(self, node: _AVLNode) -> bool:
        """
        Checks if a subtree is right-heavy.

        :param node: is the root node of the subtree.
        :return: a boolean value determining if the subtree is right-heavy.
        """
        return self.__get_balance_difference(node) < -1
```

## Heaps

### Exercise: Building a heap from scratch

```python
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
```

### Exercise: Heapify an array iteratively

```python
from typing import List


def get_max_item(numbers: List[int], first: int, second: int) -> (int, int):
    """
    Gets the maximum value and corresponding index between two items in a given array.

    :param numbers: is the array of items.
    :param first: is the first item to compare.
    :param second: is the second item to compare.
    :return: a tuple representation of the greater item with the structure: (value, index)
    """
    return (first, numbers.index(first)) \
        if first > second \
        else (second, numbers.index(second))


def heapify(numbers: List[int]) -> None:
    """
    Converts an array of numbers into a max heap in-place.

    :raise AttributeError: if the list is empty.
    :param numbers: is the list of numbers to convert into a heap.
    """
    if len(numbers) == 0:
        raise AttributeError("Cannot heapify an empty list.")

    for i in range(len(numbers) - 2):
        current = numbers[i]
        left_child, right_child = numbers[i + 1], numbers[i + 2]

        if current < left_child or current < right_child:
            # Bubble item to correct index
            max_child, max_child_index = get_max_item(numbers, left_child, right_child)
            numbers[max_child_index] = current
            numbers[i] = max_child
```

### Exercise: Heapify an array recursively

```python
from typing import List


def swap(numbers: List[int], first: int, second: int):
    """
    Swaps two items in a list of numbers.
    :param numbers: is the list of numbers
    :param first: is the first index.
    :param second: is the second index.
    """
    placeholder = numbers[first]
    numbers[first] = numbers[second]
    numbers[second] = placeholder


def _heapify(numbers: List[int], index: int) -> None:
    """
    The implementation detail of converting a list of numbers into a heap recursively in-place.

    :param numbers: is the list of numbers to convert.
    :param index: is the current index.
    """
    # Assume the provided index is the grater index, and then compare later
    larger_index = index

    # Validate left index
    left_index = (index * 2) + 1
    if (left_index < len(numbers)) and (numbers[left_index] > numbers[larger_index]):
        larger_index = left_index

    # Validate right index
    right_index = (index * 2) + 2
    if (right_index < len(numbers)) and (numbers[right_index] > numbers[larger_index]):
        larger_index = right_index

    # Item is in the correct place
    if index == larger_index:
        return

    swap(numbers, index, larger_index)

    # Recursively determine the correct index for each item
    _heapify(numbers, larger_index)


def get_last_parent_index(numbers: List[int]) -> int:
    """
    Gets the last parent index of a list of numbers to convert into a heap.

    The reason we do this is to optimize the algorithm.
    There is no need to recursively call _heapify through the whole list of numbers.
    Rather, we only need to iterate up to the last parent index.

    :param numbers: is the list of numbers.
    :return: the index of the last parent node.
    """
    return (len(numbers) // 2) - 1


def heapify(numbers: List[int]) -> None:
    """
    Converts an array of numbers into a max heap in-place.

    :raise AttributeError: if the list is empty.
    :param numbers: is the list of numbers to convert into a heap.
    """
    if len(numbers) == 0:
        raise AttributeError("List is empty.")

    # See method documentation for get_last_parent_index for the reason why we iterate this way.
    for i in range(get_last_parent_index(numbers), -1, -1):
        _heapify(numbers, i)
```

### Exercise: Priority queue using a heap

```python
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
```

## Tries

### Building a trie from scratch

```python
from typing import List, Dict

ALPHABET_SIZE = 26


class _Node:
    # Optimally, this should be a character, but Python does not support char data type
    _value: str

    # Holds key-value pairs with key: str, value: _Node
    _children = {}
    _is_end_of_word: bool = False

    def __init__(self, value: str):
        self._value = value

    @property
    def children(self):
        return self._children

    def get_children(self) -> List:
        return list(self._children.values())

    def has_no_children(self):
        return len(self._children) == 0

    def __str__(self):
        return self._value

    def has_child(self, key: str) -> bool:
        return key in self._children

    def add_child(self, key: str):
        self._children[key] = _Node(key)

    def get_child(self, key: str):
        return self._children[key]

    def has_children(self) -> bool:
        return not len(self._children) == 0

    @property
    def is_end_of_word(self):
        return self._is_end_of_word

    @property
    def value(self):
        return self._value

    def remove_child(self, key: str):
        if self.has_child(key):
            del self._children[key]


class Trie:
    __root: _Node = _Node(" ")

    def insert(self, word: str):
        """
        Inserts a word into the trie.

        :param word: is the word to insert
        """
        current = self.__root

        for letter in word:
            if not current.has_child(letter):
                current.add_child(letter)

            current = current.get_child(letter)

        current._is_end_of_word = True

    def contains(self, word: str) -> bool:
        """
        Checks if the trie contains the word.

        :param word: is the word to search
        :return: a boolean value determining if the trie contains the word.
        """
        if word is None:
            return False

        current = self.__root

        for letter in word:
            if not current.has_child(letter):
                return False
            current = current.get_child(letter)

        return current.is_end_of_word

    def auto_complete(self, prefix: str) -> List[str]:
        """
        Auto-completes a given prefix based on the nodes present in the trie.
        Example: We have car, card, care and careful in the trie.
        If the prefix equals "car", we get ["car", "card", "care", "careful"].
        If the prefix equals "care", we get ["care", "careful"].

        :param prefix: is the prefix of the words we're looking for.
        :return: a list of string containing the words that fulfills the prefix.
        """
        last_node = self.__find_last_node_of(prefix)

        words: List[str] = []

        self.__auto_complete(last_node, prefix, words)

        return words

    def __find_last_node_of(self, prefix: str) -> _Node or None:
        """
        Gets the last node of a given prefix, or None if it does not exist.

        :param prefix: is the prefix of the given word.
        :return: the last node of the prefix, or None.
        """
        current = self.__root

        for letter in prefix:
            child = current.get_child(letter)
            if child is None:
                return None
            current = child

        return current

    def __auto_complete(self, node: _Node, prefix: str, words: List[str]) -> None:
        """
        The recursive implementation detail of auto-completion.

        :param node: is the current node.
        :param prefix: is the current prefix.
        :param words: is the list of words that fulfill the current prefix.
        """
        if prefix is None:
            return

        if node.is_end_of_word:
            words.append(prefix)

        for child in node.get_children():
            # Add the current value to the prefix
            self.__auto_complete(child, prefix + child.value, words)

    def remove(self, word: str):
        """
        Removes a word from the trie.

        :param word: is the word to remove.
        """
        if word is None:
            return

        self.__remove(self.__root, word, 0)

    def __remove(self, node: _Node, word: str, index: int):
        """
        The implementation detail of removing a word from a trie.

        :param node: is the current node.
        :param word: is the word to remove.
        :param index: is the current index in the word.
        """

        # Base condition
        if index == len(word):
            node._is_end_of_word = False
            return

        current_character = node.get_child(word[index])
        child = node.get_child(current_character)

        if child is None:
            return

        self.__remove(child, word, index + 1)

        # Because this is post-order traversal, we're at the root node
        if (not child.has_children()) and (not child.is_end_of_word):
            node.remove_child(current_character)
```

## Graphs

### Exercise: Building a directed graph from scratch

```python
import random
from typing import List, Dict, Set


class _Node:
    __label: str

    def __init__(self, value: str):
        self.__label = value

    def __str__(self):
        return self.__label

    @property
    def label(self):
        return self.__label


class Graph:
    # Holds key: label, value: _Node object
    __nodes: Dict[str, _Node] = {}

    # This implementation of an adjacency list is somewhat unconventional, but has the same runtime as
    # using an array of linked list objects.
    __adjacency_list: Dict[_Node, List[_Node]] = {}

    def add_node(self, label: str):
        """
        Adds a node to the graph.
        :param label: is the label of the node.
        """
        node = None

        if label not in self.__nodes:
            node = _Node(label)
            self.__nodes[label] = node

        # This means that the label is already in self.__nodes
        if node is None:
            return

        if node not in self.__adjacency_list:
            self.__adjacency_list[node] = []

    def add_edge(self, first: str, second: str):
        """
        Adds a directed edge between two nodes in the graph.
        :param first: is the label of the first node.
        :param second: is the label of the second node.
        """
        first_node = self.__nodes.get(first)
        if first_node is None:
            raise AttributeError("First node is None.")

        second_node = self.__nodes.get(second)
        if second_node is None:
            raise AttributeError("Second node is None.")

        # Add second node to first node's adjacency list
        # Note that this causes us to have a directed graph,
        # because the relationship is not unidirectional.
        self.__adjacency_list.get(first_node).append(second_node)

    def remove_node(self, label: str):
        """
        Removes a node from the graph.
        :param label: is the label of the node to remove.
        """

        node = self.__nodes.get(label)

        if node is None:
            return

        # Remove node's relationships
        for n in self.__adjacency_list.keys():
            connections = self.__adjacency_list.get(n)
            if node in connections:
                connections.remove(node)

        # Remove node
        self.__adjacency_list.pop(node)
        self.__nodes.pop(label)

    def remove_edge(self, first: str, second: str):
        """
        Removes a directed edge between two nodes in the graph.
        :param first: is the label of the first node.
        :param second: is the label of the second node.
        """
        first_node = self.__nodes.get(first)
        if first_node is None:
            return

        second_node = self.__nodes.get(second)
        if second_node is None:
            return

        # Remove relationship from first_node to second_node
        self.__adjacency_list[first_node].remove(second_node)

    def print(self):
        """
        Prints the nodes in the graph and their relationships.
        Note that a Graph class should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """

        # Should look like this:
        # A is connected with [B, C]
        # B is connected with [A]
        for node in self.__adjacency_list.keys():
            connections = self.__adjacency_list[node]
            print(f'{node} is connected with: ', end="")
            for connection in connections:
                print(f'{connection}', end=" ")
            print()

    def traverse_breadth_first(self, start_node_label: str):
        """
        Traverses the graph using the breadth-first algorithm.
        Implemented using a queue and a set of visited nodes.
        :param start_node_label: is the label of the start node.
        """
        if start_node_label not in self.__nodes:
            return

        queue: List[_Node] = []
        visited: Set[_Node] = set()

        node = self.__nodes[start_node_label]
        queue.insert(0, node)

        while len(queue) > 0:
            # Remove first occurrence of current node
            current = queue.pop(0)

            # Node has already been visited
            if current in visited:
                continue

            # Visit current node
            print(f'Current node: {current}')
            visited.add(node)

            # Visit adjacent nodes
            connections = self.__adjacency_list[node]
            for adjacent_node in connections:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)

    def traverse_depth_first_iterative(self, start_node_label: str):
        """
        An iterative implementation of the depth-first traversal algorithm.
        Implemented using a stack and a set of visited nodes.
        :param start_node_label: is the label of the start node.
        """
        if start_node_label not in self.__nodes:
            return

        # Initialize stack that holds nodes in graph
        stack: List[_Node] = []

        # Keep track of visited nodes
        visited: Set[_Node] = set()

        current = self.__nodes[start_node_label]
        stack.append(current)

        # While we still have nodes to visit
        while len(stack) > 0:
            current: _Node = stack.pop()

            # Node has already been visited
            if current in visited:
                continue

            # Visit node
            print(f'Current node: {current}')
            visited.add(current)

            # Visit adjacent nodes
            connections = self.__adjacency_list[current]
            for adjacent_node in connections:
                if adjacent_node not in visited:
                    stack.append(adjacent_node)

    def topological_sort(self) -> List[str]:
        """
        Calculates a topological sort of the graph.
        We use topological sorting when one entity depends on one or more other entities.
        :return: a list of the node labels, in topologically sorted order.
        """
        # Initialize stack that holds nodes in graph
        stack: List[_Node] = []

        # We use a set to determine if we have visited a given node
        visited: Set[_Node] = set()

        for node in self.__nodes.values():
            self.__topological_sort(node, stack, visited)

        # Pop items off the stack and add them in order of topological sort
        sorted: List[str] = []
        while len(stack) > 0:
            sorted.append(stack.pop().label)

        return sorted

    def __topological_sort(self, node: _Node, stack: List[_Node], visited: Set[_Node]):
        """
        The implementation detail of the topological sort, implemented using recursion.
        :param node: is the current node.
        :param stack: is the stack of nodes.
        :param visited: is the set of visited nodes.
        """
        if node in visited:
            return

        visited.add(node)

        connections = self.__adjacency_list[node]
        for adjacent_node in connections:
            self.__topological_sort(adjacent_node, stack, visited)

        # These are the nodes that have the most dependencies
        stack.append(node)

    def traverse_depth_first_recursive(self, start_node_label: str):
        """
        A recursive implementation of the depth-first algorithm.
        :param start_node_label: is the label of the start node.
        """
        if start_node_label not in self.__nodes:
            return

        # We use a set to determine if we have visited a given node
        visited: Set[_Node] = set()

        self.__traverse_depth_first(self.__nodes.get(start_node_label), visited)

    def __traverse_depth_first(self, node: _Node, visited: set):
        """
        The implementation detail of the recursive depth-first algorithm.
        :param node: is the current node.
        :param visited: is the set of visited nodes.
        """
        if node in visited:
            return

        print(f'Current node: {node}')
        visited.add(node)

        connections = self.__adjacency_list[node]

        for adjacent_node in connections:
            if adjacent_node not in visited:
                self.__traverse_depth_first(adjacent_node, visited)

    def has_cycle(self) -> bool:
        """
        Checks if the directed graph has a cycle.
        A depth-first search is used to search for a cycle.
        Example: A -> B -> C -> A is a cyclic directed graph.
        :return: a boolean value determining if the directed graph is cyclic.
        """

        # Add all existing nodes
        all: Set[_Node] = set(self.__nodes.values())

        visiting: Set[_Node] = set()
        visited: Set[_Node] = set()

        while len(all) > 0:
            # Gets a random node to start the depth
            current: _Node = random.choice(list(all))
            if self.__has_cycle(current, all, visiting, visited):
                return True

        return False

    def __has_cycle(self, node: _Node, all: Set[_Node], visiting: Set[_Node], visited: Set[_Node]) -> bool:
        """
        The implementation detail of the has_cycle method.
        :param node: is the current node.
        :param all: is the set of all nodes in the graph.
        :param visiting: is the set of the nodes we currently visit.
        :param visited: is the set of already visited nodes.
        :return: a boolean value determining if the graph is cyclic.
        """
        print(f'Current node: {node}')
        all.remove(node)
        visiting.add(node)

        connections = self.__adjacency_list[node]
        for adjacent_node in connections:
            if adjacent_node in visited:
                continue
            # We have a cycle if the adjacent node is in the visiting set
            if adjacent_node in visiting:
                return True

            if self.__has_cycle(adjacent_node, all, visiting, visited):
                return True

        visiting.remove(node)
        visited.add(node)

        return False
```
