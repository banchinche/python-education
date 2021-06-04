"""
Stack realization module
"""
from typing import Union, Any
from structures.linked_list import LinkedList


class Stack(LinkedList):
    """
    Stack class
    """
    def __init__(self, values: Union[None, list, tuple]) -> None:
        """
        Initializes stack instance
        :param values: nodes
        """
        super(Stack, self).__init__(nodes=reversed(values))

    def __len__(self) -> int:
        """
        Shows size of the stack
        :return: int
        """
        return super(Stack, self).__len__()

    def __str__(self) -> str:
        """
        Shows stack
        :return: str
        """
        return super(Stack, self).__str__()

    def push(self, value: Any) -> None:
        """
        Pushes node to the stack
        :param value: node
        :return: None
        """
        super(Stack, self).prepend(value)

    def pop(self) -> LinkedList.Node:
        """
        Deletes node from the stack and returns it
        :return: node
        """
        popped = self._head
        super(Stack, self).delete(0)
        return popped

    def peek(self) -> LinkedList.Node:
        """
        Returns head of the stack
        :return: node
        """
        return self.head
