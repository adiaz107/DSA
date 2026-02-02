
class LinkedListNode:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __add_to_empty(self, data):
        new_node = LinkedListNode(data)

        self.head = new_node
        self.tail = new_node

    def add_to_front(self, data):
        if self.head is None:
            self.__add_to_empty(data)
            return

        new_node = LinkedListNode(data, next=self.head)
        self.head.prev = new_node

        self.head = new_node

    def remove_from_front(self):
        if self.head is None:
            raise Exception("Cannot remove from front of empty Linked List!")

        removed_value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

        return removed_value

    def add_to_back(self, data):
        if self.head is None:
            self.__add_to_empty(data)
            return

        new_node = LinkedListNode(data)
        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def remove_from_back(self):
        if self.head is None:
            raise Exception("Cannot remove from back of empty Linked List!")

        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None

    def add_to_index(self, data, index):
        if index < 0:
            raise Exception('Cannot add to an index less than zero!')
        elif index == 0:
            self.add_to_front(data)
            return

        itr = self.head
        curr_index = 1
        while itr:
            if curr_index == index:
                new_node = LinkedListNode(data, prev=itr, next=itr.next)

                if itr.next:
                    itr.next.prev = new_node

                itr.next = new_node
                return

            curr_index += 1
            itr = itr.next

        raise Exception(f'Out of bounds! Cannot add at index {index}!')

    def remove_from_index(self, index):
        if self.head is None:
            raise Exception('Cannot remove from empty Linked List!')

        itr = self.head
        curr_index = 0
        while itr:
            if curr_index == index:
                if itr.prev is None and itr.next is None:
                    self.head = None
                    self.tail = None
                elif itr.prev is None:
                    self.head = itr.next
                    self.head.prev = None
                elif itr.next is None:
                    self.tail = itr.prev
                    self.tail.next = None
                else:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev

                return

            curr_index += 1
            itr = itr.next

        raise Exception(f'Out of bounds! Cannot remove from index {index}!')

    def get_index(self, index):
        if index < 0:
            raise Exception('Cannot get value from negative index!')

        itr = self.head
        curr_index = 0
        while itr:
            if curr_index == index:
                return itr.data

            curr_index += 1
            itr = itr.next

        raise Exception(f'Index {index} is not located in the Linked List!')

    def search(self, data):
        itr = self.head
        curr_index = 0
        while itr:
            if itr.data == data:
                return curr_index

            curr_index += 1
            itr = itr.next

        return -1

    def to_list(self):
        ll_as_list = []
        itr = self.head
        while itr:
            ll_as_list.append(itr.data)
            itr = itr.next

        return ll_as_list