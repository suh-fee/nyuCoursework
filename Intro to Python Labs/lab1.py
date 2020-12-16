
#Part 1: name
print("Name: Safi Hasani")

#Part 2: math
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
print("Their sum is:", (int1 + int2), ". Their difference is:", (int1 - int2), ". Their product is:", (int1 * int2))

#Part 3: Temperature
temp1 = int(input("Enter a temperature in Fahrenheit: "))
temp2 = ((temp1 - 32) * (5/9))

print("In Celsius your temperature is: ", temp2, ". In Fahrenheit your temperature is: ", temp1)

#Part 4: Weight
weight1 = int(input("Enter a weight in pounds:"))
weight2 = weight1 * .45
weight3 = weight1 * 16

print(weight1, "is equivalent to", weight3, "in ounces and", weight2, "in kilograms.")

#Part 5: Binary/Decimal

#Part 6: Name p2

#Part 7: Yard/Ft


length1 = int(input("Enter the first legnth's feet: "))
length1_2 = int(input("Enter the first length's yards: "))
length2 = int(input("Enter the second legnth's feet: "))
length2_2 = int(input("Enter the second length's yards: "))

length_final = (length1 + (length1_2 * 3) + length2 + (length2_2 * 3))

length_final = (length_final / 3)
length_final2 = int(length_final)

length_final3 = (length_final - length_final2) * 3
length_final3 = round(length_final3)

print("The sum is: ", length_final2, "in yard and ", length_final3, "in feet.")