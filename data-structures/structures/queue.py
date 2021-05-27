from linked_list import LinkedList


class Queue(LinkedList):
    def __init__(self, values):
        super(Queue, self).__init__(nodes=values)

    def __len__(self):
        return super(Queue, self).__len__()

    def __str__(self):
        return super(Queue, self).__str__()

    def enqueue(self, value):
        super(Queue, self).append(value)

    def dequeue(self):
        dequeued = self._head
        super(Queue, self).delete(0)
        return dequeued

    def peek(self):
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



