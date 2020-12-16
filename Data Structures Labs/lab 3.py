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

    def __repr__(self):
        dummy = self.data[0:self.n]
        for i in range(len(dummy)):
            dummy[i] = str(dummy[i])
        strng = ', '.join(dummy)
        strng = '[' + strng
        strng = strng + ']'
        return strng

    def __add__(self, other):
        n = self.n + other.n
        final = MyList()
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

    def pop(self):

        if self.n == 1:
            raise IndexError('empty')

        return1 = self[len(self)-1]
        self[len(self)-1] = None

        if self.n < (self.capacity * .25):
            self.capacity /= 2

        return return1

    def __mul__(self, other):
        n = self.n * other
        final = MyList()
        compare = 1

        while n > compare:
            compare *= 2

        final.resize(compare)
        final.n = n
        final.capacity = compare
        multiplier = 0
        for i in range(other):
            for x in range(len(self)):
                final.data[x + (multiplier * (len(self)))] = self.data[x]
            multiplier += 1

        return final

    def __rmul__(self, other):
        n = self.n * other
        final = MyList()
        compare = 1

        while n > compare:
            compare *= 2

        final.resize(compare)
        final.n = n
        final.capacity = compare
        multiplier = 0
        for i in range(other):
            for x in range(len(self)):
                final.data[x + (multiplier * (len(self)))] = self.data[x]
            multiplier += 1

        return final




list = MyList()
list2 = MyList()


for i in range(5):
    list.append(i)

for i in range(3):
    list2.append(i)

list += list2

list2 = list2*2

for i in range(list2.n):
    print(list2.data[i])

print('List2 n:', list2.n, "capacity: ", list2.capacity)

