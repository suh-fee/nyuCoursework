class BinaryPositiveInteger:
    def __init__(self, num):
        self.BinaryNumber = '1'
        temp = num
        i = 0
        if num == 0:
            self.BinaryNumber = '0b0'
        while num >= 2**i:
            i += 1
        i -= 1
        temp -= 2**i
        for j in range(i-1,-1,-1):
            if temp - 2**j >= 0:
                self.BinaryNumber += '1'
                temp -= 2**j
            else:
                self.BinaryNumber += '0'
        self.BinaryNumber = "0b" + self.BinaryNumber
        #initialize bin with integer given
    def __add__(self, other):
        self.n1 = self.BinaryNumber[2:]
        self.n2 = other.BinaryNumber[2:]

        n3 = ""
        carry = False
        if len(self.n1) > len(self.n2):
            short = self.n2
            long = self.n1
        else:
            long = self.n2
            short = self.n1
        short = ((len(long)-len(short))*'0')+short
        for i in range(len(short)-1, -1,-1):
            if short[i] == long[i]:
                if short[i]=='1':
                    if not carry: # if carry == false
                        n3 = '0' + n3
                    else:
                        n3 = '1' + n3
                    carry = True
                else:
                    if not carry:
                        n3 = '0' + n3
                    else:
                        n3 = '1' + n3
                    carry = False
            else:
                if not carry:
                    n3 = "1" + n3
                    carry = False
                else:
                    n3 = "0" + n3
                    carry = True
        if carry == True:
            n3 = '1' + n3
        return "0b" + n3
    #def __mul__(self, other):
        #multiply self by other through elementary techn.
    def __lt__(self, other):
        self.n1 = self.BinaryNumber[2:]
        self.n2 = other[2:]
        larger = ""
        if len(self.n1) > len(self.n2):
            short = self.n2
            long = self.n1
        else:
            long = self.n2
            short = self.n1
        short = ((len(long) - len(short)) * '0') + short
        for i in range(len(short)):
            if short[i] != long[i]:
                if short[i] == '1':
                    larger = "0b" + short
                else:
                    larger = "0b" + long
        return larger
        #checks if self is less than Other
    def is_power_of_2(self):
        count = 0
        num = self.BinaryNumber[2:]
        for i in num:
            if i == '1':
                count += 1
        if count == 1:
            return True
        else:
            return False
        #checks if self is power of two
    def largest_power_of_2(self):
        num = self.BinaryNumber[2:]
        power = len(num) - 1
        return 2**(power)
        #returns largest power of 2 contained in self
    def __repr__(self):
        return self.BinaryNumber


# number = BinaryPositiveInteger(16)
# number2 = BinaryPositiveInteger(255)
# print(number)
# #print(number2[1:])
# print(1,number.is_power_of_2())
# print(2,number.largest_power_of_2())
# #print(3,number < number2)
# #print(4,number + number2)

# a = BinaryPositiveInteger(3)
# b = BinaryPositiveInteger(1)
# print(a + b)
# print(a)
# print(b)


def adder(self, other):
    n1 = self.BinaryNumber[2:]
    n2 = other.BinaryNumber[2:]

    n3 = ""
    carry = False
    if len(n1) > len(n2):
        short = n2
        long = n1
    else:
        long = n2
        short = n1
    short = ((len(long) - len(short)) * '0') + short
    print(long, "\n", short, sep='')
    for i in range(len(short) - 1, -1, -1):
        if short[i] == long[i]:
            if short[i] == '1':
                if not carry: # == False
                    n3 = '0' + n3
                else:
                    n3 = '1' + n3
                carry = True
            else:
                if not carry:
                    n3 = '0' + n3
                else:
                    n3 = '1' + n3
                carry = False
        else:
            if not carry: # == false
                n3 = "1" + n3
                carry = False
            else:
                n3 = "0" + n3
                carry = True
    if carry == True:
        n3 = '1' + n3
    return n3

a = BinaryPositiveInteger(255)
b = BinaryPositiveInteger(1)
print(a+b)
print(adder(a,b))