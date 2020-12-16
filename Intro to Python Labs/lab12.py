class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        self.hobbies = []

    def addHobby(self,newhobby):
        self.hobbies.append(newhobby)

    def deletehobby(self,oldhobby):
        counter = 0
        for i in self.hobbies:
            if i == oldhobby:
                self.hobbies.pop(counter)
            else:
                counter += 1


    def birthday(self):
        print("Happy birthday, " + self.name + "!")
        self.age += 1

    def __repr__(self):
        repre = "Name: " + self.name + "\nAge: " + str(self.age) + "\n" + "Hobbies:"
        for i in self.hobbies:
            repre += "\n" + i
        return repre


def createperson():
    name = input("Please enter a name: ")
    age = int(input("Please enter the age: "))
    person = Person(name, age)
    return person

def main():
    people = []
    while True:
        print("\nSelect one of the following options\n=================\n1. Create a new Person\n2. Add to an existing "
              "person's hobbies\n3. Delete an existing person's hobbies\n4. Someone has a birthday \n"
              "5. See a list of people\n6. Exit\n")
        user_input = input()
        if user_input == "1":
            person = createperson()
            people.append(person)
        if user_input == "2":
            person_name = input("Who is receiving this hobby? ")
            hobby = input("What is the person's new hobby? ")
            for i in people:
                if i.name == person_name:
                    i.addHobby(hobby)

        if user_input == "3":
            person_name = input("Who is losing a hobby? ")
            hobby = input("What hobby are you deleting? ")
            for i in people:
                if i.name == person_name:
                    i.deletehobby(hobby)

        if user_input == "4":
            person_name = input("Who is having a birthday? ")
            for i in people:
                if i.name == person_name:
                    i.birthday()

        if user_input == "5":
            for i in people:
                print(i)

        if user_input == "6":
            print("Goodbye!")
            break

main()


