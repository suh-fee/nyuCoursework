# Question 2

class DLL(DoublyLinkedList):  # ignore this part

    # just look at the method below, here
    # add this part to the DoublyLinkedList implementation from class

    def __getitem__(self, ind):

        if 0 <= ind <= len(self) // 2:  # if ind is in first half, start from header

            start = self.header.next  # first node (index 0)
            for i in range(ind):
                start = start.next  # bump the pointer to next

            return start.data

        elif len(self) // 2 < ind < len(self):  # if ind in second half, start from trailer

            start = self.trailer.prev  # last node (index  = len(lst) - 1)
            for i in range(len(self) - 1, ind, -1):  # iterate backwards
                start = start.prev  # bump the pointer backwards

            return start.data

        else:  # out of bounds
            raise IndexError("Index out of range!")
