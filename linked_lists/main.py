from linked_lists.linked_list import LinkedList


def main():
    list = LinkedList()

    list.add_last(10)
    list.add_last(20)
    list.add_last(30)
    list.add_last(40)
    list.add_last(50)
    list.add_last(60)

    nth_node = list.get_nth_node_from_end(0)
    print(f'nth node: {nth_node.value}')

    regular = list.to_array()
    print(regular)

    print("Done.")


if __name__ == '__main__':
    # Use the debugger to inspect the object relationships
    main()
