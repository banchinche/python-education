"""
Queue realization module
"""
from typing import Union, Any
from structures.linked_list import LinkedList


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
