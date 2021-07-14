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


if __name__ == '__main__':
    avl_tree = AVLTree()

    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
