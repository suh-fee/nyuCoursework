# Question1

#Inputs
user_weight = float(input("Please enter a weight in kilograms:"))
user_height = float(input("Please enter a height in meters:"))

bmi = user_weight / (user_height**2)
print("Your BMI is:", bmi)

if bmi > 30:
    print("Your BMI places you in the obese category.")
elif bmi > 25:
    print("Your BMI places you in the overweight category.")
elif bmi > 18.5:
    print("Your BMI places you in the normal category.")
elif bmi < 18.5:
    print("Your BMI places you in the underweight category")

# Question 2

purchase1 = float(input("How much was your first item?:"))
purchase2 = float(input("How much was your second item?:"))
club_status = input("Are you a club member? Y/N:")
tax_rate = float(input("What is your tax rate? Enter as a number:"))

total_price = purchase1 + purchase2
print("Your base price is:", total_price)

if purchase1 > purchase2:
    total_price -= purchase2 / 2
elif purchase2 > purchase1:
    total_price -= purchase1 / 2

if club_status == "Y" or "y":
    total_price *= .9

print("Your discounted price is:", total_price)

total_price *= (1 + tax_rate / 100)
total_price = round(total_price, 2)


print("Your total price after discount and tax is:", total_price)

# Question 3

error = "Enter a valid input."
day_call = input("Enter the day the call started:")
time_call = int(input("Enter the time the call started at (hhmm):"))
duration_call = int(input("Enter the duration of the call (in minutes):"))

hour_call = time_call // 100

if day_call == "Mon" or day_call == "Tue" or day_call == "Wed" or day_call == "Thr" or day_call == "Fri":
    if hour_call < 8 or hour_call > 18:
        cost_call = duration_call * .25
    elif hour_call >= 8 and hour_call <= 18:
        cost_call = duration_call * .4
elif day_call == "Sat" or day_call == "Sun":
    cost_call = duration_call * .15
else:
    print(error)

print("This call will cost $", cost_call)

# Question 4

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
disc = (b ** 2) - (4 * a * c)
if disc > 0:
    solutions = 2
elif disc < 0:
    solutions = 0
elif disc == 0:
    solutions = 1

zero1 = ((0 - b) + (disc ** (1/2))) / (2 * a)
zero2 = ((0 - b) - (disc ** (1/2))) / (2 * a)

if a == 0 and b == 0 and c == 0:
    print("The equation has infinite solutions.")
elif (a == 0 and b == 0) or (b == 0 and c > 0):
    print("This equation has no solutions")
elif solutions == 2:
    print("This equation has two real solutions that are:", zero1, "and", zero2)
elif solutions == 1:
    print("This equation has one real solution of", zero1)
else:
    print("This equation has no real solutions")

#Question5

a_side = float(input("Enter the length of the first side:"))
b_side = float(input("Enter the length of the second side:"))
c_side = float(input("Enter the length of the third side:"))

if a_side - b_side < .00001 and a_side - c_side < .00001 and c_side - b_side < .00001:
    equilateral = True
else:
    if abs(a_side - b_side) < .00001 and abs(a_side - c_side) < .00001:
        hyp = a_side
        side1 = b_side
        side2 = c_side
        equilateral = False
    elif abs(b_side - a_side) < .00001 and abs(b_side - c_side) < .00001:
        hyp = b_side
        side1 = c_side
        side2 = a_side
        equilateral = False
    elif abs(c_side - a_side) < .00001 and abs(c_side - b_side) < .00001:
        hyp = c_side
        side1 = a_side
        side2 = b_side
        equilateral = False
    elif abs(a_side - b_side) < .00001 and abs(a_side - c_side) > .00001:
        hyp = c_side
        side1 = a_side
        side2 = b_side
        equilateral = False
    elif abs(c_side - b_side) < .00001 and abs(c_side - a_side) > .00001:
        hyp = a_side
        side1 = c_side
        side2 = b_side
        equilateral = False
    elif abs(a_side - c_side) < .00001 and abs(a_side - b_side) > .00001:
        hyp = b_side
        side1 = a_side
        side2 = c_side
        equilateral = False

isos_r = False

if equilateral == False:
    if side1 - side2 < .00001:
        if abs(hyp - (side1 * (2**(1/2)))) < .00001:
            isos_r = True
        else:
            isos_r = False

if equilateral == True:
    print(a_side, ",", b_side, ",", c_side, "forms an equilateral triangle.")
elif equilateral == False:
    if isos_r == True:
        print(a_side, ",", b_side, ",", c_side, "forms an isosceles right triangle.")
    elif isos_r == False:
        print(a_side, ",", b_side, ",", c_side, "forms an isosceles triangle.")






