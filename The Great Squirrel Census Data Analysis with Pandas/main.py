from time import process_time_ns

import pandas
from numpy.ma.core import count

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data['Primary Fur Color'].unique()
fur_color = []
fur_color.extend(color[1:])
print(fur_color)
count = []
for colour in fur_color:
    count.append(data[data['Primary Fur Color'] == colour].shape[0])
print(count)
#
# color_counts = data['Primary Fur Color'].value_counts()
# print(color_counts)
