# homework 3

# question 2

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        self.data[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, iterable_collection):
        for elem in iterable_collection:
            self.append(elem)

    def insert(self, index, val):
        if (not(0 <= index <= (self.n - 1))):
            raise IndexError("invalid index")
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        for i in range(len(self), index, -1):
            self.data[i] = self.data[i-1]
        self.n += 1
        self.data[index] = val

    def pop(self):

        if self.n == 1:
            raise IndexError('empty')

        return1 = self[len(self)-1]
        self[len(self)-1] = None

        if self.n < (self.capacity * .25):
            self.capacity /= 2

        return return1



def find_duplicates(lst):
    max = lst[0]

    for i in lst:
        if i > max:
            max = i
    list0 = [0]
    list1 = list0 * (max + 1)
    for i in range(len(lst)):
        number = lst[i]
        list1[number] += 1

    final_counter = 0
    for i in list1:
        if i != 0 and i != 1:
            final_counter += 1

    final_list = list0 * final_counter

    final_counter = 0

    for i in range(len(list1)):
        if list1[i] != 0 and list1[i] != 1:
            final_list[final_counter] = i
            final_counter += 1

    return final_list



def remove_all(lst,value):
    num_of_val = 0
    for i in range(len(lst)):
        if lst[i] == value:
            num_of_val += 1

    list1 = [''] * num_of_val
    num_of_val = 0

    for i in range(len(lst)):
        if lst[i] == value:
            list1[num_of_val] = i
            num_of_val += 1
            lst[i] = ''

    for i in list1:
        lst.pop(i)

