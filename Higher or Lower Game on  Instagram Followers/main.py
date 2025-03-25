#Random module
import random
from ascii_art import logo,vs
from game_data import data
data_a = {}
data_b = {}
score = 0
def compare(data_a,data_b,choice):
    global score
    if data_a["follower_count"] > data_b["follower_count"]:
        if choice == "a":
            score += 1
    elif data_a["follower_count"] < data_b["follower_count"]:
        if choice == "b":
            score += 1
def display(item):
    account_name = item["name"]
    account_descr = item["description"]
    account_country = item["country"]
    print(f"{account_name}, a {account_descr}, from {account_country}")
def initialize_data():
    global data_a,data_b
    data_a = random.choice(data)
    flag = True
    while flag:
        temp = random.choice(data)
        if data_a != temp:
            data_b = temp
            flag = False
initialize_data()
display(data_a)
display(data_b)