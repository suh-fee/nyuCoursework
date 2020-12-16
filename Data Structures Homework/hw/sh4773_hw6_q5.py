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



def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    fin = DoublyLinkedList()
    compare1 = DoublyLinkedList()
    compare2 = DoublyLinkedList()

    for i in srt_lnk_lst1:
        compare1.add_last(i)

    for i in srt_lnk_lst2:
        compare2.add_last(i)

    if compare1.first_node().data < compare2.first_node().data:
        fin.add_last(compare1.first_node().data)
        compare1.delete_first()

    elif compare1.first_node().data > compare2.first_node().data:
        fin.add_last(compare2.first_node().data)
        compare2.delete_first()

    else:
        fin.add_last(compare2.first_node().data)
        compare2.delete_first()
        fin.add_last(compare1.first_node().data)
        compare1.delete_first()

    return merge_sublists(fin, compare1, compare2)


def merge_sublists(output, input1, input2):

    if input1.first_node().next == input1.trailer and input2.first_node().next == input2.trailer:
        if input1.first_node().data < input2.first_node().data:
            output.add_last(input1.first_node().data)
            output.add_last(input2.first_node().data)
            return output
        elif input1.first_node().data > input2.first_node().data:
            output.add_last(input2.first_node().data)
            output.add_last(input1.first_node().data)
            return output


        output.add_last(input1.first_node().data)
        output.add_last(input1.first_node().data)
        return output

    elif input1.first_node().next == input1.trailer:

        if input1.first_node().data < input2.first_node().data:
            output.add_last(input1.first_node().data)

            for i in input2:
                output.add_last(i)
                return output



    elif input2.first_node().next == input2.trailer:

        if input2.first_node().data < input1.first_node().data:
            output.add_last(input2.first_node().data)

            for i in input1:
                output.add_last(i)
                return output

    if input1.first_node().data < input2.first_node().data:
        output.add_last(input1.first_node().data)
        input1.delete_first()
        return merge_sublists(output, input1, input2)

    elif input2.first_node().data < input1.first_node().data:
        output.add_last(input2.first_node().data)
        input2.delete_first()
        return merge_sublists(output, input1, input2)

    else:
        output.add_last(input1.first_node().data)
        output.add_last(input1.first_node().data)
        input1.delete_first()
        input2.delete_first()
        return merge_sublists(output, input1, input2)

def main():
    ex1 = DoublyLinkedList()
    ex2 = DoublyLinkedList()
    ex1.add_last(1)
    ex1.add_last(3)
    ex1.add_last(5)
    ex1.add_last(6)
    ex1.add_last(8)
    ex2.add_last(2)
    ex2.add_last(3)
    ex2.add_last(5)
    ex2.add_last(10)
    ex2.add_last(15)
    ex2.add_last(18)
    ex3 = merge_linked_lists(ex1,ex2)

    print(ex3.header.next.next.next.next.next.next.next.next.next.data)


main()
