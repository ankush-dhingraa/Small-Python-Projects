import random
from ascii_art import logo,winner
game_over = False
lives = 0
win = False
# number between 1 to 100
number_to_guess = random.randint(1,100)
def check(guess):
    global lives
    if guess == number_to_guess:
        lives = 0
        global win
        win = True
    else:
        if guess > number_to_guess:
            print("Too High :-")
            print("Guess again.")
        else:
            print("Too Low :-")
            print("Guess again.")
        lives -=1
        print(f"You have {lives} attempts remaining to guess the number.")
      
while not game_over:
    print(logo)
    print("**********************************[ START ]**********************************")
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Select a difficulty level: Type 'easy' or 'hard' : ")
    if level == "easy":
        lives = 10
        print(f"You have {lives} attempts remaining to guess the number.")
    else:
        lives = 5
        print(f"You have {lives} attempts remaining to guess the number.")
    
    while lives >0:
        guess = int(input("Make a guess: "))
        check(guess)
    if win:
        print(f"You got it! The answer was {number_to_guess}")
        winner()
    else:
        print("You've run out of guesses.")
        print("You loss dear :(")
    print("**********************************[ EXIT ]**********************************")
    game_over = True
        
