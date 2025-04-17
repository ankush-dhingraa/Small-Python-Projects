import pandas
data = pandas.read_csv("CSV Practice\weather_data.csv")
# print(data["day"][7]
#method 1
temperature_list = data["temp"].to_list()
print(f"Average per day temperature is {round(sum(temperature_list)/len(temperature_list),2)}")
#method 2
print(f"Average per day temperature is {data["temp"].mean()}")
print(f"Maximum temperature is : {data['temp'].max()}")
