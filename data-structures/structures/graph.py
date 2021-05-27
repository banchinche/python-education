"""
Graph realization module
"""
from typing import Union


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
