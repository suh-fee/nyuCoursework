# Question 3

def factors(num):
    for i in range(1, int((num**.5) + .99)):
        if num % i == 0:
            yield i
    for i in range(int((num**.5)), 0, -1):
        if num % i == 0:
            yield num // i



# Question 4

def factorial(n):
    dicti = {0: 1, 1: 1}
    for i in range(1, n+1):
        dicti[i] = (dicti[(i-1)]) * i
    return dicti

def e_approx(n):
    factorials = factorial(n)
    e = 1
    new = n + 1
    for i in range(1, new):
        e += (1/(factorials[i]))
    return e

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print('n =', n, 'Approximation:', approx_str)

main()

# question 5

def split_parity(lst):
    left = 0
    right = len(lst) - 1
    while (left < right):
        print(lst)
        if (lst[left] % 2 == 0):
            switch1 = lst[left]
            switch2 = lst[right]
            lst[left] = switch2
            lst[right] = switch1
            right -= 1
        else:
            left += 1
    return lst


# question 6

def two_sum(srt_lst, target):
    for i in range(len(srt_lst)):
        left = i
        right = len(srt_lst) - 1
        found = False
        ind = None
        while ((found == False) and (left <= right)):
            mid = (left + right) // 2
            if ((srt_lst[mid] + srt_lst[i]) == target):
                return i, mid
            elif ((srt_lst[mid] + srt_lst[i]) > target):
                right = mid - 1
            else:
                left = mid + 1


# question 7

def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    found = False
    while ((found == False) and (left - right != 1)):
        mid = (left + right) // 2
        if lst01[mid] == lst01[mid + 1]:
            if lst01[mid] == 0:
                left = mid
            elif lst01[mid] == 1:
                right = mid
        else:
            return mid + 1

