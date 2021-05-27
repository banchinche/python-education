class Tree:
    """Class realized methods for Tree"""
    class Node:
        """class to represent each node of the Tree"""

        def __init__(self, value):
            self.left = None
            self.data = value
            self.right = None

    def create_node(self, data):
        """function to create a node"""
        return self.Node(data)

    def insert(self, node, data):
        """Insert function will insert a node into tree"""
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def delete_node(self, node, data):
        """Delete function will delete a node into tree"""
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

    def search(self, node, data):
        """Search function will search a node into tree"""
        if node is None or node.data == data:
            return node
        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def traverse_in_order(self, t_root):
        """shows the trunk for all branches"""
        if t_root is not None:
            self.traverse_in_order(t_root.left)
            print(t_root.data)
            self.traverse_in_order(t_root.right)

    def traverse_pre_order(self, p_root):
        """traverse function will print all tree in order of nesting"""
        if p_root is not None:
            print(p_root.data)
            self.traverse_pre_order(p_root.left)
            self.traverse_pre_order(p_root.right)

    def traverse_post_order(self, po_root):
        """traverse function will print all the node in the tree in reverse order"""
        if po_root is not None:
            self.traverse_post_order(po_root.left)
            self.traverse_post_order(po_root.right)
            print(po_root.data)


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
