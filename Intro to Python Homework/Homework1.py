#Safi Hasani, CS 1114 ILC3 ILB2
#Question3
string1 = input("Please enter your name: ")
print("Hi", string1, "Welcome to CS-UY 1114!")

#Question4 - Population

years = int(input("Enter a number of years: "))
years2 = years * 31557600

births = int(years2 // 7)
deaths = int(years2 // -13)
immigrants = int(years2 // 35)

total_pop = int(307357870 + births + deaths + immigrants)

print("The US population after", years, "year(s) is:", total_pop, "people")

#Question 5
print("Please enter the number of coins:")
quarters = int(input("# of quarters:"))
dimes = int(input("# of dimes:"))
nickels = int(input("# of nickels:"))
pennies = int(input("# of pennies:"))

total_cents = int(quarters * 25) + (dimes * 10) + (nickels * 5) + pennies

dollars = total_cents // 100
cents = int(total_cents % 100)

print("You have", dollars, "dollar(s) and", cents, "cent(s).")

#Question 6
print("Please enter your amount in the format of dollars and cents in two sperate lines")

dollars_6 = int(input())
cents_6 = int(input())

total_cents_6 = cents_6 + (dollars_6 * 100)

quarters_6 = total_cents_6 // 25
remainder1 = total_cents_6 % 25

dimes_6 = remainder1 // 10
remainder2 = remainder1 % 10

nickels_6 = remainder2 // 5
remainder3 = remainder2 % 5

pennies_6 = remainder3

print(dollars_6, "dollars and", cents_6, "cents are:")
print(quarters_6, "quarters,", dimes_6, "dimes,", nickels_6, "nickels, and", pennies_6, "pennies.")
