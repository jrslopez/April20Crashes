import csv

fatal_evening = 0
non_fatal_evening = 0
fatal_late = 0
non_fatal_late = 0

for i in range (1992,2017):

    folder_path = 'origData/testCleanData/April27'
    file_name = 'ACCIDENT' + str(i) + '.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        fatals_index = headers.index('FATALS')
        persons_index = headers.index('PERSONS')
        hour_index = headers.index('HOUR')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (int(row[hour_index]) >= 16 and int(row[hour_index]) <= 19):
                fatal_evening = fatal_evening + int(row[fatals_index])
                non_fatal_evening = non_fatal_evening + (int(row[persons_index]) - int(row[fatals_index]))
            elif (int(row[hour_index]) >= 20 and int(row[hour_index]) <= 23):
                fatal_late = fatal_late + int(row[fatals_index])
                non_fatal_late = non_fatal_late + (int(row[persons_index]) - int(row[fatals_index]))

print('total fatal count from 1992 to 2016 in the evening is ' + str(fatal_evening))
print('total non-fatal count from 1992 to 2016 in the evening is ' + str(non_fatal_evening))        
print('total fatal count from 1992 to 2016 late night is ' + str(fatal_late))
print('total non-fatal count from 1992 to 2016 late night is ' + str(non_fatal_late))
