# q 1

from DoublyLinkedList import *

class Empty(Exception):
    pass

class LinkedQueue:
    def __init__(self):
        self.que = DoublyLinkedList()

    def __len__(self):
        return len(self.que)

    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def enqueue(self, elem):
        self.que.add_first(elem)

    def dequeue(self):
        if len(self) == 0:
            raise Empty('Empty')
        temp = self.que.last_node().data
        self.que.delete_last()
        return temp

    def first(self):
        return self.que.first_node().data