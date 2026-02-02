
from main import LinkedList

class Stack:

    def __init__(self):
        self.back = LinkedList()
        self.size = 0

    def push(self, data):
        self.back.add_to_front(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception('Cannot pop from empty stack!')

        self.size -= 1
        return self.back.remove_from_front()

    def peek(self):
        if self.size == 0:
            raise Exception('Cannot peek at empty stack!')

        return self.back.get_index(0)

    def clear(self):
        self.back.head = None
        self.back.tail = None
        self.size = 0

    def to_list(self):
        return self.back.to_list()