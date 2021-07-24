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


if __name__ == '__main__':
    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")

    graph.add_edge("D", "A")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")

    # graph.print()
    has_cycle = graph.has_cycle()
    print(has_cycle)
