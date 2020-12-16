class BinaryPositiveInteger(object):
    def __init__(self, num):
        self.binary_num = ""
        while num != 0:
            if num % 2 == 0:
                self.binary_num = '0' + self.binary_num
            else:
                self.binary_num = '1' + self.binary_num
            num = num // 2

        self.binary_num = "0b" + self.binary_num

    def __add__(self, other):
        adder1 = str(self.binary_num[2:]) # initial set up
        adder2 = str(other.binary_num[2:])
        while len(adder1) != len(adder2):
            if len(adder1) > len(adder2):
                adder2 = '0' + adder2

            if len(adder2) > len(adder1):
                adder1 = '0' + adder1

        adder1 = list(adder1)
        adder2 = list(adder2)
        carry = False
        sum_bin = []

        for i in range(len(adder1) - 1, -1, -1):  # creates a new string that is the binary representation of the sum
            # that will be converted to an int
            if carry == False:
                if adder1[i] == adder2[i]:
                    if adder1[i] == '1':
                        sum_bin.append('0')
                        carry = True
                    else:
                        sum_bin.append('0')
                        carry = False
                else:
                    sum_bin.append('1')
                    carry = False
            else:
                if adder1[i] == adder2[i]:
                    if adder1[i] == '1':
                        sum_bin.append('1')
                        carry = True
                    else:
                        sum_bin.append('1')
                        carry = False
                else:
                    sum_bin.append('0')
                    carry = True

        if carry == True:
            sum_bin.append('1')

        sum_bin.reverse()
        sum_bin = ''.join(sum_bin)

        end_sum = 0
        exponent = 0 # converting from binary to int to create the new object
        for i in range(len(sum_bin) - 1, -1, -1):
            if sum_bin[i] == '1':
                end_sum += 2 ** exponent
            exponent += 1
        end_object = BinaryPositiveInteger(end_sum)
        return end_object

    def __lt__(self, other):
        num1 = list(self.binary_num[2:])
        num2 = list(other.binary_num[2:])
        if len(num1) < len(num2):
            return True
        elif len(num1) > len(num2):
            return False
        else:
            for i in range(len(num1)):
                if num1[i] == '1' and num2[i] == '0':
                    return False
                if num1[i] == '0' and num2[i] == '1':
                    return True

    def __repr__(self):
        return self.binary_num

    def is_power_of_2(self):
        check = list(self.binary_num[1:])
        counter = 0
        for i in check:
            if i == '1':
                counter += 1
        if counter == 1:
            return True
        else:
            return False

    def largest_power_of_2(self):
        check = list(self.binary_num[1:])
        length = len(check) - 2
        largest_power = 2 ** length
        return largest_power


 





a = BinaryPositiveInteger(255)
b = BinaryPositiveInteger(1)
print(a.largest_power_of_2())


