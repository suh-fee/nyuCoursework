# Question1

int1_0 = int(input("Please input a positive integer: "))
int2 = int(input("Please enter the number of digits: "))
int1_1 = int1_0
x = 0
int_fin = 0
while x < int2:
    x += 1
    remainder1 = int1_1 % 10
    int1_1 = int1_1 // 10
    int_fin = int_fin + remainder1

print("Sum of the last", int2, "digit(s) in", int1_0, "is: ", int_fin)

# Question2

int1 = int(input("Please enter a positive integer: "))
sum = 0

for x in range(int1):
    num_to_add = (x + 1) * ((0 - 1) ** (x + 2))
    sum = sum + num_to_add

print("Sum is: ", sum)

# Question 3

int1 = int(input("Please enter a positive integer as the dividend: "))
int2 = int(input("Please enter a positive integer as the divisor: "))
int3 = 0
quotient = 0

while int3 < int1:
    int3 = int3 + int2
    quotient += 1

if (int3 > int1):
    print("Quotient of", int1, "divided by", int2, "is: ", (quotient - 1))
elif int3 == int1:
    print("Quotient of", int1, "divided by", int2, "is: ", quotient)

# Question 4

int1 = int(input("Please enter a positive integer as the dividend: "))
int2 = int(input("Please enter a positive integer as the divisor: "))
int3 = 0

while int3 < int1:
    int3 = int3 + int2

if (int3 > int1):
    print("Remainder of", int1, "divided by", int2, "is: ", abs(((int3 - int2) - int1)))
elif int3 == int1:
    print("Remainder of", int1, "divided by", int2, "is 0")

# Question 5

# a
input1 = int(input("Please a number: "))

for x in range(input1):
    y = (x + 1) ** 3
    print(y)

# b
y = 1
z = 0
while z < input1:
    print(y ** 3)
    z = (y + 1) ** 3
    y += 1

# c
y = 0
z = 0
for x in range(input1):
    y = (x + 1) **3
    z += y

print(z)

# Question 6

int1 = int(input("Please input a positive number: "))
for x in range(int1):
    y = int1 - x - 1
    print("x" * x, "o", y * "x", sep='')
