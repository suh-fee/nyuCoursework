# question 1

oddstring = input("Please enter an odd length string: ")
middle_char = 0
first_half = 0
second_half = 0


if len(oddstring) % 2  == 0:
    print("That is an invalid string.")
    print(len(oddstring))
    half = len(oddstring) // 2
    middle_char = oddstring[half]
    first_half = oddstring[:half]
    second_half = oddstring[half+1:]

print("Middle character: ", middle_char)
print("First half: ", first_half)
print("Second half: ", second_half)

# question 2

# a

inp_str = input("Please enter a character: ")

alpha_state = str.isalpha(inp_str)

number_state = str.isnumeric(inp_str)

if alpha_state == True:
    lower_state = str.islower(inp_str)
    upper_state = str.isupper(inp_str)
    if lower_state == True:
        print(inp_str, "is a lowercase letter")
    if upper_state == True:
        print(inp_str, "is an uppercase letter")

if number_state == True:
    print(inp_str, "is a digit")

number_state = not(number_state)
alpha_state = not(alpha_state)

if number_state and alpha_state == True:
    print(inp_str, "is a non-alphanumeric character")

# b

inp_str = input("Please enter a character: ")

ord_str = ord(inp_str)

if ord_str <= 122 and ord_str >= 97:
    print(inp_str, "is a lowercase letter")
elif ord_str >= 65 and ord_str <= 90:
    print(inp_str, "is an uppercase letter")
elif ord_str >= 0 and ord_str <= 90:
    print(inp_str, "is a digit.")
else:
    print(inp_str, "is an non-alphanumeric character")

# question 3

space = " "
equation = input("Please input a mathematical expression: ")

for i in range(len(equation)):
    if equation[i] == space:
        num1 = equation[:i]
        num2 = equation[i+3:]
        if equation[i+1] == "+":
            op = 0
        if equation[i+1] == "-":
            op = 1
        if equation[i+1] == "/":
            op = 2
        if equation[i+1] == "*":
            op = 3
        break


if op == 0:
    answer = int(num1) + int(num2)
    print(num1, "+", num2, "=", answer)
elif op == 1:
    answer = int(num1) - int(num2)
    print(num1, "-", num2, "=", answer)
elif op == 2:
    answer = int(num1) / int(num2)
    print(num1, "/", num2, "=", answer)
elif op == 3:
    answer = int(num1) * int(num2)
    print(num1, "*", num2, "=", answer)

# question 4

word = input("Please input a word: ")
comp_word = word.upper()
vowel = 0
for i in range(len(word)):
    if ord(comp_word[i]) == 65 or ord(comp_word[i]) == 69 or ord(comp_word[i]) == 73 or ord(comp_word[i]) == 79 or \
                                                                                        ord(comp_word[i]) == 85:
        vowel += 1

consonant = len(word) - vowel

print(word, "has", vowel, "vowels and", consonant, "consonants")

# question 5

upper_state = False
lower_state = False
digit_state = False
special_state = False
digit = 0
lower = 0
upper = 0
special = 0
password = input("Please enter a password: ")
if len(password) >= 8:
    for i in range(len(password)):
        if ord(password[i]) >= 48 and ord(password[i]) <= 57:
            digit += 1
        if ord(password[i]) >= 65 and ord(password[i]) <= 90:
            upper += 1
        if ord(password[i]) >= 97 and ord(password[i]) <= 122:
            lower += 1
        else:
            special += 1

if digit >= 2:
    digit_state = True
if lower >= 1:
    lower_state = True
if upper >= 2:
    upper_state = True
if special >= 1:
    special_state = True

if special_state and lower_state and upper_state and digit_state == True:
    print(password, "is a valid password")
else:
    print(password, "is not a valid password")

# question 6

lower_word = input("Please enter a string of lowercase letters: ")
for i in range(len(lower_word)-1):
    initial = lower_word[i]
    second = lower_word[i+1]
    if ord(initial) < ord(second):
        lexi_state = True
    else:
        lexi_state = False
        break

if lexi_state == True:
    print(lower_word, "is increasing.")
else:
    print(lower_word, "is not increasing.")

# question 7

# a

roman_inp = input("Please enter a number in the simplified Roman system: ")
value = 0

for i in range(len(roman_inp)):
    if roman_inp[i] == "M":
        value += 1000
    if roman_inp[i] == "D":
        value += 500
    if roman_inp[i] == "C":
        value += 100
    if roman_inp[i] == "L":
        value += 50
    if roman_inp[i] == "X":
        value += 10
    if roman_inp[i] == "V":
        value += 5
    if roman_inp[i] == "I":
        value += 1

print(roman_inp, "is", value)

# b

value = int(input("Enter a decimal number: "))

m_value = value // 1000
remainder = value % 1000
d_value = remainder // 500
remainder = remainder % 500
c_value = remainder // 100
remainder = remainder % 100
l_value = remainder // 50
remainder = remainder % 50
x_value = remainder // 10
remainder = remainder % 10
v_value = remainder // 5
remainder = remainder % 5
i_value = remainder // 1

roman = (("M" * m_value) + ("D" * d_value) + ("C" * c_value) + ("L" * l_value) + ("X" * x_value) + ("V" * v_value) + ("I" * i_value))

print(value, "is", roman)

# question 8

string_inp = input("Please enter a line of text: ")
new_string = string_inp
ch = input("Please enter the character you want to remove: ")
difference = 0

for i in range(len(string_inp)):
    if string_inp[i] == ch:
        new_string = new_string[:i-difference] + new_string[i+1-difference:]
        difference += 1


print(new_string)
