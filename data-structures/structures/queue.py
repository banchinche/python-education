"""
Queue realization module
"""
from typing import Union, Any
from linked_list import LinkedList


class Queue(LinkedList):
    """
    Queue class
    """
    def __init__(self, values: Union[None, list, tuple]) -> None:
        """
        Initialization of the queue instance
        :param values: nodes
        """
        super(Queue, self).__init__(nodes=values)

    def __len__(self) -> int:
        """
        Returns size of the queue
        :return: int
        """
        return super(Queue, self).__len__()

    def __str__(self) -> str:
        """
        Returns view of the queue
        :return: str
        """
        return super(Queue, self).__str__()

    def enqueue(self, value: Any) -> None:
        """
        Appends node to the queue
        :param value: node
        :return: None
        """
        super(Queue, self).append(value)

    def dequeue(self) -> LinkedList.Node:
        """
        Deletes from the queue and returns this node
        :return: node
        """
        dequeued = self._head
        super(Queue, self).delete(0)
        return dequeued

    def peek(self):
        """
        Shows peek of the queue
        :return: node
        """
        return self.head


if __name__ == '__main__':
    queque1 = Queue([2, 3, 4])
    print(queque1)
    print(len(queque1))
    print(queque1.dequeue())
    print(queque1)
    queque1.enqueue(7)
    print(queque1.peek())
    print(queque1)
    print(queque1.dequeue())
    print(queque1.dequeue())



