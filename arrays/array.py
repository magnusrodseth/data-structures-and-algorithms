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


array = Array(3)

array.print()

array.insert(1)
array.insert(2)
array.insert(3)

array.print()

array.insert(4)

array.print()

reversed = array.reverse()

print(reversed)

array.remove_at(3)

array.print()

index = array.index_of(4)

print(f'Index: {index}')

array.print()

array.remove_at(1)

array.print()

max_value = array.max()

print(f'Max value: {max_value}')

print("-----")

new_array = Array(5)

new_array.insert(1)
new_array.insert(2)
new_array.insert(3)

reversed = array.reverse()

print(reversed)

array.print()

array.insert_at(10, 1)

array.print()
