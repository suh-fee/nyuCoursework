import math
import turtle

#Question1

radius_1 = int(input("Please input a radius:"))
circumference_1 = (2 * radius_1) * math.pi
area_1 = (radius_1 ** 2) * math.pi

print("Circumference of the circle is:", circumference_1, "and the  area of the circle is", area_1)


#Question 2
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.bye()

#Question 3
days_1 = int(input("Enter a number of days: "))
weeks_1 = days_1 // 7
days_final = days_1 - (weeks_1 * 7)

print(days_1, "day(s) is equal to", weeks_1, "week(s) and", days_final, "day(s).")

#Question 4

initial_value = int(input("Please enter in a value more than zero but less than 100: "))

fifties = initial_value // 50
remainder1 = initial_value % 50

tens = (remainder1) // 10
remainder2 = remainder1 % 10

fives = remainder2 // 5
remainder3 = remainder2 % 5

ones = remainder3

roman_final = ("L" * fifties) + ("X" * tens) + ("V" * fives) + (ones * "I")

print(roman_final)

#Question 5a

initial_dob = int(input("Please enter a date of birth: "))

birth_years = initial_dob // 10000
remainder4 = initial_dob % 10000
birth_months = remainder4 // 100
birth_days = remainder4 % 100

today_date = int(input("Please enter today's date: "))

today_years = today_date // 10000
remainder5 = today_date % 10000
today_months = remainder5 // 100
today_days = remainder5 % 100

print("Date of birth is:", birth_months, "/", birth_days, "/", birth_years)
print("Today's date is:", today_months, "/", today_days, "/", today_years)

#Question 5b

today_days = (today_years * 365) + (today_months * 30) + today_days
birth_days = (birth_years * 365) + (birth_months * 30) + birth_days
age_days = today_days - birth_days

age_years = age_days // 365
remainder6 = age_days % 365
age_months = remainder6 // 30
remainder7 = remainder6 % 30
age_days = remainder7


print("You have been alive for", age_years, "years,", age_months, "months, and", age_days, "days.")