import pandas
#data object
data = pandas.read_csv("CSV Practice\weather_data.csv")
#display all csv data
# print(data)

#display specific column 'temp'
print(data['condition'])

#csv to dict
data_dict = data.to_dict()
print(data_dict)

#series 1 dim and dataframe dim 2
# create a list from csv series
data_list = data["temp"].to_list()
print(data_list)