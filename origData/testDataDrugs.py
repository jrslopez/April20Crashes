import csv

non_fatal_neg = 0
non_fatal_pos = 0
non_fatal_unk = 0
fatal_neg = 0
fatal_pos = 0
fatal_unk = 0

for i in range (1992,2017):

    folder_path = 'origData/testCleanData/April27'
    file_name = 'PERSON' + str(i) + '.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        death_month_index = headers.index('DEATH_MO')
        drugs_index = headers.index('DRUGS')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (row[death_month_index] == '0'):
                if (row[drugs_index] == '0'):
                    non_fatal_neg += 1
                elif (row[drugs_index] == '1'):
                    non_fatal_pos += 1
                else: non_fatal_unk += 1
            elif(row[death_month_index] != '0'):
                if (row[drugs_index] == '0'):
                    fatal_neg += 1
                elif (row[drugs_index] == '1'):
                    fatal_pos += 1
                else: fatal_unk += 1
                
print('total fatal negative is ' + str(fatal_neg))
print('total non-fatal negative is ' + str(non_fatal_neg))        
print('total fatal positive is ' + str(fatal_pos))
print('total non-fatal positive is ' + str(non_fatal_pos))  
print('total fatal unknown is ' + str(fatal_unk))
print('total non-fatal unknown is ' + str(non_fatal_unk))  