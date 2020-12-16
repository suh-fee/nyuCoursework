#Question1

#a

input_lang = input("Enter a language:")

if input_lang == "en":
    print("Hello, world!")
elif input_lang == "es":
    print("¡Hola mundo!")
else:
    print("That language isn't recognized")

#b

input_num1 = int(input("Please enter a number:"))
input_num1 %= 2

if input_num1 < .5:
    print("Your number is even.")
else:
    print("Your number is odd")

#Question2

input_name = input("Please enter your name:")
input_grad_yr = int(input("Please enter your graduation year:"))
input_current_yr = int(input("Please enter the current year:"))

yrs_in_school = input_grad_yr - input_current_yr

if yrs_in_school < 0:
    print(input_name, "is a graduate.")
elif yrs_in_school == 0:
    print(input_name, "is about to graduate!")
elif yrs_in_school == 1:
    print(input_name, "is a senior")
elif yrs_in_school == 2:
    print(input_name, "is a junior")
elif yrs_in_school == 3:
    print(input_name, "is a sophomore")
elif yrs_in_school == 4:
    print(input_name, "is a freshman")
else:
    print(input_name, "isn't in college yet.")

#Question3

inp_first_leg = float(input("Enter the length of the first leg: "))
inp_second_leg = float(input("Enter the length of the second leg: "))
inp_hyp = float(input("Enter the length of the hypotenuse: "))

math_hyp = inp_first_leg ** 2 + inp_second_leg ** 2
math_hyp **= (1/2)

if abs(math_hyp - inp_hyp) <= .01:
    print(inp_first_leg, ",", inp_second_leg, ", and", inp_hyp, "form a right triangle.")
else:
    print(inp_first_leg, ",", inp_second_leg, ", and", inp_hyp, "don't form a right triangle. :(")

#Question4
print("This will solve for x when (ax + b = 0)")
a_val = float(input("Enter a value for a: "))
b_val = float(input("Enter a value for b: "))

if a_val == 0:
    if b_val != 0:
        print("The equation has no solution")
    else:
        print("The equation has infinite solutions")
else:
    x_val = (-b_val) / a_val
    print("The equation has one solution which is x = ", x_val)

#Question5

month = int(input("Please enter an integer between and including 1 and 12: "))

if month == 1:
    print("The month is January, which has 31 days.")
elif month == 2:
    print("The month is February, which has 28 days.")
elif month == 3:
    print("The month is March, which has 31 days.")
elif month == 4:
    print("The month is April, which has 30 days.")
elif month == 5:
    print("The month is May, which has 31 days.")
elif month == 6:
    print("The month is June, which has 30 days.")
elif month == 7:
    print("The month is July, which has 31 days.")
elif month == 8:
    print("The month is August, which has 31 days.")
elif month == 9:
    print("The month is September, which has 30 days.")
elif month == 10:
    print("The month is October, which has 31 days.")
elif month == 11:
    print("The month is November, which has 30 days.")
elif month == 12:
    print("The month is December, which has 31 days.")
else:
    print("That isn't a recognized value for a month")

#Question6

inp_sides = int(input("Enter a number of sides: "))

if inp_sides == 3:
    print("The shape is a triangle")
elif inp_sides == 5:
    print("The shape is a pentagon")
elif inp_sides == 4:
    side_length_equal = input("Are the side lengths equal? (Y/N): ")
    if side_length_equal == "N":
        angle_90 = input("Are the angles all right angles? (Y/N): ")
        if angle_90 == "N":
            print("The shape is a quadrilateral")
        elif angle_90 == "Y":
            print("The shape is a rectangle")
        else:
            print("Please enter a valid input.")
    elif side_length_equal == "Y":
        angle_90 = input("Are the angles all right angles? (Y/N): ")
        if angle_90 == "N":
            print("The shape is a quadrilateral")
        elif angle_90 == "Y":
            print("The shape is a square")
        else:
            print("Please enter a valid input:")
    else:
        print("Please enter a valid input.")
elif inp_sides > 4:
    print("Your shape has too many sides for this simple code :/")
else:
    print("That shape is impossible.")

#Question7

inp_time = (int(input("Please enter a time in 24hr format (####): "))) / 100
inp_hrs = round(inp_time // 1)
inp_min = round((inp_time % 1) * 100)

if inp_hrs > 24:
    print("Enter a valid input.")
elif inp_min > 59:
    print("Enter a valid input.")
elif inp_hrs > 12:
    print(inp_hrs, ":", inp_min, "in 12hr format is: ", (inp_hrs - 12), ":", inp_min, "pm")
elif inp_hrs <= 12 and inp_hrs >= 0:
    print(inp_hrs, ":", inp_min, "in 12hr format is: ", (inp_hrs), ":", inp_min, "am")
else:
    print("You done goofed.")

