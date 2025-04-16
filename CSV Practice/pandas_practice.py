import pandas
#data object
data = pandas.read_csv("CSV Practice\weather_data.csv")
#display all csv data
# print(data)

#display specific column 'temp'
print(data['condition'])