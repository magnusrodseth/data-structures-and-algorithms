# Code with Mosh: Data Structures and Algorithms

## The boring stuff 💭

### What is it ❓

This repository serves as a collection of code snippets from "The Ultimate Data Structures and Algorithms", a course by
Code with Mosh. An overview of his courses can be found found [here](https://codewithmosh.com/courses).

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
        self.__array = [0 for item in range(self.__length)]

    def insert(self, item: int) -> bool:
        """
        Inserts an item at the end of the array,
        or the first available spot if the array is not yet filled up.

        :rtype: a boolean value determining whether the operation was successful or not.
        :param item: is the item to be inserted.
        """

        if self.__counter == len(self.__array):
            self.__array = self.__expand_by_1()

        # __counter is inside __array bounds
        try:
            self.__array[self.__counter] = item
            self.__counter += 1

            return True
        except IndexError:
            return False

    def remove_at(self, index: int) -> int:
        """
        Removes the item at the provided index.

        :rtype: the value removed, or -1 if index is out of bounds.
        :param index: is the index of the item to remove.
        """
        if index < 0 or index > len(self.__array) - 1:
            return -1

        removed = self.__array[index]

        new = [0 for i in range(len(self.__array) - 1)]

        counter = 0
        for i in range(len(self.__array)):
            if self.__array[i] != removed:
                new[counter] = self.__array[i]
                counter += 1

        self.__array = new
        self.__counter -= 1

        return removed

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

    def print(self) -> None:
        """
        Prints the content of the array.
        Note that an array should not usually concern itself with printing the content.
        However, for this example, this method is added to the class, for simplicity.
        """
        s = "["

        for i in range(len(self.__array)):
            if i == len(self.__array) - 1:
                s += f'{str(self.__array[i])}'
            else:
                s += f'{str(self.__array[i])}, '

        s += "]"

        print(s)

    def __expand_by_1(self) -> List[int]:
        """
        Copies the existing array, and adds space for 1 item more.

        :rtype: the copied array with space for 1 item more.
        """
        copy = [item for item in self.__array]
        copy.append(0)

        return copy
```