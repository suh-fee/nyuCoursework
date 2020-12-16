int1 = int(input("Please enter a number: "))

int_remainder1 = int1 % 3
int_remainder2 = int1 % 5

if int_remainder1 == 0 and int_remainder2 == 0:
    print("FizzBuzz")
elif int_remainder1 == 0:
    print("Fizz")
elif int_remainder2 == 0:
    print("buzz")
else:
    print(nah)