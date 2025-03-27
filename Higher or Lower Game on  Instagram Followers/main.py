#Random module
import random
from ascii_art import logo,vs
from game_data import data
data_a = {}
data_b = {}
score = 0
game_over = False
def compare(data_a,data_b,choice):
    global score
    if data_a["follower_count"] > data_b["follower_count"]:
        if choice == "a":
            score += 1
            return True
    elif data_a["follower_count"] < data_b["follower_count"]:
        if choice == "b":
            score += 1
            return True
    else:
        return False
    
def display(item,type):
    account_name = item["name"]
    account_descr = item["description"]
    account_country = item["country"]
    if type == "a":
        print(f"Compare A: {account_name}, a {account_descr}, from {account_country}")
    elif type == "b":
        print(f"Compare B: {account_name}, a {account_descr}, from {account_country}")
def initialize_data():
    global data_a,data_b
    data_a = random.choice(data)
    flag = True
    while flag:
        temp = random.choice(data)
        if data_a != temp:
            data_b = temp
            flag = False
while not game_over:
    print(logo,"\n")
    initialize_data()
    display(data_a,"a")
    print(vs)
    display(data_b,"b")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if compare(data_a,data_b,answer):
        print("\n"*50)
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong :-(, Final score: {score}")
        game_over = True

