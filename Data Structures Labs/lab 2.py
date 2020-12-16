import random

def roll_the_dice_str(n):
    s = ''
    for i in range(1,n+1):
        curr_val = random.randint(1,6)
        s += str(curr_val) + ' '
    return s[:-1]

def roll_the_dice_str2(n):
    s = ['' for i in range(n)]
    for i in range(n):
        curr_val = random.randint(1,6)
        s[i] = curr_val
    return ' '.join(s)


# print(roll_the_dice_str(5))
# max()

# def move_zeroes(nums):
#     length = len(nums) - 1
#     counter = 0
#     for item in nums:
#         if item == 0:
#             nums.pop(counter)
#             nums.insert(length, 0)
#         counter += 1
#     return nums

def move_zeroes(nums):
    length = len(nums) - 1
    counter = 0
    for i in range(length):
        if nums[i] == 0:
            nums[i] = nums[length-counter]
            nums[length - counter] = 0
            counter += 1
    return nums


list = [0, 1,2,3,0,5,0,2,1,2,0]
print(move_zeroes(list))