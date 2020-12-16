# a


class Student(object):
    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = []

    def add_grade(self, catalog_name, grade):
        self.grades_list.append((catalog_name, grade))

    def average(self):
        sum = 0
        counter = 0
        for i in range(len(self.grades_list)):
            if str(self.grades_list[i][1]).isnumeric() == True: # turns the int into a string. if there is no int, in
                # case the student isn't taking the class, then it will return false.
                sum += self.grades_list[i][1]
                counter += 1
        average = sum / counter
        return average

    def get_email(self):
        email = self.net_id + "@nyu.edu"
        return email

# b


def load_students(students_data_filename):
    f = open(students_data_filename, "r")
    master_list = []
    counter = 0
    for line in f:
        counter += 1
        if counter == 1:
            class_list = line.split(',')
            class_list = class_list[3:10]
        else:
            split = line.split(',')
            name = split[1]
            NYU_id = split[0]
            net_id = split[2]
            student = Student(name, NYU_id, net_id)
            grade_list = split[3:10]
            for i in range(len(grade_list)):
                if grade_list[i].isnumeric():
                    student.add_grade(class_list[i], int(grade_list[i]))
                else:
                    student.add_grade(class_list[i], '')
            master_list.append(student)
    f.close()
    return master_list

# c


def generate_performance_report(students_lst, out_filename):
    f = open(out_filename, "w")
    print("NYU ID,Average", file=f)
    for i in range(len(students_lst)):
        average = students_lst[i].average()
        line = students_lst[i].NYU_id
        print(line + ',' + str(int(average)), file=f)
    f.close()


# d


def generate_course_mailing_list(catalog_name, out_filename, master_list):
    f = open(out_filename, "w")
    for i in range(len(master_list)):
        for x in range(len(master_list[i].grades_list)):
            if master_list[i].grades_list[x][0] == catalog_name and str(master_list[i].grades_list[x][1]).isnumeric():
                print(master_list[i].get_email(), file=f)
    f.close()


# e

def main():
    student_list = load_students('hw9 - students grades.csv')
    generate_performance_report(student_list, 'performance report.csv')
    generate_course_mailing_list("CS-UY 1114", "CS-UY 1114 Mailing List.txt", student_list)
    generate_course_mailing_list("MA-UY 1024", "MA-UY 1024 Mailing List.txt", student_list)
    generate_course_mailing_list("EG-UY 1001", "EG-UY 1001 Mailing List.txt", student_list)
    generate_course_mailing_list("EG-UY 1003", "EG-UY 1003 Mailing List.txt", student_list)
    generate_course_mailing_list("CS-UY 1122", "CS-UY 1122 Mailing List.txt", student_list)
    generate_course_mailing_list("CS-UY 1134", "CS-UY 1134 Mailing List.txt", student_list)
    generate_course_mailing_list("CS-UY 1114", "MA-UY 1124 Mailing List.txt", student_list)


main()
