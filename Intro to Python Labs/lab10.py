import random


# question 1

#
def write_name(filename, first_name, last_name):
    my_file = open(filename, "w")
    print(first_name + " " + last_name, file = my_file)
    my_file.close()
    return my_file


write_name("name_file.txt", "safi", "hasani")


# question 2

def write_random_numbers(filename, n):
    my_file = open(filename, "w")
    for i in range(n):
        print(random.randint(1, 100), file = my_file)
    my_file.close()
    return my_file

write_random_numbers("numbers.txt", 5)


# question 3

def sum_column(filename):
    my_file = open(filename, "r")
    total = 0
    for line in my_file:
        total += int(line)
    my_file.close()
    return total

print(sum_column("numbers.txt"))


# question 4


def html_table_generator(lst, file_to_write_to):
    my_file = open(file_to_write_to, "w")
    print("<html>", file = my_file)
    print("\t<table>", file = my_file)
    print("\t\t<tr>", file=my_file)
    for i in range(len(lst[0])):
        print("\t\t\t<th>" + lst[0][i] + "</th>", file=my_file)
    print("\t\t</tr>", file=my_file)
    for x in range(1, 4):
        print("\t\t<tr>", file=my_file)
        for i in range(len(lst[x])):
            print("\t\t\t<td>" + lst[x][i] + "</td>", file = my_file)
        print("\t\t</tr>", file = my_file)
    print("\t</table>", file = my_file)
    print("</html>", file = my_file)
    my_file.close()
    return my_file


list1 = [['Header 1', 'Header2', 'Header3', 'Header4'], ['R1C1', 'R1C2', 'R1C3', 'R1C4'],
         ['R2C1', 'R2C2', 'R2C3', 'R2C4'], ['R3C1', 'R3C2', 'R3C3', 'R3C4'], ['R4C1', 'R4C2', 'R4C3', 'R4C4']]

html_table_generator(list1, "html.txt")
