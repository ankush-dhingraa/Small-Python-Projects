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

#get data in column ( Dictionary-style access,Returns a Series (single column).)
print(data["condition"])
#this is also valid (Attribute-style access,Returns a Series (single column).)
print(data.condition)
#get data in row
print(data[data.temp == data.temp.max()])
#also can use this 
print(data[data["temp"] == data['temp'].max()])

#particular row and column
monday = data[data.day == 'Monday']
print("\nMonday Condition\n")
print(monday.condition)
print("\nMonday temperature\n")
print((monday.temp*9/5)+32) # also use *1.8 instead (9/5 )

#create a dataFrame from scratch
data_dict = {
    'students' : ['Ankush','Saksham','Armaan'],
    'marks' : [29,25,17]
}
data_d = pandas.DataFrame(data_dict)
print(data_d)
csv = data_d.to_csv("CSV Practice\student marks.csv")