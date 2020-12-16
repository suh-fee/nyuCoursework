# QUESTION 2
# a
def shift(lst, k):
    end = len(lst) - 1
    for shifts in range(k):
        shifter = lst.pop(0)
        lst.insert(end, shifter)

# b
def shift2(lst, k, place = ''):
    if place == '' or place == 'left' or place == 'Left':
        end = len(lst) - 1
        for shifts in range(k):
            shifter = lst.pop(0)
            lst.insert(end, shifter)
    if place == 'right' or place == 'Right':
        end = len(lst) - 1
        for shifts in range(k):
            shifter = lst.pop(end)
            lst.insert(0, shifter)

# QUESTION 3
# a
def squareadder(n):
    sum = 0
    for square in range(n):
        sum += (square ** 2)
    return sum

# b
n = 1 # dummy var to avoid pycharm error notifications
sum([square ** 2 for square in range(n)])

# c
def oddsquareadder(n):
    sum = 0
    for square in range(n):
        if square % 0 != 0:
            sum += (square ** 2)
    return sum

#d

sum([square ** 2 for square in range(n) if square % 2 != 0])

# QUESTION 4
#a
list2 = [10 ** i for i in range(6)]

#b
list3 = [i * (i+1) for i in range(10)]

#c
list4 = [chr(i + 97) for i in range(26)]

# QUESTION 5
#a

def fibs(n):
    lst = []
    for i in range(n):
        if i == 0:
            lst.append(1)
            yield lst[i]
        elif i == 1:
            lst.append(1)
            yield lst[i]
        else:
            lst.append(lst[i-2] + lst[i-1])
            yield lst[i-2] + lst[i-1]

# QUESTION 6

class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] *d
        elif isinstance(d, list):
            self.coords = d

    def __sub__(self, other):
        result = []
        for i in range(len(self.coords)):
            result.append(self.coords[i] - other.coords[i])
        return Vector(result)

    def __len__(self):
        return len(self.coords)

    def __neg__(self):
        result = []
        for i in range(len(self.coords)):
            result.append(self.coords[i] * (-1))
        return Vector(result)

    def __getitem__(self, j):
        return self.coords[j]

    def __mul__(self, other):
        if (isinstance(other, Vector)):
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] * other.coords[i])
            return sum(result)
        elif (isinstance(other, int)):
            result = []
            for i in range(len(self.coords)):
                result.append(self.coords[i] * (other))
            return Vector(result)

    def __rmul__(self, other):
        result = []
        for i in range(len(self.coords)):
            result.append(self.coords[i] * (other))
        return Vector(result)

    def __setitem__(self, j, value):
        self.coords[j] = value

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<' + str(self.coords)[1:(-1)] + '>'

    def __repr__(self):
        return str(self)

