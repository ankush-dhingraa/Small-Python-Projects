import pandas
data = pandas.read_csv(r"The Great Squirrel Census Data Analysis with Pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data['Primary Fur Color']=='Gray'])
red_squirrels = len(data[data['Primary Fur Color']=='Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color']=='Black'])
dict = {
    'Fur color' : ['Grey', 'Cinnamon', 'Black'],
    'Count' : [grey_squirrels,red_squirrels,black_squirrels]
}

new_data = pandas.DataFrame(dict)
new_data.to_csv(r"The Great Squirrel Census Data Analysis with Pandas\Squirrel count by color copy.csv", index=False)
# print(count_dict)