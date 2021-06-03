"""
Hash-table realization module
"""
from typing import Union, Any
from structures.linked_list import LinkedList


class HashTable:
    """
    Hash-table class
    """
    BASE_MAX_SIZE = 100

    class Node:
        """
        Node class
        """
        def __init__(self, key: int, value=None, next_value=None) -> None:
            """
            Initialization of the node instance
            :param key: key
            :param value: None or smth
            :param next_value: node
            """
            self.key = key
            self.value = value
            self.next_value = next_value

    def __init__(self) -> None:
        """
        Initialization of the hash-table instance
        """
        self.capacity = self.BASE_MAX_SIZE
        self.size = 0
        self.list = LinkedList()
        for _ in range(self.capacity):
            self.list.append(LinkedList())

    def hash(self, key: int) -> int:
        """
        Hash function
        :param key: key to compute hash
        :return: hash - int
        """
        if isinstance(key, str):
            _hash = 0
            for idx, c in enumerate(key):
                _hash += (idx + len(key)) ** ord(c)
                _hash = _hash % self.capacity
            return _hash
        elif isinstance(key, int):
            return key % self.capacity

    def insert(self, key: Union[int, str], value: Any) -> None:
        """
        Inserts value to hash-table with certain key
        :param key: int or str
        :param value: Any
        :return: None
        """
        index = self.hash(key)
        self.list[index].value.append(value)

    def lookup(self, key: Union[int, str]) -> LinkedList:
        """
        Returns LinkedList with certain key in hash-table
        :param key: int or str
        :return: LinkedList
        """
        index = self.hash(key)
        return self.list[index]

    def delete(self, key: Union[int, str], value=None) -> None:
        """
        Deletes value in hash-table with certain key
        :param key: int or str
        :param value: Any
        :return: None
        """
        index = self.hash(key)
        if value is None:
            self.list.delete(index)
        value_index = self.list[index].value.lookup(value)
        self.list[index].value.delete(value_index)
