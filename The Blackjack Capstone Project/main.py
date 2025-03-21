import random
from ascii_art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
should_play = True
#for user 
def give_cards_to_user(num = 1):
    for i in range(num):
        user_cards.append(random.choice(cards))
#for computer
def give_cards_to_computer(num = 1):
    for i in range(num):
        user_cards.append(random.choice(cards))
while should_play:
    choice_for_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice_for_play == "y":
        give_cards_to_user(2)
        
    else:
        should_play = False
