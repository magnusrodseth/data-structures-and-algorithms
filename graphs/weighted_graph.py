import heapq
from typing import Dict, List, Set
import random

from graphs.Path import Path


class _Node:
    __label: str

    def __init__(self, label: str):
        self.__label = label

    def __str__(self):
        return self.__label

    @property
    def label(self):
        return self.__label


class _NodeEntry:
    __node: _Node
    __priority: float

    def __init__(self, node: _Node, priority: float):
        self.__node = node
        self.__priority = priority

    @property
    def node(self):
        return self.__node

    @property
    def priority(self):
        return self.__priority


class _Edge:
    __source: _Node
    __target: _Node
    _weight: int

    def __init__(self, source: _Node, target: _Node, weight: int):
        self.__source = source
        self.__target = target
        self._weight = weight

    def __str__(self):
        return f'{self.__source} -> {self.__target}'

    @property
    def source(self):
        return self.__source

    @property
    def target(self):
        return self.__target

    @property
    def weight(self):
        return self._weight


# Note that this graph is an undirected, weighted graph.
class WeightedGraph:
    # Holds key: label, value: _Node object
    __nodes: Dict[str, _Node] = {}

    __adjacency_list: Dict[_Node, List[_Edge]] = {}

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

    def add_edge(self, first: str, second: str, weight: int = 0):
        """
        Adds a undirected, potentially weighted, edge between two nodes in the graph.
        :param first: is the label of the first node.
        :param second: is the label of the second node.
        :param weight: is the weight of the edge. Defaults to weight = 0.
        """
        first_node = self.__nodes.get(first)
        if first_node is None:
            raise AttributeError("First node is None.")

        second_node = self.__nodes.get(second)
        if second_node is None:
            raise AttributeError("Second node is None.")

        # Because this graph is undirected, the edge relationship must go both ways.
        self.__adjacency_list.get(first_node).append(_Edge(first_node, second_node, weight))
        self.__adjacency_list.get(second_node).append(_Edge(second_node, first_node, weight))

    def get_shortest_path(self, source: str, target: str) -> Path:
        """
        Calculates the shortest distance between two nodes using Dijkstra's algorithm.
        :param source: is the label of the source node.
        :param target: is the label of the target node.
        :return: the shortest distance between source and target node.
        """
        source_node = self.__nodes.get(source)
        if source_node is None:
            raise AttributeError("Source node does not exist.")

        target_node = self.__nodes.get(target)
        if target_node is None:
            raise AttributeError("Target node does not exist.")

        # Holds the shortest distance from start node to the current node
        # Initially populate with each node and a distance of Infinity
        distances: Dict[_Node, float] = dict(
            (node, float('inf')) for node in self.__nodes.values()
        )
        # Set distance equals 0 to find the source node
        distances[source_node] = 0

        # Holds all visited nodes
        visited: Set[_Node] = set()

        # Holds the relationship between the current node and its previous node with shortest distance
        # Initially populate with each node and previous node = None
        previous_nodes: Dict[_Node, _Node or None] = {}

        priority_queue = []
        heapq.heapify(priority_queue)

        priority_queue.append((distances[source_node], source_node))
        heapq.heapify(priority_queue)

        while len(priority_queue) > 0:
            current: _Node = priority_queue.pop()[1]
            visited.add(current)

            # Visit unvisited neighbors
            for edge in self.__adjacency_list[current]:
                if edge.target in visited:
                    continue

                # Calculate distance to unvisited neighbor based on source node and current node
                distance = distances[current] + edge.weight

                # New distance is smaller than previous distance
                if distance < distances[edge.target]:
                    distances[edge.target] = distance

                    # Set next node's previous node to be the current node
                    previous_nodes[edge.target] = current

                    priority_queue.append((distance, edge.target))
                    heapq.heapify(priority_queue)

        return self.__build_path(target_node, previous_nodes)

    def __build_path(self, target_node: _Node, previous_nodes: Dict[_Node, _Node]) -> Path:
        # Initially populate the stack with the target node
        stack: List[_Node] = [target_node]
        previous = previous_nodes.get(target_node)

        while previous:
            stack.append(previous)
            previous = previous_nodes.get(previous)

        path = Path()
        while len(stack) > 0:
            path.add(stack.pop().label)

        return path

    def has_cycle(self) -> bool:
        visited: Set[_Node] = set()
        for node in self.__nodes.values():
            if (node not in visited) and (self.__has_cycle(visited, None, node)):
                return True
        return False

    def __has_cycle(self, visited: Set[_Node], previous: _Node or None, node: _Node) -> bool:
        visited.add(node)

        connections = self.__adjacency_list.get(node)
        for edge in connections:
            # In this case, this target node is the one we came from
            if edge.target == previous:
                continue

            if edge.target in visited:
                return True

            # Pass current node as previous to detect potential cycle
            if self.__has_cycle(visited, node, edge.target):
                return True

        # In this case, we did not find a cycle
        return False

    def get_minimum_spanning_tree(self):
        tree: WeightedGraph = WeightedGraph()

        edges = []
        heapq.heapify(edges)

        if len(self.__nodes) == 0:
            return tree

        start_node: _Node = random.choice(list(self.__nodes.values()))
        current_connections = self.__adjacency_list.get(start_node)
        for edge in current_connections:
            edges.append((edge.weight, edge))
            heapq.heapify(edges)

        tree.add_node(start_node.label)

        if len(edges) == 0:
            return tree

        # As long as our tree doesn't contains all nodes in the graph
        while len(tree.__nodes) < len(self.__nodes):
            # Pick edge with minimum weight from the queue
            minimum_edge = edges.pop()
            next_node = minimum_edge.target

            # Continue if the edge is currently connected to a node that exists in the tree
            # in order to prevent a cyclic graph
            if next_node in tree:
                continue

            # Add target node and edge to the tree
            tree.add_node(next_node.label)
            tree.add_edge(minimum_edge.source.label, next_node.label, minimum_edge.weight)

            # Add all edges connected to the target node to the priority queue.
            # We are only interested in the edges that connect to an unvisited node.
            next_connections = self.__adjacency_list[next_node]
            for edge in next_connections:
                if edge.target not in tree:
                    edges.append((edge.weight, edge))
                    heapq.heapify(edges)

        return tree

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
                print(f'{connection}', end=" | ")
            print()


if __name__ == '__main__':
    graph = WeightedGraph()

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B", 3)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 5)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "C", 2)

    tree = graph.get_minimum_spanning_tree()

    tree.print()
