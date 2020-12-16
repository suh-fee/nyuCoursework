# question 1

# a


def print_shifted_triangle(n, m, symbol):
    space = " "
    num_space = m + n
    for x in range(n + 1):
        print((space * num_space), (symbol * (2 * x - 1)))
        num_space -= 1


# b


def print_pine_tree(n, symbol):
    triangle_lines = n
    for i in range(1, n+1):
        triangle_lines -= 1
        num_space = i
        print_shifted_triangle(i+1, triangle_lines, symbol)


# c

def main():
    n = int(input("Please enter a number: "))
    symbol = input("Please enter an input")
    print_pine_tree(n, symbol)


# question 2

# a


def print_month_calendar(num_days, starting_day):
    print('MON\tTUE\tWED\tTHU\tFRI\tSAT\tSUN')
    count = starting_day
    for x in range(1, num_days+1):
        if x == 1:
            for i in range(starting_day-1):
                print('\t', end='')
        print(x, end='\t')
        if count % 7 == 0:
            print()
        count += 1
    print()
    print()


print_month_calendar(31, 4)

# b


def leap_year_checker(year):
    if year % 100 == 0 and year % 400 == 0:
        status = True
    elif year % 100 == 0:
        status = False
    elif year % 4 == 0:
        status = True
    else:
        status = False
    return status

# c

def print_year_calender(year, starting_day):
    print("January", year)
    print_month_calendar(31, starting_day)
    status = leap_year_checker(year)
    if status == True:
        print("February", year)
        print_month_calendar(29, (7 + starting_day - 4) % 7)
        print("March", year)
        print_month_calendar(31, (7 + starting_day - 2) % 7)
        print("April", year)
        print_month_calendar(30, (7 + starting_day + 1) % 7)
        print("May", year)
        print_month_calendar(31, (7 + starting_day + 2) % 7)
        print("June", year)
        print_month_calendar(30, (7 + starting_day - 2) % 7)
        print("July", year)
        print_month_calendar(31, (7 + starting_day) % 7)
        print("August", year)
        print_month_calendar(31, (7 + starting_day - 4) % 7)
        print("September", year)
        print_month_calendar(30, (7 + starting_day - 1) % 7)
        print("October", year)
        print_month_calendar(31, (7 + starting_day + 1) % 7)
        print("November", year)
        print_month_calendar(30, (7 + starting_day - 3) % 7)
        print("December", year)
        print_month_calendar(31, (7 + starting_day - 1) % 7)
    else:
        print("February", year)
        print_month_calendar(28, (7 + starting_day - 5) % 7)
        print("March", year)
        print_month_calendar(31, (7 + starting_day - 3) % 7)
        print("April", year)
        print_month_calendar(30, (7 + starting_day) % 7)
        print("May", year)
        print_month_calendar(31, (7 + starting_day + 1) % 7)
        print("June", year)
        print_month_calendar(30, (7 + starting_day - 3) % 7)
        print("July", year)
        print_month_calendar(31, (7 + starting_day - 1) % 7)
        print("August", year)
        print_month_calendar(31, (7 + starting_day - 5) % 7)
        print("September", year)
        print_month_calendar(30, (7 + starting_day - 2) % 7)
        print("October", year)
        print_month_calendar(31, (7 + starting_day) % 7)
        print("November", year)
        print_month_calendar(30, (7 + starting_day - 4) % 7)
        print("December", year)
        print_month_calendar(31, (7 + starting_day - 2) % 7)


# d

def main():
    starting = int(input("Please enter a starting value: "))
    year = int(input("Please enter a year: "))
    print_year_calender(starting, year)


main()


# question 3

# a

string = "the quick brown fox jumps over the lazy dog"
def word_return(phrase):
    i = 0
    while phrase[i] != " ":
        first_word = phrase[:i+1]
        i += 1
    return first_word



# b

def sentence_return(phrase):
    i = 0
    phrase_copy = ""
    while phrase[i] != " ":
        phrase_copy = phrase[i+2:]
        i += 1
    return phrase_copy


# c


def reverse_sentence(phrase):
    sentence = ""
    count = phrase.count(" ")
    for i in range(count):
        first_word = word_return(phrase)
        phrase = sentence_return(phrase)
        sentence = first_word + " " + sentence
    sentence = phrase + " " + sentence
    return sentence




# d


def main():
    phrase = input("Please enter a sentence: ")
    print(reverse_sentence(phrase))


main()

