def main():
    keys = []
    values = []
    dict = {}
    for i in range(3):
        keys.append(input("Please enter three keys: \n"))
    for i in range(3):
        values.append(int(input("Please enter three values: \n")))
    for i in range(3):
        dict[keys[i]] = values[i]

    print(dict)

main()