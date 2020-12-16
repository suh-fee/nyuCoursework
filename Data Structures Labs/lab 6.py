# 1

def powers_of_two(num):
    for i in range(1, num + 1):
        yield 2 ** i



# 2

def nested(lst):
    sum = 0
    for i in lst:
        if type(i) == list:
            sum += nested(i)
        elif type(i) == int:
            sum += i
    return sum

# 3

def sort_first(lst):
    compare = lst[0]
    dif = 0

    for i in range(len(lst)):

        if lst[i-dif] < compare:
            drop = lst.pop(i-dif)
            lst.insert(0, drop)

        elif lst[i-dif] > compare:
            drop = lst.pop(i-dif)
            lst.append(drop)
            dif += 1

list1 = [25,10,16,76,1200,4,2,70,1]

def sort(lst):
    compare = lst[0]
    big = 1
    small = len(lst) - 1
    while big < small:
        if lst[big] < compare:
            big += 1
        if lst[small] > compare:
            small -= 1
        comp2 = lst[big]
        if lst[big] > compare and lst[small] < compare:
            lst[big] = compare
            lst[0] = comp2



sort(list1)
print(list1)


# 4
import ctypes

def make_array(n):
    return (n * ctypes.py_object)()

class MyString:
    def __init__(self, initial_str=''):
        self.n = len(initial_str)
        capacity = 1
        comp = len(initial_str)
        while comp > capacity:
            capacity *= 2

        self.data = make_array(capacity)
        self.capacity = capacity

        for i in range(len(initial_str)):
            self.data[i] = initial_str[i]

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (len(self) * (-1)) <= ind <= (0):
            index = self.n + ind
            return self.data[index]

        elif (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (len(self) * (-1)) <= ind <= (0):
            index = self.n + ind
            self.data[index] = val
        elif (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        self.data[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def __repr__(self):
        strng = ''
        for i in range(self.n):
            strng += self.data[i]
        return strng

    def __add__(self, other):
        n = self.n + other.n
        final = MyString()
        compare = 1

        while n > compare:
            compare *= 2

        final.resize(compare)
        final.n = n

        for i in range(self.n):
            final.data[i] = self.data[i]

        for i in range(other.n):
            final.data[i + self.n] = other.data[i]

        return final

    def __radd__(self, other):
        n = self.n + other.n
        final = MyString()
        compare = 1

        while n > compare:
            compare *= 2

        final.resize(compare)
        final.n = n

        for i in range(self.n):
            final.data[i] = self.data[i]

        for i in range(other.n):
            final.data[i + self.n] = other.data[i]

        return final

    def __iadd__(self, other):
        comp = self.n + other.n
        capacity = 1

        while comp > capacity:
            capacity *= 2

        self.resize(capacity)


        for i in range(other.n):
            self.data[i + self.n] = other.data[i]

        self.n += other.n
        return self

    def upper(self):
        for i in range(self.n):
            self.data[i] = self.data[i].upper()

