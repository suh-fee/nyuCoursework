
# runtimes
# a: constant
# b: constant
# c: constant
# d: constant
# e: constant
# f: constant
# g: constant
# h: constant
# i: constant
# j: constant
# k: constant

# 2:
# it puts the string into a DLL, and it goes through it and deletes the vowels

# 3. 3, 2, 5, 8, 12, 6
# -------
#
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"



# 1

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def push(self, data):
        self.data.add_last(data)

    def pop(self, data):
        return self.data.delete_last()

    def top(self, data):
        return self.data.last_node()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

# 2

class LeakyStack:
    def __init__(self, limit):
        self.data = DoublyLinkedList()
        self.limit = limit

    def push(self, data):
        if len(self.data) < self.limit:
            self.data.add_last(data)
        else:
            self.data.add_last(data)
            self.data.delete_first()

    def pop(self, data):
        return self.data.delete_last()

    def top(self, data):
        return self.data.last_node()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

# 3

def sum_lnk_list(lnk_lst):
    if len(lnk_lst) == 1:
        return lnk_lst.first_node().data
    else:
        sum = lnk_lst.first_node().data
        lnk_lst.delete_first()
        return sum + sum_lnk_list(lnk_lst)

# 4

def reverse_list_change_elements_order(lnk_lst):
    first = lnk_lst.first_node()
    last = lnk_lst.last_node()
    for i in range(len(lnk_lst) // 2):
        first.data, last.data = last.data, first.data
        first = first.next
        last = last.prev

def reverse_list_change_nodes_order(lnk_lst):
    curr = lnk_lst.first_node()
    while curr.data != None:
        temp = curr.next
        curr.next = curr.prev
        curr.prev = temp
        curr = curr.prev

    temp = lnk_lst.header.next
    lnk_lst.header.next = lnk_lst.trailer.prev
    lnk_lst.trailer.prev = temp

    lnk_lst.last_node().next = lnk_lst.trailer

lnk = DoublyLinkedList()
lnk.add_first(1)
lnk.add_last(2)
lnk.add_last(3)
lnk.add_last(4)
lnk.add_last(5)

reverse_list_change_nodes_order(lnk)

# print(lnk)
#
# for elem in lnk:
#     print(elem, end='')
print(lnk)
# print(lnk.first_node().data, lnk.first_node().next.data,lnk.first_node().next.next.data, lnk.first_node().next.next.next.data,lnk.first_node().next.next.next.next.data, lnk.first_node().next.next.next.next.next.data,lnk.first_node().next.next.next.next.next.next.data)