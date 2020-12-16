running_total = 0

num = int(input("Please enter a number , -1 to stop:"))
while num != -1:
    running_total += num
    print("You entered: ", num)
    num = int(input("Please enter a number, -1 to stop: "))
print("The total is: ", running_total)