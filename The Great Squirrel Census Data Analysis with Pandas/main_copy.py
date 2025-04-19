import pandas
data = pandas.read_csv(r"The Great Squirrel Census Data Analysis with Pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unique_color = data['Primary Fur Color'].unique()
# print(unique_color)
count_dict = {}
for color in unique_color[1:]:
    count_dict[color] = data[data['Primary Fur Color']==color].shape[0]
new_data = pandas.DataFrame(list(count_dict.items()),columns=["Fur Colour","Total Count"])
new_data.to_csv(r"The Great Squirrel Census Data Analysis with Pandas\Squirrel count by color copy.csv", index=False)
# print(count_dict)