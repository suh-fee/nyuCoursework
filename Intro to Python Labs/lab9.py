# pen and paper 1

# a: ['hi', 'mom', 'dad', 1, 57, 25]
# b: ['hi', 25]
# c: ['hi', 'mom', 'dad', [1, 57, 25]]
# d: ['hi', 'mom', 'dad', [1, 57, 25]]

# pen and paper 2

# a: 5
# b: 3
# c: [3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]

#programming

# q 1

def staircase(myint, n):
    num_list = []
    for i in range(n):
        num_list.append(myint+i)
    return num_list

# q 2

def count(lst, item):
    length = len(lst)
    counter = 0
    for i in range(length):
        if lst[i] == item:
            counter += 1
    return counter


# q 3

def two_powers():
    n = int(input("Please input an n: "))
    num_list = []
    for i in range(n):
        num_list.append(2**(i+1))
    return num_list

# q 4

def find_max_even_index(lst):
    length = len(lst)
    last_even_place = -1
    last_even = 0
    for i in range(length):
        if (lst[i] % 2) == 0:
            if lst[i] > last_even:
                last_even_place = i
                last_even = lst[last_even_place]
    return last_even_place


# q 5

def get_common_element(lst1, lst2):
    fin_list = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                fin_list.append(lst1[i])
                lst2.pop(j)
                break
    return fin_list


# q 6

def squared(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i] ** 2
    return sum

# q 7

def remove_below_average(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    average = sum / len(lst)
    difference = 0
    for i in range(len(lst)):
        if lst[i-difference] < average:
            lst.pop(i - difference)
            difference += 1
    return lst

# q 8

def circular_shift_list(lst, k):
    for i in range(k):
        lst.insert(0, lst.pop())
    return lst
