def main():
    boyfile = open('BoyNames.txt', 'r')
    boys = []
    girls = []

    for line in boyfile:
        status = False
        line = line.strip('\n')

        for name in boys:
            if name[0] == line:
                status = True
                name[1] += 1

        if status == False:
            boys.append([line, 1])

    boyfile.close()
    girlfile = open("GirlNames.txt", 'r')

    for line in girlfile:
        status = False
        line.strip('\n')

        for name in girls:
            if name[0] == line:
                status = True
                name[1] += 1

        if status == False:
            girls.append([line, 1])

    girlfile.close()

    inp = raw_input("Enter your input: ")
    if inp == 'g' or inp == 'G':
        max = ['null', 0]
        for name in girls:
            if name[1] > max[1]:
                max = name
    elif inp == 'B' or inp == 'B':
        max = ['null', 0]
        for name in boys:
            if name[1] > max[1]:
                max = name

    print(max[0])


main()
