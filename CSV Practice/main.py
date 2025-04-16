import csv
with open("CSV Practice\weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
    temperatures = []
    for row in data:
        temp = row[1].isnumeric()
        if temp:
            temperatures.append(int(row[1]))
        
print(temperatures)
