from linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self, values):
        super(Stack, self).__init__(nodes=reversed(values))

    def __len__(self):
        return super(Stack, self).__len__()

    def __str__(self):
        return super(Stack, self).__str__()

    def push(self, value):
        super(Stack, self).prepend(value)

    def pop(self):
        popped = self._head
        super(Stack, self).delete(0)
        return popped

    def peek(self):
        return self.head


if __name__ == '__main__':
    stack1 = Stack([2, 4, 5])
    print(stack1)
    print(stack1.peek())
    stack1.push(22)
    print(stack1)
    print(len(stack1))
    print(stack1.pop())

