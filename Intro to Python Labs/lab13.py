# # pen and paper 1
#
# 33
#
# 'walter'
#
# False
#
# {'bill': 1, 'rich': 2, 'fred': 10, 'walter': 20}

# part 2

# prob 1

import random


def checker(number):
    status = False

    if len(number) == 10:
        status = True
        for character in number:
            if character.isnumeric() == False:
                status = False
                break
    return status


class Phonebook(object):
    def __init__(self):
        self.phonebook = {}

    def add_entry(self, name, phone_number):
        if checker(phone_number):
            self.phonebook[name] = phone_number
        else:
            print("There was an error, try again.")

    def lookup(self, name):
        if name in self.phonebook:
            print(self.phonebook[name])
        else:
            print('There was an error, try again.')

    def print_all(self):
        for key in self.phonebook:
            print(key, self.phonebook[key])


def main1():
    f = open('Lab 13 - phonebook.txt', 'r')
    phonebook = Phonebook()
    for line in f:
        list = line.split(" ")
        if len(list) == 3:
            name = list[1].strip(',') + " " + list[0]
            number = list[2].strip('\n')
            phonebook.add_entry(name, number)
        elif len(list) == 4:
            name = list[2] + " " + list[0] + " " + list[1].strip(',')
            number = list[3].strip('\n')
            phonebook.add_entry(name, number)

    phonebook.print_all()
    f.close()

main1()

# prob 2

class BandAccount:
    def __init__(self, number, balance):
        self.account_number = number
        self.balance = balance

    def __repr__(self):
        string = "Current balance is: $" + str(self.balance)
        return string

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance. The current balance remained as $" + str(self.balance))

    def deposit(self, amount):
        self.balance += amount


# prob 3

class Patron:
    def __init__(self, name):
        self.name = name
        self.lib_acct_num = ''
        self.list_of_books = []

    def __repr__(self):
        string = "Name: " + self.name + "\nLibrary Account Number: " + \
                 str(self.lib_acct_num) + '\n\nBorrowed Books:'

        for book in self.list_of_books:
            string += "\n" + book

        return string + "\n"

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.patrons = {}
        self.books = []

    def __repr__(self):
        string = "Name: " + self.name + "\nLocations: " + self.address + "\n\nAvailable Books:"
        for book in self.books:
            string += "\n" + book
        string += "\n\nLibrary Patron Information:"
        for key in self.patrons:
            string += "\n" + repr(self.patrons[key])
        return string

    def add_patron(self, patron):
        name = patron.name
        random_id = self.random_id()
        patron.lib_acct_num = random_id
        self.patrons[name] = patron

    def add_book(self, book):
        self.books.append(book)

    def lend(self, name, book):
        status = False
        if name in self.patrons:
            for i in range(len(self.books)):
                if self.books[i] == book:
                    self.patrons[name].list_of_books.append(self.books.pop(i))
                    status = True
                    break
            if status == False:
                print(book, "is not available.\n")
        else:
            print(name, "is not a patron of the", self.name)

    def random_id(self):
        random_id = ''
        for i in range(5):
            random_id += str(random.randint(0, 9))
        return random_id

def main():
    library = Library("BK Lib", "6 Metro")
    library.add_book("Yer")
    library.add_book("Yee")
    library.add_book("Yeet")
    bob = Patron('Bob')
    library.add_patron(bob)
    library.lend('Bob', "Yer")
    # print(bob.lib_acct_num)
    janet = Patron('Janet')
    library.add_patron(janet)
    library.lend('Janet', 'Yeet')
    library.lend('Janet', 'Yerrr')
    print(library)

main()