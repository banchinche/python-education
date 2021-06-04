"""
Graph realization module
"""
from typing import Any, Union
from structures.linked_list import LinkedList


class Graph:
    """
    Graph class
    """
    class Vertex:
        """
        Vertex class
        """
        def __init__(self, value: Any) -> None:
            """
            Initializes vertex
            :param value: vertex value
            """
            self.value = value
            self.adjacency_list = LinkedList()

        def add_edge(self, node: Any) -> None:
            """
             Add edge to the given node
             :param node: Node itself
             :return: None
             """
            self.adjacency_list.append(node)
            node.adjacency_list.append(self)

        def delete_edge(self, edge_value: Any) -> None:
            """
         Deletes references for the given node

         :param edge_value: Value of the vertex to be deleted
         :return: None
         """
            index = self.adjacency_list.lookup(edge_value)
            self.adjacency_list.delete(index)

        def __str__(self) -> str:
            """
            Str magic method for vertex
            :return: str
            """
            return f'Vertex : {self.value}'

    def __init__(self) -> None:
        """
        Initializes graph instance
        """
        self.edges = LinkedList()

    def insert(self, node_value: Any, adj_list: list) -> None:
        """
         Inserts new vertex with given value
         :param node_value: value to be inserted in the new vertex
         :param adj_list: list of edges between vertices
         :return: None
        """
        new_node = self.Vertex(node_value)
        for item in adj_list:
            node = self.lookup(item)
            if node is None:
                node = self.Vertex(item)
            new_node.add_edge(node)
            self.edges.append(node)
        self.edges.append(new_node)

    def lookup(self, value) -> Union[None, Vertex]:
        """
         Returns reference of the vertex with given value
         :param value: node value
         :return: link on vertex or None
         """
        for node in self:
            if node.value == value:
                return node
        return None

    def delete(self, deletion_node: Vertex) -> None:
        """
        Deletes vertex with given link
        :param deletion_node: deleted vertex
        :return: None
        """
        if deletion_node is None:
            return
        adj_nodes = deletion_node.adjacency_list
        for node in adj_nodes:
            node.value.delete_edge(deletion_node)
        self.edges.delete(self.edges.lookup(deletion_node))

    def __str__(self) -> str:
        """
        Str magic method for graph
        :return:
        """
        return f"{self.edges}"

    def __iter__(self) -> Vertex:
        """
        For iterates over graph
        :return: vertex instance
        """
        nodes_list = self.edges
        for node in nodes_list:
            yield node
