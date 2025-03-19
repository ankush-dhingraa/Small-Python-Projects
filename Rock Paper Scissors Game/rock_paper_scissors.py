import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

exit_art = '''
.######..##..##..######..######.
.##.......####.....##......##...
.####......##......##......##...
.##.......####.....##......##...
.######..##..##..######....##...  

Thanks for playing! Remember, every game is a chance to improve. Goodbye!
'''
game_images = [rock,paper,scissors,exit_art]
flag = True
while flag:
    user_choice = int(input("What do you Chose? Type 0 for Rock, 1 for Paper, 2 for Scissor or 3 for EXIT # : "))
    if user_choice >=0 and user_choice <=3:
        print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    if user_choice !=3:
        print("Computer Choose : ")
        print(game_images[computer_choice])

    if user_choice >= 4 or user_choice < 0:
        print("You entered an incorrect number. Unfortunately, you've lost :(")
    elif user_choice == 0 and computer_choice == 2:
        print("Rock wins against scissors.\n🏆🏆🏆")
    elif user_choice == 1 and computer_choice == 0:
        print("Paper wins against rock.\n🏆🏆🏆")
    elif user_choice == 2 and computer_choice == 1:
        print("Scissors win against paper.\n🏆🏆🏆")
    elif computer_choice == user_choice:
        print("it is a draw")
    elif user_choice == 3:
        flag = False
    else:
        print("You've been defeated :(")