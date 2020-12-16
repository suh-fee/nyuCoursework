def reverse_vowels(input_string):
    list = [''] * len(input_string)
    vowels = ['a','e','i','o','u']
    indexes = ['']
    num = 0
    for i in range(len(list)):
        list[i] = input_string[i]
    for char in range(len(list)):
        if list[char] in vowels:
            num += 1
    indexes *= num
    num = 0
    for char in range(len(list)):
        if list[char] in vowels:
            indexes[num] = char
            num+=1

    for i in range(len(indexes)//2):
        switch1 = list[indexes[i]]
        index_end = indexes[len(indexes)-1-i]
        switch2 = list[index_end]
        list[indexes[i]] = switch2
        list[index_end] = switch1

    return ''.join(list)


def binary_search(srt_lst, val):
    left = 0
    right = len(srt_lst) - 1
    found = False
    ind = None
    while ((found == False) and (left <= right)):
        mid = (left + right) // 2
        if (srt_lst[mid] == val):
            ind = mid
            found = True
        elif (srt_lst[mid] > val):
            right = mid - 1
        else:
            left = mid + 1
    return ind

def sorted_comp(list1, list2):
    a = 0
    b = 0
    while a != len(list1):
        pass
    pass

    # counter = 0
    # list3 = ['']
    # for i in range(len(list1)):
    #     ind = binary_search(list2, list1[i])
    #     if ind != None:
    #         counter +=1
    # list3 *= counter
    # counter = 0
    # for i in range(len(list1)):
    #     ind = binary_search(list2, list1[i])
    #     if ind != None:
    #         list3[ind] = list2[ind]
    # print(list3)

#
# sorted_comp([1,2,3], [2,3,4])

# 3a

def square_root(num):
    start = 1
    while round((start*start),2) != num:
        start += .001
    return round(start, 2)


# b

def square_root2(num):
    left = 0
    right = num/2
    found = False
    val = round(num, 2)
    while ((found == False) and (left <= right)):
        mid = (left + right) / 2
        squared = round(mid * mid, 2)
        if squared == val:
            ind = mid
            found = True
        elif (squared > val):
            right = mid - .01
        else:
            left = mid + .01
        print(mid)
    return round(mid, 2)


print(square_root2(4))