import random
from ascii_art import logo,winner
game_over = False
lives = 0
# number between 1 to 100
number_to_guess = random.randint(1,100)
def check():

while not game_over:
    print(logo)
    print("*********************************[ START ]*********************************")
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Select a difficulty level: Type 'easy' or 'hard' : ")
    if level == "easy":
        lives = 10
    else:
        lives = 5
    
    while lives >0:
        guess = int(input("Make a guess: "))
        check(guess)
        
