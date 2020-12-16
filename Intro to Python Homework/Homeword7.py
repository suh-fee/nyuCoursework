# question 1


def max_abs_val(lst):
    lst_max = lst[0]
    for i in range(len(lst)):
        lst_max = abs(lst_max)
        compare = abs(lst[i])
        if compare > lst_max:
            lst_max = compare
    return lst_max


# question 2



def find_all(lst, val):
    new_list = []
    for i in range(len(lst)):
        place = lst[i]
        if place == val:
            new_list.append(i)
    return new_list


# question 3

def add_list(lst1, lst2):
    new_lst = []
    if len(lst1) != len(lst2):
        print("Lists are different lengths")
    else:
        for i in range(len(lst1)):
            add1 = lst1[i]
            add2 = lst2[i]
            new_lst.append(add1 + add2)
    return new_lst

def main():
    lst1 = []
    lst2 = []
    exit = False
    print("Enter the values for the first list.")
    while exit != True:
        add = input()
        if add == "done" or add == "Done":
            exit = True
        else:
            lst1.append(int(add))
    print("Enter the values for the second list.")
    exit = False
    while exit != True:
        add = input()
        if add == "done" or add == "Done":
            exit = True
        else:
            lst2.append(int(add))
    end_r = add_list(lst1, lst2)
    print(end_r)



# question 4

def create_prefix_lists(lst):
    new_list = []
    for i in range(len(lst) + 1):
        empty_lst = lst[:i]
        new_list.append(empty_lst)
    return new_list

# question 5

#a

def comp(char, comp_char, new_list, n):
    if char == comp_char:
        n += 1
    else:
        add_list = [char, n]
        new_list.append(add_list)
        n = 1
    return new_list, n


def length_string_encoder(strng):
    n = 1
    new_list = []
    for i in range(1, len(strng)+1):
        char = strng[i-1]
        if i <= (len(strng)-1):
            comp_char = strng[i]
        else:
            comp_char = "THIS WILL BREAK"
        new_list, n = comp(char, comp_char, new_list, n)
    return new_list




#b



def length_string_decoder(lst):
    length = len(lst)
    new_string = ""
    for i in range(length):
        char = lst[i][0]
        num = lst[i][1]
        new_string += char*num
    return new_string




# question 6

# a
def reverse_to_new_list(lst):
    new_list = []
    length = len(lst)
    for i in range(length-1, -1, -1):
        new_list.append(lst[i])
    return new_list



# b
def reverse_in_place(lst):
    length = len(lst)
    if length % 2 == 0:
        length = int(length / 2)
        for i in range(length):
            place1 = lst[i]
            place2 = lst[len(lst)-1-i]
            lst[i] = place2
            lst[len(lst)-1-i] = place1

    else:
        length = int((len(lst)-1) / 2)
        for i in range(length):
            place1 = lst[i]
            place2 = lst[(len(lst)-1)-i]
            lst[i] = place2
            lst[len(lst) - 1 - i] = place1
    return lst
my_list = [1,2,3,4,5,6]
print(reverse_in_place(my_list))

