# question 1

import ctypes

def make_array(n):
    return (n*ctypes.py_object)()

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
        return self.data[0]



def postfix_calculator(inputs, dict):
    stack = ArrayStack()
    dict = dict
    for a in inputs:
        if type(a) is int:
            stack.push(a)
            continue
        elif a in dict:
            stack.push(a)
            continue
        num1 = stack.pop()
        num2 = stack.pop()

        if num1 in dict:
            num1 = dict[num1]

        if num2 in dict:
            num2 = dict[num2]

        if a == '+':
            stack.push(num2 + num1)
        elif a == '-':
            stack.push(num2 - num1)
        elif a == '*':
            stack.push(num2 * num1)
        elif a == '/':
            stack.push(num2 / num1)

    return stack.pop()

def main():
    values = {}
    while True:
        inp = input('--> ')


        if inp == 'done()':
            break
        list1 = inp.split(' ')

        for i in range(len(list1)):
            if ord(list1[i]) < 58 and ord(list1[i]) > 47:
                list1[i] = int(list1[i])

        if len(list1) > 1:
            if list1[1] == '=':
                newlist = list1[2:]
                values[list1[0]] = postfix_calculator(newlist, values)
                print(list1[0])
            else:
                print(postfix_calculator(list1, values))
        else:
            print(values[inp])

main()








# question 2


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maxi = ''

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self) == 0:
            return True

        else:
            return False

    def push(self, elem):
        if self.maxi == '':
            self.maxi = elem

        elif self.maxi < elem:
            self.maxi = elem

        self.data.push((elem, self.maxi))

    def pop(self):
        if (self.is_empty()):
            raise Exception('Stack is empty bruh bruh')
        self.maxi = self.data.data[len(self) - 2][1]
        return self.data.pop()

    def top(self):
        if (self.is_empty()):
            raise Exception('Stack is empty bruh bruh')
        return self.data.data[0]

    def max(self):
        return self.maxi

# question 3

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, val):
        self.data.append(val)
    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]
    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()


class ArrayQueue:
    INITIAL_CAPACITY = 10
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return (self.num_of_elems == 0)
    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1
    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


class ArrayDeque:
    INITIAL_CAPACITY = 10
    def __init__(self):
        self.front_ind = 0
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return (self.num_of_elems == 0)
    def add_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1
    def add_last(self, e):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = e
        self.num_of_elems += 1
    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val
    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[self.front_ind]
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[(self.front_ind + self.num_of_elems - 1) % (len(self.data))]
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.queue = ArrayDeque()

    def is_empty(self):
        return self.queue.is_empty()

    def __len__(self):
        return len(self.queue)

    def push(self, elem):
        self.queue.add_last(elem)

    def top(self):
        return self.queue.last()

    def pop(self):
        return self.queue.delete_last()

    def mid_push(self, elem):
        new_q = ArrayDeque()
        new_q.add_first(elem)
        if len(self) % 2 == 0:
            length = len(self) // 2
            for i in range(length):
                self.stack.push(self.queue.delete_last())
            for i in range(length):
                new_q.add_last(self.stack.pop())
            for i in range(length):
                self.stack.push(self.queue.delete_first())
            for i in range(length):
                new_q.add_first(self.stack.pop())
        else:
            length = len(self) // 2
            for i in range(length):
                self.stack.push(self.queue.delete_last())
            for i in range(length):
                new_q.add_last(self.stack.pop())
            for i in range(length+1):
                self.stack.push(self.queue.delete_first())
            for i in range(length+1):
                new_q.add_first(self.stack.pop())

        self.queue = new_q
        self.stack = ArrayStack()