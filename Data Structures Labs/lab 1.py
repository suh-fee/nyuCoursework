#1

class Polynomial:
    def __init__(self, lst = [0]):
        self.coef = lst
        self.poly = ''
        for degree in range(len(self.coef) - 1, -1, -1):
            if degree == 0:
                self.poly = self.poly + '+' + str(self.coef[degree])
            elif degree == len(self.coef) - 1:
                if self.coef[degree] > 0:
                    self.poly = self.poly + str(self.coef[degree]) + 'x^' + str(degree)
                elif self.coef[degree] < 0:
                    self.poly = self.poly + str(self.coef[degree]) + 'x^' + str(degree)
            elif self.coef[degree] > 0:
                self.poly = self.poly + '+' + str(self.coef[degree]) + 'x^' + str(degree)
            elif self.coef[degree] < 0:
                self.poly = self.poly + str(self.coef[degree]) + 'x^' + str(degree)

    def __repr__(self):
        return self.poly

    def eval(self, val):
        sum = 0
        degree = 0
        for num in self.coef:
            sum += num * (val ** degree)
        return sum

    def __add__(self, other):
        coef1 = self.coef
        coef2 = other.coef
        while len(coef1) != len(coef2):
            if len(coef1) > len(coef2):
                coef2.append(0)
            elif len(coef1) < len(coef2):
                coef1.append(0)
        final_sum = [(coef1[x] + coef2[x]) for x in range(len(coef1))]

        return Polynomial(final_sum)

    def __mul__(self, other):
        coef1 = self.coef
        coef2 = other.coef
        length_new = len(coef1) + len(coef2) -1
        new_coef = []
        for x in range(length_new):
            new_coef.append(0)
        for i in range(len(coef1)):
            for x in range(len(coef2)):
                degree = i + x
                coeff = coef1[i] * coef2[x]
                new_coef[degree] += coeff
        return Polynomial(new_coef)






poly = Polynomial([0,1,5])
poly2 = Polynomial([0,1,3,0,0,0,0,0,2])
print(poly * poly2)

#2

list1 = [2,3,5,6,8,8]
list2 = [list1[x] for x in range(len(list1)) if x % 2 == 0 and list1[x] % 2 == 0]
print(list2)


