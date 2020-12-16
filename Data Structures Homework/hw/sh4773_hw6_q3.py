

from DoublyLinkedList import *

class Empty(Exception):
    pass

class CompactString:
    def __init__(self, orig_str):
        if orig_str != '':
            self.info = DoublyLinkedList()
            counter = 1
            compare = orig_str[0]
            for i in range(1, len(orig_str)):
                if orig_str[i] == compare:
                    counter += 1
                else:
                    self.info.add_last((compare, counter))
                    counter = 1
                    compare = orig_str[i]
            self.info.add_last((compare, counter))
        else:
            self.info = DoublyLinkedList()

    def __add__(self, other):
        compare = CompactString('')
        compare2 = CompactString('')

        for i in self.info:
            compare.info.add_last(i)

        for i in other.info:
            compare2.info.add_last(i)

        if compare.info.last_node().data[0] == compare2.info.first_node().data[0]:
            total = compare.info.last_node().data[1] + compare2.info.first_node().data[1]
            compare.info.delete_last()
            compare.info.add_last((compare2.info.first_node().data[0], total))
            compare2.info.delete_first()

        while compare2.info.first_node() != compare2.info.last_node():
            compare.info.add_last(compare2.info.first_node().data)
            compare2.info.delete_first()
        compare.info.add_last(compare2.info.first_node().data)
        compare2.info.delete_first()
        return compare

    def __lt__(self, other):

        comp1 = DoublyLinkedList() # done so that nodes could be deleted w/o altering input nodes
        comp2 = DoublyLinkedList()


        for i in self.info:
            comp1.add_last(i)

        for i in other.info:
            comp2.add_last(i)

        return (self.compare(comp1, comp2))


    def compare(self, input1, input2):

        start1 = input1.first_node().data
        start2 = input2.first_node().data

        if start1[0] != start2[0]:
            if ord(start1[0]) < ord(start2[0]):
                return True
            else:
                return False
        else:
            if start1[1] < start2[1]:
                if input1.first_node() == input1.last_node():
                    return True
                elif input2.first_node() == input2.last_node():
                    return False
                input1.delete_first()
                return self.compare(input1, input2)
            elif start1[1] > start2[1]:
                if input1.first_node() == input1.last_node():
                    return True
                elif input2.first_node() == input2.last_node():
                    return False

                input2.delete_first()
                return self.compare(input1, input2)
            else:
                if input1.first_node().next == input1.trailer:
                    return True
                if input2.first_node().next == input2.trailer:
                    return False
                input1.delete_first()
                input2.delete_first()
                return self.compare(input1, input2)

    def equal(self, input1, input2):
        for x,y in zip(input1, input2):
            if x != y:
                return False
        return True


    def __gt__(self, other):

        comp1 = DoublyLinkedList() # done so that nodes could be deleted w/o altering input nodes
        comp2 = DoublyLinkedList()


        for i in self.info:
            comp1.add_last(i)

        for i in other.info:
            comp2.add_last(i)

        if self.equal(comp1, comp2):
            return False

        return not(self.compare(comp1, comp2))


    def __le__(self, other):

        comp1 = DoublyLinkedList() # done so that nodes could be deleted w/o altering input nodes
        comp2 = DoublyLinkedList()

        for i in self.info:
            comp1.add_last(i)

        for i in other.info:
            comp2.add_last(i)

        if self.equal(comp1, comp2):
            return self.equal(comp1, comp2)

        return (self.compare(comp1, comp2))

    def __ge__(self, other):

        comp1 = DoublyLinkedList() # done so that nodes could be deleted w/o altering input nodes
        comp2 = DoublyLinkedList()

        for i in self.info:
            comp1.add_last(i)

        for i in other.info:
            comp2.add_last(i)

        if self.equal(comp1, comp2):
            return self.equal(comp1, comp2)

        return not(self.compare(comp1, comp2))

    def __repr__(self):
        string = ''

        for i in self.info:
            string += (i[0] * i[1])

        return string




