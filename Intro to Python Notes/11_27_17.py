# write a program that reads a comma seperated list of values in a file and adds them together. it writes
# them in answers.txt in the correct order

def read_file(infile):
    f = open(infile, "r")
    answers = []
    for line in f:
        first, second = parse_line(line)
        add_and_accumulate(first, second, answers)
    return answers


def parse_line(line):
    line = line.strip()
    numbers = line.split(',')
    first = int(numbers[0])
    second = int(numbers[1])
    return first, second


def add_and_accumulate(first, second, answers):
    answers.append(first + second)
    return answers


def write_answers(numbers, output_file):
    output_file = open(output_file, 'w')
    for i in numbers:
        print(i, file=output_file)
    return output_file


def main():
    input_file = "html.txt"
    output_file = "output.txt"
    numbers = read_file(input_file)
    write_answers(numbers, output_file)

main()

# class Student(object):
#     def __init__(self):
#         self.name = "Omar"
#         self.gpa = "4.0"
#         self.classes = []
#
# my_student = Student.gpa()
# print(my_student)
