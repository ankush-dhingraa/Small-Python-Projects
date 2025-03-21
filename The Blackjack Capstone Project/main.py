import random
from ascii_art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
should_play = True
taking_card = True
#for user 
def give_cards_to_user(num = 1):
    for i in range(num):
        user_cards.append(random.choice(cards))
#for computer
def give_cards_to_computer(num = 1):
    for i in range(num):
        computer_cards.append(random.choice(cards))

def info_print():
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards}")
    
def check_status():
    if sum(user_cards) == 21:

    




while should_play:
    choice_for_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice_for_play == "y":
        give_cards_to_user(2)
        give_cards_to_computer()
        info_print()
        check_status()
        while taking_card:
            user_input = input("Type 'Hit' to get another card, type 'stand' to pass: ").lower()
            if user_input == "hit":
                give_cards_to_user()
            else:
                taking_card = False

        check_status()
    else:
        should_play = False
