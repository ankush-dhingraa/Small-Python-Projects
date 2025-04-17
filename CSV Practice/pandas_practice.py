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
print(data_dict)
# print(data["day"][7]
#method 1
temperature_list = data["temp"].to_list()
print(f"Average per day temperature is {round(sum(temperature_list)/len(temperature_list),2)}")
#method 2
print(f"Average per day temperature is {data["temp"].mean()}")
print(f"Maximum temperature is : {data['temp'].max()}")