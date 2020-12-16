# question 3

def print_triangle(n):
    if n != 0:
        print_triangle(n - 1)
        print('*' * n)


def print_opposite_triangles(n):
    if n != 0:
        print('*' * n)
        print_opposite_triangles(n - 1)
        print('*' * n)

def print_ruler(n):
    if n!=0:
        print_ruler(n-1)
        print('-' * n)
        print_ruler(n-1)

# question 4

def list_min(lst,low,high):
    if low != high:
        if lst[low] < lst[high]:
            return list_min(lst, low, high - 1)
        elif lst[low] > lst[high]:
            return list_min(lst, low + 1, high)
        else:
            return list_min(lst, low + 1, high)
    else:
        return lst[low]

# question 5

def count_lowercase(s,low,high):
    total = 0
    if low != high:
        if s[low].isupper():
            total += count_lowercase(s,low+1,high)
        else:
            total += 1
            total += count_lowercase(s,low+1,high)
    else:
        if not(s[low].isupper()):
            total+=1
    return total

def is_number_of_lowercase_even(s, low, high):
    def count_lowercase(s, low, high):
        total = 0
        if low != high:
            if s[low].isupper():
                total += count_lowercase(s, low + 1, high)
            else:
                total += 1
                total += count_lowercase(s, low + 1, high)
        else:
            if not (s[low].isupper()):
                total += 1
        return total
    total = count_lowercase(s, low, high)
    if total % 2 == 0:
        return True
    else:
        return False

# question 6

def appearances(s, low, high):
    if low != high:
        dct = appearances(s, low+1, high)
        if s[low] in dct:
            dct[s[low]] += 1
        else:
            dct[s[low]] = 1
    else:
        dct = {}
        dct[s[low]] = 1
    return dct

# question 7

def split_by_sign(lst, low, high):
    if low < high:
        if lst[low] < 0:
            neg = lst.pop(low)
            lst.insert(0, neg)
        split_by_sign(lst, low + 1, high)
    else:
        if lst[low] < 0:
            neg = lst.pop(low)
            lst.insert(0, neg)


# question 8

def flat_list(nested_lst, low, high):
    if low < high:
        if nested_lst == []:
            return nested_lst
        elif type(nested_lst[low]) == list:
            return flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1) + flat_list(nested_lst[low], 1, len(nested_lst[low]) - 1)
        else:
            return nested_lst[:1] + flat_list(nested_lst, low+1, high)


# question 9
def permutations(list1, low, high):
    if len(list1) == 0:
        return []
    if len(list1) == 1:
        return [list1]
    masterlist = []
    for i in range(len(list1)):
        y = list1[i]
        temp_list = list1[:i] + list1[i+1:]
        for x in permutations(temp_list, 0, 0):
            masterlist.append([y] + x)
    return masterlist

list1 = permutations([1,2,3], 0, 0)
for i in list1:
    print(i)


def permutations(lst, low, high):
    list1 = lst[low:high+1]
    if len(list1) == 0:
        return []
    if len(list1) == 1:
        return [list1]
    masterlist = []
    for x in range(high-low+1):
        z = list1[x]
        remLst = list1[:]
        remLst.remove(list1[x])
        for y in permutations(remLst, 0, len(remLst) -1):
            masterlist.append([z] + y)
    return masterlist

data = [1,2,3,4]
print(permutations(data, 0, 3))