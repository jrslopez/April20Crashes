import csv

# NEED TO CHANGE YEARS FROM REMOTE (1996-2003) TO RECENT (2004-2016)

fatal_remote = 0
non_fatal_remote = 0


for i in range (1992,2004):

    folder_path = 'origData/testCleanData/April27'
    file_name = 'PERSON' + str(i) + '.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        death_month_index=headers.index('DEATH_MO')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (row[death_month_index] == '0'):
                non_fatal_remote += 1
            else: fatal_remote += 1

print('total fatal count from 1992 to 2003 is ' + str(fatal_remote))
print('total non-fatal count from 1992 to 2003 is ' + str(non_fatal_remote))        

