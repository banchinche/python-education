"""
Graph realization module
"""
from typing import Union
from linked_list import LinkedList


class Graph:
    """
    Graph class
    """
    graph_dict = {}

    def add_edge(self, node: Union[int, str], neighbour: Union[int, str]) -> None:
        """
        Adds edge to graph
        :param node: edge value
        :param neighbour: neighbour value
        :return: None
        """
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self) -> None:
        """
        Prints all edges of the graph
        :return: None
        """
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")

    def find_path(self, start: Union[int, str], end: Union[int, str], path=None) -> \
            Union[list, None]:
        """
        Finds the path from one edge to another
        :param start: start edge
        :param end: end edge
        :param path: initial list to call recursively
        :return: list or None
        """
        if path is None:
            path = list()
        path = path + [start]
        if start == end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None

    def breadth_first_search(self, s: Union[int, str]) -> None:
        """
        Prints sequence of breadth first search
        :param s: start searching edge
        :return: None
        """
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = [s]
        visited[s] = True
        while len(queue) != 0:
            s = queue.pop(0)
            for node in self.graph_dict[s]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
            print(s, end=' ')

    def all_paths(self, start: Union[int, str], end: Union[int, str], path=None) -> list:
        """
        Return all paths from edge to edge
        :param start: start edge
        :param end: end edge
        :param path: initial list to call recursively
        :return: list
        """
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.all_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def shortest_path(self, start: Union[int, str], end: Union[int, str], path=None) -> \
            list:
        """
        Returns shortest path from edge to edge
        :param start: start edge
        :param end: end edge
        :param path: initial list to call recursively
        :return: list
        """
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.shortest_path(node, end, path)
                if new_path:
                    if not shortest or len(shortest) > len(new_path):
                        shortest = new_path
        return shortest

    def depth_first_search(self, s: Union[int, str]) -> None:
        """
        Prints sequence of depth first search
        :param s: start searching edge
        :return: None
        """
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        stack = [s]
        visited[s] = True
        while stack:
            n = stack.pop(len(stack) - 1)
            for i in self.graph_dict[n]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
            print(n, end=' ')


class Node(LinkedList.Node):
    """
    Inheritor of the Node in linked list
    """
    def __init__(self, value=None, next_value=None) -> None:
        """
        Initializes single node
        :param value: value in node
        :param next_value: next node
        """
        super().__init__(value, next_value)

    def __str__(self) -> str:
        """
        Str magic method for showing all chain of nodes in certain edge
        :return: str
        """
        return f'{self.value if self.value else ""} {self.next_value if self.next_value else ""}'


class GraphLinked:
    """
    Graph realization using linked list (nodes)
    """
    def __init__(self, edges: int) -> None:
        """
        Initializes graph
        :param edges: number of the edges in graph
        """
        self.edges = edges
        self.graph = [None] * self.edges

    def add_edge(self, source: int, destination: int) -> None:
        """
        Adds edge to graph
        :param source: source edge
        :param destination: destination edge
        :return: None
        """
        node = Node(destination)
        node.next_value = self.graph[source]
        self.graph[source] = node
        node = Node(source)
        node.next_value = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self) -> None:
        """
        Prints every edge in graph and connections
        :return: None
        """
        for i in range(self.edges):
            temp = self.graph[i]
            if temp:
                print("Adjacency list of vertex {}\n".format(i), end="")
                temp_str = ''
                try:
                    while temp:
                        if temp.value is not None:
                            temp_str += f'{temp.value} >- '
                        temp = temp.next_value
                    temp_str = temp_str[:-3][::-1]
                    print(f'{i} ->{temp_str}')
                    print()
                except AttributeError:
                    pass

    def delete_node(self, value: int) -> None:
        """
        Deletes node from the graph and connections
        :param value: int
        :return: str or None / Node
        """
        self.graph[value] = None
        for node in self.graph:
            while node:
                if node.value == value and node.next_value is None:
                    node.value = None
                node = node.next_value

    def lookup(self, value: int) -> Union[None, Node, str]:
        """
        Finds graph edge with certain value
        :param value: value to find, int
        :return: node or str message
        """
        try:
            if self.graph is not None:
                return self.graph[value]
        except IndexError:
            return 'There is no such edge in graph!'


if __name__ == '__main__':
    g = Graph()
    g.add_edge('1', '2')
    g.add_edge('1', '3')
    g.add_edge('2', '3')
    g.add_edge('2', '1')
    g.add_edge('3', '1')
    g.add_edge('3', '2')
    g.add_edge('3', '4')
    g.add_edge('4', '3')
    g.depth_first_search('1')
    print()
    g.breadth_first_search('1')

    print('Graph implementation using linked list...')
    vertices = 5
    graph = GraphLinked(vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()

    graph.delete_node(0)
    graph.print_graph()

    f = graph.lookup(1)
    d = graph.lookup(2)
    print(f)
    print(d)
