# # CS Lecture review
#
# list = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list)):
#     adder = list.pop((len(list)-1))
#     list.insert(i, adder)
#     print(list)

def greet_person(sPersonName):
    """
    says hello
    """
    if sPersonName == "Robert":
        raise Exception("we don't like you, Robert")
    print("Hi there {0}" + (sPersonName))


greet_person("Robert")