import random
from ascii_art import logo
print(logo)
print("***************************[ START ]***************************")
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
    if num == 1:
        print(f"\n\nYour cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards}\n")
    else:
        print(f"\n\nYour final hand: {user_cards}, final score: {sum(user_cards)}\nComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")
    
def check_status():
    if sum(user_cards) == 21:
        return True
    elif sum(user_cards)>21:
        return False

    




while should_play:
    choice_for_play = input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice_for_play == "y":
        give_cards_to_user(2)
        if check_status():
            win = True
            taking_card =False
        give_cards_to_computer()
        info_print()
        while taking_card:
            user_input = input("\n\nType 'y' (HIT) to get another card, type 'n' (STAND) to pass : ").lower()
            if user_input == "y":
                give_cards_to_user()
                info_print()
                if check_status():
                    win = True
                    taking_card = False
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
                info_print(0)
                print("Match draw :----")
            else:
                if sum(user_cards) == 21:
                    info_print(0)
                    print("\nWin with a Blackjack 😎\n")
                else:
                    info_print(0)
                    print("Opponent went over. You win 😁")
        else:
            info_print(0)
            print("You lose 😤")
        user_cards.clear()
        computer_cards.clear()
        should_play = True
        taking_card = True
        win = False
        draw = False
    else:
        should_play = False
        print("Good bye :)-")
        print("***************************[ EXIT ]***************************")
