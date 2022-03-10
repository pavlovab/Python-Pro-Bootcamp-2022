from art import logo 
import random
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear(): 
    os.system('cls') 

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else: 
        input("Choose a diggiculty. Type 'easy' or 'hard': ").lower()
        return -1

def generate_number():
    number = random.randint(1, 100)
    return number

def check_user_guess(initial_number, user_guess, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if initial_number > user_guess:
        print("Too low.")
        return turns - 1
    elif initial_number < user_guess:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it! The answer was {initial_number}.")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    if turns == -1:    
        return

    number = generate_number()
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_user_guess(number, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


while input("Do you want to start a new game? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game()