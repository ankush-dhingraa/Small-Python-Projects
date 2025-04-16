import csv
with open("weather_data.csv") as csv_file:
    data = csv.reader(csv_file)
print(data)