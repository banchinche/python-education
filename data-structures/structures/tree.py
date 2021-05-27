"""
Tree realization module
"""
from typing import Union


class Tree:
    """
    Class realized methods for Tree
    """
    class Node:
        """
        Class to represent each node of the Tree
        """
        def __init__(self, value: int) -> None:
            """
            Initialization node instance
            :param value: it will be stored in this node
            """
            self.left = None
            self.data = value
            self.right = None

    def create_node(self, data: int) -> Node:
        """
        Function to create a node
        :param data: value in node
        :return: Node itself
        """
        return self.Node(data)

    def insert(self, node: Union[Node, None], data: int) -> Node:
        """
        Insert function will insert a node into tree
        :param node: node
        :param data: to check node value
        :return: Node
        """
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def delete_node(self, node: Node, data: int) -> Union[None, Node]:
        """
        Delete function will delete a node into tree
        :param node: node
        :param data: to check node value
        :return: None or Node
        """
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp
        return node

    def search(self, node: Node, data: int) -> Union[None, Node]:
        """
        Search function will search a node into tree
        :param node: node
        :param data: to check node value
        :return: None or Node
        """
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def traverse_in_order(self, _root: Node) -> None:
        """
        Traverses tree in order
        :param _root: initial node
        :return: None
        """
        if _root is not None:
            self.traverse_in_order(_root.left)
            print(_root.data)
            self.traverse_in_order(_root.right)

    def traverse_pre_order(self, _root: Node) -> None:
        """
        Traverses tree in order of nesting
        :param _root: initial node
        :return: None
        """
        if _root is not None:
            print(_root.data)
            self.traverse_pre_order(_root.left)
            self.traverse_pre_order(_root.right)

    def traverse_post_order(self, _root: Node) -> None:
        """
        Traverses tree in reverse order
        :param _root: initial node
        :return: None
        """
        if _root is not None:
            self.traverse_post_order(_root.left)
            self.traverse_post_order(_root.right)
            print(_root.data)


if __name__ == '__main__':
    custom_tree = Tree()
    root = custom_tree.insert(None, 100)
    custom_tree.insert(root, 200)
    custom_tree.insert(root, 300)
    custom_tree.insert(root, 400)
    custom_tree.insert(root, 150)
    custom_tree.insert(root, 120)
    custom_tree.insert(root, 550)
    custom_tree.insert(root, 800)
    print("Traverse in order")
    custom_tree.traverse_in_order(root)
    print("Traverse pre order")
    custom_tree.traverse_pre_order(root)
    print("Traverse post order")
    custom_tree.traverse_post_order(root)
