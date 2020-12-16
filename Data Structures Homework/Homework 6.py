import linklist


class LinkedQueue:
    def __init__(self):
        self.que = linklist.DoublyLinkedList()

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
        return self.que.delete_last()

    def first(self):
        return self.que.first_node().data

