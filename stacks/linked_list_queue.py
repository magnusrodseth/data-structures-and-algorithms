from linked_lists.linked_list import LinkedList


class LinkedListQueue:
    __linked_list: LinkedList = LinkedList()

    def enqueue(self, item: int):
        self.__linked_list.add_last(item)

    def dequeue(self):
        self.__linked_list.remove_first()

    def peek(self) -> int:
        return self.__linked_list.get_nth_node_from_end(self.__linked_list.size()).value

    def size(self) -> int:
        return self.__linked_list.size()

    def is_empty(self) -> bool:
        return self.__linked_list.is_empty()

    def print(self):
        print(self.__linked_list.to_array())


if __name__ == '__main__':
    queue = LinkedListQueue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.dequeue()

    queue.print()
