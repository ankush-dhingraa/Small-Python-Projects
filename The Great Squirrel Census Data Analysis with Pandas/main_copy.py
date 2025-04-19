import pandas
data = pandas.read_csv(r"The Great Squirrel Census Data Analysis with Pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unique_color = data['Primary Fur Color'].unique()
# print(unique_color)
count_dict = {}
for color in unique_color[1:]:
    count_dict[color] = data[data['Primary Fur Color']==color].shape[0]
# print(count_dict)