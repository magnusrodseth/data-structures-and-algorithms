from typing import List


class Path:
    __nodes: List[str] = []

    def add(self, node: str):
        self.__nodes.append(node)

    def __str__(self):
        for label in self.__nodes:
            print(label)
