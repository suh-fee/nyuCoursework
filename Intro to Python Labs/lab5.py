# Problem 1

def read_file(filename):
    f = open(filename , "r")
    f.readline()
    colleges = []
    for line in f:
        fields = line.split(",")
        colleges.append(fields)
    f.close()
    return colleges



# Problem 2

def find_exclusive_womens_college(colleges):
    mostname = ""
    mostadmin = 1.0
    for college in colleges:
        if college[22] == "1":
            if float(college[24]) < mostadmin:
                mostadmin = float(college[24])
                mostname = college[3]

    return mostname

# print("The most selective women's college is: " + find_exclusive_womens_college(read_file("colleges.csv")))






# Problem 3

def consecutive_numbers(filename, n):
    output_lst = []
    for i in range(1, n + 1):
        output_lst.append(str(i) + "\n")
    file_write_obj = open(filename, "w")
    file_write_obj.writelines(output_lst)
    file_write_obj.close()


consecutive_numbers("output.txt",10)


# Problem 4

def squared_numbers(filename, outFile):
    file_obj = open(filename, "r")

    output_lst = []
    for line in file_obj:
        output_lst.append(str(int(line.strip()) ** 2) + "\n")
    file_obj.close()

    file_write_obj = open(outFile, "w")
    file_write_obj.writelines(output_lst)
    file_write_obj.close()


squared_numbers("output.txt","squared_output.txt")

# Problem 5

def get_data_list(file_name):
    file_obj = open(file_name, "r")
    data_list = []
    file_obj.readline()
    for line in file_obj:
        lst = line.strip().split(",")
        data_list.append(lst)

    return data_list


# print(get_data_list("TSLA.csv"))

def get_monthly_averages(data_list):
    beg_month = data_list[0][0][:7] #First month
    sum_close = 0 # v1c1 + v2c2 +... vncn
    sum_vol = 0 #v1+v2+...+vn
    ret_lst = [] #output list
    for day in data_list:
        month = day[0][:7]
        if beg_month == month:
            sum_close += float(day[5]) * int(day[6])
            sum_vol += int(day[6])
        else:
            avg = sum_close / sum_vol
            ret_lst.append((beg_month, avg))
            beg_month = month
            sum_close = float(day[5]) * int(day[6])
            sum_vol = int(day[6])
    avg = sum_close / sum_vol
    ret_lst.append((beg_month, avg))
    return ret_lst


def print_info(monthly_averages_list):
    new_lst = []
    for date, avg in monthly_averages_list:
        new_lst.append((avg, date))

    new_lst.sort()

    worst = new_lst[:6]
    worst.reverse()

    new_lst.reverse()

    best = new_lst[:6]

    print("Best months")
    for avg, date in best:
        print(date, avg)

    print("Worst months")
    for avg, date in worst:
        print(date, avg)


def main():
    data_list = get_data_list("TSLA.csv")

    monthly_averages_list = get_monthly_averages(data_list)
    # print("Monthly averages:")
    # for elem in monthly_averages_list:
    #     print(elem)
    print_info(monthly_averages_list)

main()