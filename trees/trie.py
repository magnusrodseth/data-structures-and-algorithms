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


if __name__ == '__main__':
    trie = Trie()

    trie.insert("car")
    trie.insert("card")
    trie.insert("care")
    trie.insert("careful")
    trie.insert("egg")

    words = trie.auto_complete("car")

    print(words)
