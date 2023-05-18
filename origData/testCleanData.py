import csv

for i in range (1992,2017):

    folder_path = 'FARSData\FARS' + str(i) + 'NationalCSV'
    file_name = 'ACCIDENT.csv'

    file_path = f'{folder_path}/{file_name}'

    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file)

        # Find the indices of the MONTH, DAY, HOUR, and MINUTE columns
        headers = next(reader)
        month_index = headers.index('MONTH')
        day_index = headers.index('DAY')
        hour_index = headers.index('HOUR')
        minute_index = headers.index('MINUTE')

        # Read the data from the input file where month is April, day is the 20th,
        # hour is greater than or equal to 4, and minute is greater than or equal to 20
        data = [headers]
        for row in reader:
            if (
            row[month_index] == '4'
            and row[day_index] == '27'
            and (
                int(row[hour_index]) != 99
            )
            and (
                int(row[hour_index]) > 16
                or (
                    int(row[hour_index]) == 16
                    and int(row[minute_index]) >= 20
                )
            )
        ):
                data.append(row)
        
    new_folder_path = 'origData/testCleanData/April27'
    new_file_name = 'ACCIDENT' + str(i) + '.csv'

    new_file_path = f'{new_folder_path}/{new_file_name}'

    # Write the filtered data to a new CSV file
    with open(new_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data)

