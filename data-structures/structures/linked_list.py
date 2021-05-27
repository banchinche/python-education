"""
Linked list realization module
"""
from typing import Union, Any


class LinkedList:
    """
    Linked list class
    """
    class Node:
        """
        Node class
        """
        def __init__(self, value=None, next_value=None) -> None:
            """
            Initializes node instance
            :param value: None or smth
            :param next_value: None or smth
            """
            self.value = value
            self.next_value = next_value

        def __str__(self) -> str:
            """
            str magic method for showing node value
            :return: str
            """
            return f'{self.value}'

    def __init__(self, nodes=None) -> None:
        """
        Initializing linked list instance
        :param nodes: all nodes in list
        """
        self._head = None
        self._tail = None
        if nodes:
            for node in nodes:
                self.append(node)

    def __str__(self) -> str:
        """
        str magic method to show all linked list
        :return: str
        """
        node = self._head
        nodes = ''
        while node.value:
            nodes += f'{node.value}, '
            node = node.next_value
            if not node:
                break
        return nodes.strip(' ,')

    def __len__(self) -> int:
        """
        Shows length of the linked list
        :return: int
        """
        count = 0
        current_node = self._head
        while current_node:
            count += 1
            current_node = current_node.next_value
            if not current_node:
                break
        return count

    def append(self, node: Union[None, Node]) -> None:
        """
        Appends node to linked list (end)
        :param node: it could be any type to store
        :return: None
        """
        node = self.Node(node)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            last_node = self._tail
            last_node.next_value = node
            self._tail = node

    def prepend(self, node: Union[None, Node]) -> None:
        """
        Prepends node to list (begin)
        :param node: it could be any type to store
        :return: None
        """
        node = self.Node(node)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next_value = self._head
            self._head = node

    def lookup(self, value: Any) -> Union[str, int]:
        """
        Shows index of the node in list
        :param value: any
        :return: str or int
        """
        if self.head is None:
            return 'List is empty.'
        current = self._head
        count = 0
        while current:
            if current.value == value:
                return count
            else:
                count += 1
            current = current.next_value

        else:
            print('Not in list.', end=' ')

    def insert(self, value: Any, index: int) -> None:
        """
        Inserts node to list at index position
        :param value: it could be any type to store
        :param index: int
        :return: None
        """
        if index > len(self):
            raise IndexError('Index is out of range!')
        if index == 0:
            self.prepend(value)
        else:
            current = self._head
            count = 0
            while current and count < index:
                if count + 1 == index:
                    after_inserted = current.next_value
                    current.next_value = self.Node(value, after_inserted)
                count += 1
                current = current.next_value

    def delete(self, index: int) -> None:
        """
        Deletes node from list
        :param index: index of the node in list
        :return: None
        """
        if index > len(self):
            raise IndexError('Index is out of range!')
        if index == 0:
            self._head = self._head.next_value
        else:
            current = self._head
            count = 0
            while current and count < index:
                if count + 1 == index:
                    deleted = current.next_value
                    current.next_value = deleted.next_value
                    del deleted
                count += 1
                current = current.next_value

    @property
    def head(self) -> Node:
        """
        Returns head of the linked list
        :return: head node of the list
        """
        return self._head

    @property
    def tail(self) -> Node:
        """
        Returns head of the linked list
        :return: tail of the list
        """
        return self._tail


if __name__ == '__main__':
    linked1 = LinkedList([2, 3, 4])
    print(linked1)
    print(linked1.head, linked1.tail)
    print(len(linked1))
    linked1.append(8)
    print(linked1)
    print(linked1.head, linked1.tail)
    print(len(linked1))
    linked1.prepend(6)
    print(linked1)
    linked1.prepend(1)
    print(linked1)
    linked1.insert(22, 3)
    linked1.insert(44, 0)
    linked1.insert(66, 8)
    print(linked1)
    linked1.delete(0)
    print(linked1)
    linked1.delete(3)
    print(linked1)
    linked1.delete(6)
    print(linked1)
    print(linked1.head, linked1.tail)