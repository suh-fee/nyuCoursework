# pen and paper 1
#
# x is 10 y is 25
#
# question 1

import random
string = ""


def descending(x):
    string = ""
    for i in range(x):
        y = str(random.randint(0, 9))
        string = string + y + " "
    print(string)
    return string
#


length = int(input("Please enter a number: "))

for i in range(length, 0, -1):
    descending(i)

for i in range(1, length+1):
    descending(i)

#question 2


def shout(input):
    y = input.upper()
    y = y + "!!!"
    return y
y = shout(input())

# question 3


def convertASCIItoText(x):
    string = ""
    for index in range(0, int(len(x)/2)):
        region = x[(2 * index):(2 * (index + 1))]
        character = chr(int(region))
        string = string + character
    print(string)

convertASCIItoText(input(""))

