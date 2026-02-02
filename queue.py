
from main import LinkedList

class Queue:

    def __init__(self):
        self.back = LinkedList()
        self.size = 0

    def enqueue(self, data):
        self.back.add_to_back(data)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Cannot remove from empty queue!")

        self.back.remove_from_front()
        self.size -= 1

    def top(self):
        if self.size == 0:
            raise Exception("Cannot get top value from an empty queue!")

        return self.back.head.data

    def clear(self):
        self.back.head = None
        self.back.tail = None
        self.size = 0

    def to_list(self):
        return self.back.to_list()

