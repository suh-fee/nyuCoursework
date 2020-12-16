class ToDoList(object):
    def __init__(self):
        self.to_do = []
        self.daily_to_do = []
        self.daily_to_do_day = self.daily_to_do
        self.accomplishments = []

    def create_to_do_list_item(self):
        task = input('Input the task: ')
        self.to_do.append(task)

    def create_daily_to_do(self):
        self.daily_to_do.append(input("Please enter the new daily task: "))
        self.daily_to_do_day = self.daily_to_do

    def delete_daily_to_do(self):
        deleter = input("What task would you like to delete? ")
        for i in range(len(self.daily_to_do)):
            if self.daily_to_do[i] == deleter:
                self.daily_to_do.pop(i)
                
    def check_to_do_list(self):
        for i in range(len(self.to_do)):
            pop_state = input('Did you do ' + self.to_do[i] + '? (y/n): ')
            if pop_state == 'y':
                self.accomplishments.append(self.to_do.pop(i))

        for i in range(len(self.daily_to_do_day)):
            pop_state = input('Did you do ' + self.daily_to_do_day[i] + '? (y/n): ')
            if pop_state == 'y':
                self.accomplishments.append(self.daily_to_do_day.pop(i))


        print("\nUpdated To Do List \n\nToday's accomplishments\n=========================")
        for i in self.accomplishments:
            print(i)
        print("\nLeft to do\n=========================")
        final_todo = self.to_do + self.daily_to_do_day
        for i in final_todo:
            print(i)



class Calender(object):
    def __init__(self):
        self.months = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['June', 30],
                ['July', 31], ['August', 31], ['September', 30], ['October', 31], ['November', 30], ['December', 31]]
        day_input = input('Please enter the date in month/day/year format: ')
        self.date_list = day_input.split('/')
        self.current_day = int(self.date_list[1])
        self.current_month = int(self.date_list[0])
        self.current_year = int(self.date_list[2])
        self.day_place = int(input('Please enter the day of the week today (1 for Monday, 7 for Sunday): ')) - 1
        self.week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.to_do_list = ToDoList()

    def __repr__(self):
        self.date = [str(self.current_month), str(self.current_day), str(self.current_year)]
        representation = "Today's date is: " + str(self.week_list[self.day_place]) + " " + "/".join(self.date) + \
            "\nToday's accomplishments\n=========================\n"

        for i in range(len(self.to_do_list.accomplishments)):
            representation += self.to_do_list.accomplishments[i] + '\n'

        representation += "Left to do\n========================="

        for i in range(len(self.to_do_list.to_do)):
            representation += self.to_do_list.to_do[i] + '\n'

        return representation

    def start_new_day(self):
        if self.current_day == (self.months[self.current_month - 1][1]):
            new_month_state = True
        else:
            new_month_state = False

        if new_month_state == True:
            if self.current_month == 12:
                self.current_year += 1
            self.current_day = 1
            self.current_month = (self.current_month + 1) // 11
        else:
            self.current_day = self.current_day + 1
        self.day_place = (self.day_place + 1) % 6
        self.to_do_list.accomplishments = []
        self.to_do_list.daily_to_do_day = self.to_do_list.daily_to_do



def main():
    calender = Calender()
    while True:
        print('\nMain Menu:')
        print('1. Create New Calender')
        print('2. Add To-Do List Item')
        print('3. Check Off To-Do List')
        print("4. Show Today's Calender")
        print('5. Start the next day')
        print('6. Create a daily to-do item')
        print('7. Delete a daily to-do item\n')
        answer = input('What would you like to do? ')
        if answer == '1':
            calender = Calender()
        elif answer == '2':
            calender.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calender.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calender))
        elif answer == '5':
            calender.start_new_day()
        elif answer == '6':
            calender.to_do_list.create_daily_to_do()
        elif answer == '7':
            calender.to_do_list.delete_daily_to_do()

main()










