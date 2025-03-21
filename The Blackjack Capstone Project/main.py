import random
from ascii_art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
should_play = True
taking_card = True
win = False
draw = False
#for user 
def give_cards_to_user(num = 1):
    for i in range(num):
        user_cards.append(random.choice(cards))
#for computer
def give_cards_to_computer(num = 1):
    for i in range(num):
        computer_cards.append(random.choice(cards))

def info_print(num = 1):
    if num:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards}")

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards}")
    
def check_status():
    if sum(user_cards) == 21:
        return True
    elif sum(user_cards)>21:
        return False

    




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
                if check_status:
                    win = True
            else:
                taking_card = False
        if not win:
            while sum(computer_cards) <= 17:
                give_cards_to_computer()
        if sum(computer_cards) >=21:
            win = True
        elif sum(computer_cards) < sum(user_cards):
            win = True
        elif sum(computer_cards) == sum(user_cards):
            draw = True
        else:
            win = False

        if win:
            if draw:
                info_print()
                print("Match draw :----")
            else:
                if sum(user_cards) == 21:
                    info_print()
                    print("\nWin with a Blackjack 😎\n")
                else:
                    info_print()
                    print("Opponent went over. You win 😁")
        else:
            info_print()
            print("You lose 😤")



        check_status()
    else:
        should_play = False
