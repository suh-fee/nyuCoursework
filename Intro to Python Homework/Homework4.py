# Question 1

# a

input1 = int(input("Please input a number: "))
multiple = 1

while input1 > 0:
    even_num = 2 * multiple
    print(even_num)
    input1 -= 1
    multiple += 1

# b
input1 = int(input("Please input a number: "))
multiple = 1
for x in range(input1):
    even_num = 2 * multiple
    print(even_num)
    multiple += 1

# question 2

length = int(input("Please input a length for the hourglass: "))
star = "*"
space = " "
space_num = 0
for x in range(length, 0, -1):
    print((space * space_num), (star * (2 * x - 1)))
    space_num += 1
space_num = length
for x in range(length + 1):
    print((space * space_num), (star * (2 * x - 1)))
    space_num -= 1

# question 3
print("| >>> ==================== RESTART ====================")
print("| >>>")
i = 1
for x in range(5):
    print("| ", 1, "    ", 2 ** i, "    ", 3 ** i, "    ", 4 ** i, "    ", 5 ** i, "    ", 6 ** i, "    ", 7 ** i, "    ", 8 ** i, "    ", 9 ** i, "    ", 10 ** i, sep='')
    i += 1
print("| >>>")
# question 4

int1 = int(input("Please input a number: "))
space_num = int1
string = ""
for x in range(int1):
    string += str(x+1)
    print((space * space_num), string)
    space_num -= 1

# question 5
int1 = int(input("Please input a number: "))

for x in range(int1 - 2):
    if ((x) % 2) == 0:
        print(x+2)

# question 6a

length = int(input("Please enter the length of the sequence: "))
print("Please enter your sequence:")
root = 0
sum = 0

while length != 0:
    num_add = int(input(""))
    sum += num_add
    length -= 1
    root += 1

geo = sum ** (1 / root)

print("The geometric mean is: ", geo)

# question 6b
print(" Please enter a non-empty sequence of + integers, each one in a separate line. End the sequence by typing done:")
root = -1
sum = 0
exit = 0
state = 0
while exit != 1:
    num = int(state)
    sum += num
    root += 1
    state = input()
    if state == "done":
        exit = 1

geo = sum ** (1 / root)
print("The geometric mean is: ", geo)

# question 7
import random
answer = random.randint(1, 100)
print("I thought of a number between 1 and 100! Try to guess it.")
min = 1
max = 100
for guess in range(5, 0, -1):
    print("Range: [", min, ", ", max, "], Number of guesses left: ", guess)
    user_guess = int(input("Your guess: "))
    if user_guess == answer:
        print("Correct! You guessed it in", (6 - guess), "guess(es)!")
        while True:
            num = input()
    if user_guess < answer:
        min = user_guess + 1
        print("Wrong! My number is larger.")
    if user_guess > answer:
        max = user_guess - 1
        print("Wrong! My number is smaller.")

print("No more chances! My answer was: ", answer)