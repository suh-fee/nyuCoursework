class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self) == 0:
            return True

        else:
            return False

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if (self.is_empty()):
            raise Exception('Stack is empty bruh bruh')
        return self.data.pop()

    def top(self):
        if (self.is_empty()):
            raise Exception('Stack is empty bruh bruh')
        return self.data[-1]

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



class DupStack:
    def __init__(self):
        self.data = ArrayStack()
        self.capacity = 0
    def __len__(self):
        return self.capacity

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        if self.is_empty():
            self.data.push((e, 1))
            self.capacity += 1
        else:
            if self.data.top()[0] == e:
                temp = self.data.top()[1]
                self.data.pop()
                self.data.push((e, temp+1))
                self.capacity += 1
            else:
                self.data.push((e, 1))
                self.capacity += 1


    def top(self):
        if (self.is_empty()):
            raise ValueError('empty')
        return self.data.top()[0]

    def top_dups_count(self):
        if (self.is_empty()):
            raise ValueError('empty')
        return self.data.top()[1]

    def pop(self):
        if (self.is_empty()):
            raise ValueError('empty')

        temp = self.data.top()[0]

        if self.data.top()[1] > 1:

            temp2 = self.data.top()[1] - 1
            self.data.pop()
            self.data.push((temp, temp2))
            self.capacity -= 1

        else:
            self.capacity -= 1
            self.data.pop()

        return temp

    def pop_dups(self):
        if (self.is_empty()):
            raise ValueError('empty')
        self.capacity -= self.data.top()[1]
        return self.data.pop()[0]


def insert_sorted(srt, elem):
    first = srt.first_node()
    second = first.next

    if elem < first.data:
        node = DoublyLinkedList.Node(elem, srt.header, srt.first_node())
        first.prev = node
        srt.header.next = node

    elif elem > srt.last_node().data:
        node = DoublyLinkedList.Node(elem, srt.last_node(), srt.trailer)
        srt.last_node().next = node
        srt.trailer.prev = node

    status = True
    while first != srt.last_node() and status:

        if first.data < elem and second.data > elem:
            node = DoublyLinkedList.Node(elem, first, second)
            first.next = node
            second.prev = node
            status = False

        else:
            first = first.next
            second = second.next

def main():
    list = DoublyLinkedList()
    list.add_first(1)
    list.add_last(2)
    list.add_last(4)
    list.add_last(5)
    insert_sorted(list, 6)
    print(list)

main()