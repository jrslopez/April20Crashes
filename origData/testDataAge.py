import csv

fatal_count_younger_20 = 0
non_fatal_count_younger_20 = 0
fatal_count_21to30 = 0
non_fatal_count_21to30 = 0
fatal_count_31to40 = 0
non_fatal_count_31to40 = 0
fatal_count_41to50 = 0
non_fatal_count_41to50 = 0
fatal_count_older_50 = 0
non_fatal_count_older_50 = 0

for i in range (1992,2017):

    folder_path = 'origData/testCleanData/April27'
    file_name = 'PERSON' + str(i) + '.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        death_month_index=headers.index('DEATH_MO')
        age_index = headers.index('AGE')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (int(row[age_index]) <= 20):
                if (row[death_month_index] == '0'):
                    non_fatal_count_younger_20 += 1
                else: fatal_count_younger_20 += 1
            elif (int(row[age_index]) > 20 and int(row[age_index]) <= 30):
                if (row[death_month_index] == '0'):
                    non_fatal_count_21to30 += 1
                else: fatal_count_21to30 += 1
            elif (int(row[age_index]) > 30 and int(row[age_index]) <= 40):
                if (row[death_month_index] == '0'):
                    non_fatal_count_31to40 += 1
                else: fatal_count_31to40 += 1
            elif (int(row[age_index]) > 40 and int(row[age_index]) <= 50):
                if (row[death_month_index] == '0'):
                    non_fatal_count_41to50 += 1
                else: fatal_count_41to50 += 1
            elif (int(row[age_index]) > 50):
                if (row[death_month_index] == '0'):
                    non_fatal_count_older_50 += 1
                else: fatal_count_older_50 += 1

print('total fatal count from 1992 to 2016 for people 20 or younger is ' + str(fatal_count_younger_20))
print('total non-fatal count from 1992 to 2016 for people 20 or younger is ' + str(non_fatal_count_younger_20))        
print('total fatal count from 1992 to 2016 for people 21 to 30 is ' + str(fatal_count_21to30))
print('total non-fatal count from 1992 to 2016 for people 21 to 30 is ' + str(non_fatal_count_21to30))
print('total fatal count from 1992 to 2016 for people 31 to 40 is ' + str(fatal_count_31to40))
print('total non-fatal count from 1992 to 2016 for people 31 to 40 is ' + str(non_fatal_count_31to40))
print('total fatal count from 1992 to 2016 for people 41 to 50 is ' + str(fatal_count_41to50))
print('total non-fatal count from 1992 to 2016 for people 41 to 50 is ' + str(non_fatal_count_41to50))
print('total fatal count from 1992 to 2016 for people 50 or older is ' + str(fatal_count_older_50))
print('total non-fatal count from 1992 to 2016 for people 50 or older is ' + str(non_fatal_count_older_50)) 