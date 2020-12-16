# # question 1
#
#
# def alphabet(ch, n):
#     newstring = ""
#     for i in range(n):
#         letter = chr((ord(ch) + i - 97) % 26 + 97)
#         newstring += letter
#     return newstring
#
#
# # question 2
#
#
# def comparison(a, b):
#     compare = True
#     for char in a:
#         if char in b:
#             index = b.find(char)
#             b = b[:index] + b[index + 1:]
#         else:
#             compare = False
#     return compare
#
#
# # question 3
#
#
# def encodeBinary(x):
#     new_x = x + "  "
#     type = ""
#     num1 = 0
#     num2 = 0
#     for i in range(len(x)):
#         if new_x[i] == "1":
#             type = "1"
#             num1 += 1
#             if new_x[i+1] == "0":
#                 print(num1, "1's")
#                 num1 = 0
#         if new_x[i] == "0":
#             type = "0"
#             num2 += 1
#             if new_x[i+1] != "0":
#                 print(num2, "0's")
#                 num2 = 0


# question 4


def binaryFlip(binary_ini):
    step = 0
    digit = 0
    for i in range(len(binary_ini)):
        if binary_ini[i] == "1":
            binary_ini = binary_ini[:i] + "0" + binary_ini[i+1:]
        elif binary_ini[i] == "0":
            binary_ini = binary_ini[:i] + "1" + binary_ini[i+1:]
    for i in range(len(binary_ini), 0, -1):
        if binary_ini[i-1] == "1":
            digit += 2**step
            step += 1
        else:
            step += 1
    return binary_ini, digit


print(binaryFlip("010"))
