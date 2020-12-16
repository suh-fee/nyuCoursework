# recursive algorithms

# 1. define the recursion hypoyhesis - Assume that "when calling the function on a smaller input, it does it's job"
# 2. Based on this assumption, find how to combine calls to smaller instances, in order to solve the problem for the given input

# assume that when calling countdown on a smaller range it would print the numbers of that range in decreasing order

# start <= end

def countdown (start, end):
    if (start == end):
        print(start)
    else:
        countdown(start+1, end)
        print(start)

# assume when calling countupdown on a smaller range it would print the numbers in increasing then decreasing order
def countupdown(start, end):
    if (start == end):
        print(start)
    else:
        print(end)
        countupdown(start, end-1)
        print(end)


# countdown(1,10)
# countupdown(1, 10)

#assume that when calling factorial with a k < n it would return a factorial

def factorial(n):
    if (n == 1):
        return 1
    else:
        return(factorial(n - 1)) * n

def cound_appear(lst, val):
    if len(lst) == 0:
        return 0
    else:
        count = cound_appear(lst[1:], val)
    if lst[0] == val:
        return count + 1
    else:
        return count

print(cound_appear([1,1,1,2,3], 1))


def count_appear(lst, low, high, val):
    if (low == high):
        if (lst[0] == val):
            return 1
        else:
            return 0
    else:
        count = count_appear(lst, low + 1, high, val)
        if lst[low] == val:
            return count + 1
        else:
            return count


print(count_appear([0,1,2,3,4,5,6], 1, 4, 2))