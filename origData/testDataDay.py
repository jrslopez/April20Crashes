import csv

fatal_weekday = 0
non_fatal_weekday = 0
fatal_weekend = 0
non_fatal_weekend = 0

for i in range (1992,2017):

    folder_path = 'origData/testCleanData/April27'
    file_name = 'ACCIDENT' + str(i) + '.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        day_index = headers.index('DAY_WEEK')
        fatals_index = headers.index('FATALS')
        persons_index = headers.index('PERSONS')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (row[day_index] == '1' or row[day_index] == '6' or row[day_index] == '7'):
                fatal_weekend = fatal_weekend + int(row[fatals_index])
                non_fatal_weekend = non_fatal_weekend + (int(row[persons_index]) - int(row[fatals_index]))
            elif (row[day_index] == '2' or row[day_index] == '3' or row[day_index] == '4' or row[day_index] == '5' or row[day_index] == '9'):
                fatal_weekday = fatal_weekday + int(row[fatals_index])
                non_fatal_weekday = non_fatal_weekday + (int(row[persons_index]) - int(row[fatals_index]))

print('total fatal count from 1992 to 2016 weekends is ' + str(fatal_weekend))
print('total non-fatal count from 1992 to 2016 weekends is ' + str(non_fatal_weekend))        
print('total fatal count from 1992 to 2016 weekdays is ' + str(fatal_weekday))
print('total non-fatal count from 1992 to 2016 weekdays is ' + str(non_fatal_weekday))
