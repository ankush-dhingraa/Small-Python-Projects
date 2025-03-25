#Random module
import random
from ascii_art import logo,vs
from game_data import data
data_a = {}
data_b = {}
def data_to_compare():
    global data_a,data_b
    data_a = random.choice(data)
    flag = True
    while flag:
        temp = random.choice(data)
        if data_a != temp:
            data_b = temp
            flag = False
data_to_compare()
print(data_a,"\n",data_b)
