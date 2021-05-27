class HashTable:
    BASE_MAX_SIZE = 100

    class Node:
        def __init__(self, key, value=None, next_value=None):
            self.key = key
            self.value = value
            self.next_value = next_value

    def __init__(self):
        self.capacity = self.BASE_MAX_SIZE
        self.size = 0
        self.values = [None] * self.capacity

    def hash(self, key):
        if isinstance(key, str):
            _hash = 0
            for idx, c in enumerate(key):
                _hash += (idx + len(key)) ** ord(c)
                _hash = _hash % self.capacity
            return _hash
        elif isinstance(key, int):
            return key % self.capacity

    # Insert a key,value pair to the hashtable
    # Input:  key - string
    # 		  value - anything
    # Output: void
    def insert(self, key, value):
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

    # Find a data value based on key
    # Input:  key - string
    # Output: value stored under "key" or None if not found
    def find(self, key):
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

    # Remove node stored at key
    # Input:  key - string
    # Output: removed data value or None if not found
    def remove(self, key):
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



