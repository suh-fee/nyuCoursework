#Question1

#a
#Inputs
user_weight = float(input("Please enter a weight in kilograms:"))
user_height = float(input("Please enter a height in meters:"))

bmi = user_weight / (user_height**2)
#Results
print("BMI is:", bmi)

#b
#Input
user_weight = float(input("Please enter a weight in pounds:"))
user_height = float(input("Please enter a height in inches:"))

user_weight = user_weight * 0.453592
user_height = user_height * 0.0254
#Result
bmi = user_weight / (user_height**2)

print("BMI is:", bmi)

#Question2

import turtle

#Square1
turtle.left(20)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
#Square2
turtle.left(20)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
#Square3
turtle.left(20)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

#Question3

import math

#Inputs

a_side = float(input("Please enter the first side length: "))
b_side = float(input("Please enter the second side length: "))
c_angle = int(input("Please enter an angle length in degrees: "))

#Degrees to Radian Conversion

c2_angle = (c_angle * math.pi) / 180


#Evaluating c Side
cos_ang = math.cos(c2_angle)
c_side = (a_side ** 2) + (b_side ** 2) - (2 * a_side * b_side * cos_ang)
c_side **= (1/2)

#Evaluating b Angle
b_angle = math.acos(((b_side ** 2) - (c_side **2) - (a_side ** 2)) / (-2 * a_side * c_side))
b_angle = (b_angle * 180) / math.pi

#Evaluating a Angle
a_angle = math.acos(((a_side ** 2) - (b_side **2) - (c_side ** 2)) / (-2 * b_side * c_side))
a_angle = (a_angle * 180) / math.pi


#Drawing the triangle
turtle.reset()
turtle.forward(a_side)
turtle.left(180 - c_angle)
turtle.forward(b_side)
turtle.left(180 - a_angle )
turtle.forward(c_side)
turtle.left(input())


#Question 4

import time

print("Today's date is", time.strftime("%m/%d/%y"))

#Question 5
#Input
j_days = int(input("Enter how many days John has worked: "))
j_hours = int(input("Enter how many hours John has worked: "))
j_minutes = int(input("Enter how many minutes John has worked: "))
b_days = int(input("Enter how many days Bill has worked: "))
b_hours = int(input("Enter how many hours Bill has worked: "))
b_minutes = int(input("Enter how many minutes Bill has worked: "))
#Calculations
j_minutes = (j_days * 1440) + (j_hours * 60) + j_minutes
b_minutes = (b_days * 1440) + (b_hours * 60) + b_minutes

t_minutes = j_minutes + b_minutes

t_days = t_minutes // 1440
t_hours = (t_minutes % 1440) // 60
t_minutes = (t_minutes % 1440) % 60
#Results
print("The total time both of them worked is:", t_days, "days,", t_hours, "hours, and", t_minutes, "minutes.")

