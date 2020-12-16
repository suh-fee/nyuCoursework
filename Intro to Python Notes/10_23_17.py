# my_str = "Hello World"
#
# #Hello:World
#
# new_string = my_str[:5] + ":" + my_str[6:] #mystr[:5] is exclusive, mystr[6:] is inclusive
#
# print(new_string)

# my_str = "Hello world1000"
#
# print(my_str.upper()) # makes it uppercase
# print(my_str[0].isalpha()) # checks if the specific character is a letter instead of a number
#     # true if all in the range are, false otherwise
# print(my_str.find("l", 5)) # find the PLACE of that specific character, only displays the first
#     # if it isn't there, gives a value of negative one, second part is the starting character
#
# index = 0
# while index != -1:
#     index = my_str.find("l", index + 1)
#     print(index)

# haystack = input("Please enter the string to be searched: ")
# needle = input("Please enter the character to search for: ")
# index = 0
# if len(needle) != 1:
#     print("That is not a valid needle")
# else:
#     while index != -1:
#         index = haystack.find(needle, index+1)
#         if index != -1:
#             print("The needle is at place: ", index)
#
# story = "To VERB or not to VERB, that is the NOUN"
# verb = input("Please enter a verb: ")
# noun = input("Please enter a noun: ")
#
# story = story.replace("VERB", verb)
# story = story.replace("NOUN", noun)
#
# print(story)

sentence = input("Please enter the sentence to be disconnected: ") # same as above but it looks for specfic set of characters
word = input("Please enter a word: ")

last_index = sentence.find(" ")
count = 0
if last_index != -1:
    print("Found a space at ", last_index)
w = sentence[:last_index]
if w == word:
    count += 1
while last_index != -1:
    last_index = sentence.find[" ", last_index+1]
    if last_index != 1:
        print("Found a space at ", last_index)

# rest of code in photo