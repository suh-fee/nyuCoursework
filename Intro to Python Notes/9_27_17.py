# var1 = int(input("Enter a number:"))
#
# if var1 > 5:
#     print("var1 is True!")
#     print("Here's another statement")
#     print("Here's a third")
# elif var1 == 4:
#     print("var1 is 4!")
# elif var1 > 3:
#     print("We're in the middle!")
# #if "if" is False, than else block occurs
# else:
#     print("var1 is too small!")

# print("This happens after the if regardless.") #since it's on a different indentation than the if statement, it is a spereate block of code. it will always run.

# pressure_sensor = 75
# glass_break = False
# motion_sensor = True
#
# alarm_armed = False
#
# if alarm_armed:
#     if (motion_sensor or glass_break or (pressure_sensor > 100)):
#         print("WOOOOOOOOOO!")
#     else:
#         print("*silence*")
# else:
#     print("*silence*")


# Let the user enter a number of hours
# Let the user enter a hourly rate
# Calculate their pay
# If they have more than 40 hrs, they earn 1.5 times hourly rate for each hr over 40

# number_of_hours = int(input("Enter a number of hours:"))
# hourly_rate = float(input("Enter hourly rate of pay:"))
#
# if number_of_hours > 40:
#     overtime_hours = number_of_hours - 40
#     total_pay = ((number_of_hours - overtime_hours) * hourly_rate) + ((1.5 * hourly_rate) * overtime_hours)
# else:
#     total_pay = hourly_rate * number_of_hours
# print("Total pay is:", total_pay)