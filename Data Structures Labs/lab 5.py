

# question 1

def find_lst_max(lst):
    max = lst[0]
    if len(lst) > 1:
        new = lst[1:]
        compare = find_lst_max(new)
        if compare > max:
            max = compare
    return max


# print(find_lst_max([1,2,3,4,6,32,1,10000, -1]))

# question 2

def product_evens(lst):
    list1 = lst
    max = len(list1)
    sum = 1
    if list1[0] != '':
        if (list1[0] % 2 == 0) and (list1[0] <= max):
            sum *= list1[0]
        if len(list1) != 1:
            new = list1[1:]
            new.append('')
            multipler = product_evens(new)
        else:
            multipler = 1
        if multipler != None:
            sum *= multipler
    if sum == 1:
        sum = None
    del(list1)
    return sum

list1 = [1,2,1]
print(product_evens(list1))
print(list1)


# question 3

def is_palindrome(input_str, low, high):
    if low != high:
        if input_str[low] == input_str[high]:
                status = is_palindrome(input_str, low+1, high-1)
                return status
        else:
                return False

    else:
            return True

# question 4

def binary_search(srt_lst, val, low, high):
    left = low
    right = high
    found = False
    ind = None
    mid = (left + right) // 2
    if srt_lst[mid] > val:
        index = binary_search(srt_lst, val, low, mid-1)

    elif srt_lst[mid] < val:
        index = binary_search(srt_lst, val, low + 1, high)

    else:
        index = mid

    return index


# question 5
# input: string, return: int

import os

def disk_usage(path):
    total_usage = 0
    total_usage += os.path.getsize(path)
    if os.path.isdir(path):
        list = os.listdir(path)
        for i in list:
            total_usage += disk_usage(path + '/' + i)


    return total_usage


def disk(path):
    total = 0
    total += os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    return total

# print(os.path.getsize('/Users/safi_hasani/PycharmProjects/CS Semester 2/CS Semester 2 Labs'))

print(disk_usage('/Users/safi_hasani/PycharmProjects'))