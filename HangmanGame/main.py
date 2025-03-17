import random
from hangman_ascii_art import stages, logo
from hangman_words_list import word_list
#Step 1
print(logo)
chosen_word = random.choice(word_list)
placeholder = "_"*len(chosen_word)
lives = 6
game_over = False
correct_letter = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in correct_letter:
        print(f"You've already guessed : {guess}")
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(f"Word to guess : {display}")

    if guess not in chosen_word:
        print(f"{guess} is not in the word to guess :( You lose a live")
        live -= 1
        if lives == 0:
            game_over = True 
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
