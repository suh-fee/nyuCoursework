from DoublyLinkedList import *

class Empty(Exception):
    pass

class Integer:
    def __init__(self, num_str):
        self.str = num_str
        self.data = DoublyLinkedList()

        for i in range(len(num_str)):
            self.data.add_last(self.str[i])


    def __add__(self, other):

        start1 = self.data.last_node()
        start2 = other.data.last_node()
        status = True

        multiple = 0
        sum1 = 0
        carry = 0

        while status:

            temp = int(start1.data) + int(start2.data) + carry

            carry = temp // 10

            temp = temp % 10

            sum1 += temp * (10**multiple)

            multiple += 1

            start1 = start1.prev
            start2 = start2.prev

            status = (start1.data != None) and (start2.data != None)

        if len(self.data) > len(other.data):

            status = True


            while status:

                temp = int(start1.data) + carry

                carry = temp // 10
                temp = temp % 10

                sum1 += temp * (10**multiple)

                multiple += 1

                start1 = start1.prev
                status = (start1.data != None)

        elif len(self.data) < len(other.data):

            status = True


            while status:

                temp = int(start2.data) + carry

                carry = temp // 10
                temp = temp % 10

                sum1 += temp * (10 ** multiple)

                multiple += 1

                start2 = start2.prev
                status = (start2.data != None)
        if carry != 0:
            sum1 += carry * (10 ** multiple)

        fin = Integer(str(sum1))

        return fin

    def __mul__(self, other):
        pass


    def __repr__(self):
        return self.str


