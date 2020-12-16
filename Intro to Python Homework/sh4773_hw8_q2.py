'''

Safi
CS 1114
sh4773

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    f = open(complete_weather_filename, "r")
    final_list = []
    for line in f:
        list = line.split(",")
        compare = list[8]
        if compare != 'T':
            cleaned = list[0] + ',' + list[1] + ',' + list[2] + ',' + list[3] + ',' + list[8]
        elif compare == 'T':
            cleaned = list[0] + ',' + list[1] + ',' + list[2] + ',' + list[3] + ',0'
        final_list.append(cleaned)
    f.close()
    f = open(cleaned_weather_filename, "w")
    for i in range(len(final_list)):
        print(final_list[i], file=f)
    f.close()


    
clean_data("hw8 - weather.csv", "weather_cleaned.txt")

# Part B


def f_to_c(f_temperature):
    c_temp = (float(f_temperature) - 32) * (5/9)
    return c_temp


def in_to_cm(inches):
    cm = float(inches) * 2.54
    return cm


def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    f = open(imperial_weather_filename, "r")
    final_list = []
    for line in f:
        list = line.split(",")
        if list[0] != 'City':
            metric_list = list[0] + ", " + list[1] + ", " + str(round(f_to_c(list[2]), 2)) + ", " + str(round(f_to_c(list[3]), 2)) + ", " + str(round(in_to_cm(list[4]), 2))
            final_list.append(metric_list)
    f.close()
    f = open(metric_weather_filename, "w")
    print("City,Date,High,Low,Precipitation", file=f)
    for i in range(len(final_list)):
        print(final_list[i], file=f)
    f.close()









# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    f = open(weather_filename, 'r')
    counter = 0
    dates = [['January', 0, 0, 0], ['February', 0, 0, 0], ['March', 0, 0, 0], ['April', 0, 0, 0], ['May', 0, 0, 0],
             ['June', 0, 0, 0], ['July', 0, 0, 0], ['August', 0, 0, 0], ['September', 0, 0, 0], ['October', 0, 0, 0],
             ['November', 0, 0, 0], ['December', 0, 0, 0]] # month, high added, low added, num of days to div by
    for line in f:
        master_list = line.split(',')
        if master_list[0] == city:
            date = master_list[1].split('/')
            month = int(date[0]) - 1  # to find place in dates
            high_temp = float(master_list[2])
            low_temp = float(master_list[3])
            dates[month][1] = dates[month][1] + high_temp  # increase high temp
            dates[month][2] = dates[month][2] + low_temp  # ' ' low temp
            dates[month][3] += 1  # counter of days of each month
    print('Average temperatures for ' + city + ":")
    for i in range(12):
        high = round((dates[i][1]) / (dates[i][3]), 2)
        low = round((dates[i][2]) / (dates[i][3]), 2)
        if unit_type == 'imperial' or unit_type == 'Imperial':
            print(dates[i][0] + ': ' + str(high) + 'F High, ' + str(low) + 'F Low')
        elif unit_type == 'metric' or unit_type == 'Metric':
            print(dates[i][0] + ': ' + str(high) + 'C High, ' + str(low) + 'C Low')
    f.close()

print_averages_per_month('San Francisco', 'weather_cleaned.txt', 'metric')







    # prints average highs and lows in each month for the given city



# Part D
# given two cities, which has a hotter summer (june, july, august comparison using high temps)?

def higher_average_temp(city, city2, weather_filename):
    f = open(weather_filename, 'r')
    counter = 0
    dates1 = [['January', 0, 0, 0], ['February', 0, 0, 0], ['March', 0, 0, 0], ['April', 0, 0, 0], ['May', 0, 0, 0],
             ['June', 0, 0, 0], ['July', 0, 0, 0], ['August', 0, 0, 0], ['September', 0, 0, 0], ['October', 0, 0, 0],
             ['November', 0, 0, 0], ['December', 0, 0, 0]] # month, high added, low added, num of days to div by
    dates2 = [['January', 0, 0, 0], ['February', 0, 0, 0], ['March', 0, 0, 0], ['April', 0, 0, 0], ['May', 0, 0, 0],
              ['June', 0, 0, 0], ['July', 0, 0, 0], ['August', 0, 0, 0], ['September', 0, 0, 0], ['October', 0, 0, 0],
              ['November', 0, 0, 0], ['December', 0, 0, 0]]  # month, high added, low added, num of days to div by
    for line in f:
        master_list = line.split(',')
        if master_list[0] == city:
            date = master_list[1].split('/')
            month = int(date[0]) - 1  # to find place in dates
            high_temp = float(master_list[2])
            low_temp = float(master_list[3])
            dates1[month][1] = dates1[month][1] + high_temp  # increase high temp
            dates1[month][2] = dates1[month][2] + low_temp  # ' ' low temp
            dates1[month][3] += 1  # counter of days of each month
        if master_list[0] == city2:
            date = master_list[1].split('/')
            month = int(date[0]) - 1  # to find place in dates
            high_temp = float(master_list[2])
            low_temp = float(master_list[3])
            dates2[month][1] = dates2[month][1] + high_temp  # increase high temp
            dates2[month][2] = dates2[month][2] + low_temp  # ' ' low temp
            dates2[month][3] += 1  # counter of days of each month
    total_days = dates1[5][3] + dates1[6][3] + dates1[7][3]
    average_heat1 = (dates1[5][1] + dates1[6][1] + dates1[7][1]) / total_days
    average_heat2 = (dates2[5][1] + dates2[6][1] + dates2[7][1]) / total_days
    if average_heat1 > average_heat2:
        print(city + ' in the summer is hotter than ' + city2)
    elif average_heat1 < average_heat2:
        print(city2 + 'in the summer is hotter than ' + city)


def main():
    print ("Running Part A")
    clean_data("hw8 - weather.csv", "weather in imperial.csv")

    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")

    print ("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    city1 = input('Please enter a city: ')
    city2 = input('Please enter another city: ')
    temp_type = input('Please enter imperial (I) or metric (M): ')
    if temp_type == 'I':
        higher_average_temp(city1, city2, 'weather in imperial.csv')
    if temp_type == 'M':
        higher_average_temp(city1, city2, 'weather in metric.csv')


main()
