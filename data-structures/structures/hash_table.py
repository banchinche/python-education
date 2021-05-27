"""
Hash-table realization module
"""
from typing import Union, Any


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
        self.values = [None] * self.capacity

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

    def insert(self, key: Union[str, int], value: Any) -> None:
        """
        Inserting value to table
        :param key: key to compute hash
        :param value: new node
        :return:
        """
        self.size += 1
        index = self.hash(key)
        node = self.values[index]
        if node is None:
            self.values[index] = self.Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next_value
        prev.next_value = self.Node(key, value)

    def find(self, key: Union[str, int]) -> Union[None, list]:
        """
        Finds data value based on hash from key
        :param key: key to find hash-index
        :return: list or None
        """
        index = self.hash(key)
        node = self.values[index]
        if node is None:
            return None
        else:
            nodes = []
            while node.value:
                nodes.append(node.value)
                node = node.next_value
                if not node:
                    break
            return nodes

    def remove(self, key: int) -> Any:
        """
        Removes nodes stored at key and returns them
        :param key: key to find hash-index
        :return: None or Node
        """
        index = self.hash(key)
        node = self.values[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next_value
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.values[index] = node.next_value
            else:
                prev.next_value = prev.next_value.next_value
            return result


if __name__ == '__main__':
    ht = HashTable()
    ht.insert(52, 12456)
    ht.insert(52, 234)
    ht.insert(53, 3213)
    ht.insert('41', '21313')
    ht.insert('52', 777)
    print(ht.find(52))
    print(ht.find('52'))
    print(ht.find(53))
    print(ht.remove(52))
    print(ht.remove(52))



