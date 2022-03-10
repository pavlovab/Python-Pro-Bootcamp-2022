import random
import art
from game_data import data
import os

def clear():
    os.system('cls') 

def get_random_celebrity():
    celebrity = random.choice(data)
    return celebrity

def format_data(celebrity_account):
    """Format account into printable format: name, description and country"""
    name = celebrity_account['name']
    description = celebrity_account['description']
    country = celebrity_account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
def game():
    print(art.logo)
    score = 0
    should_continue = True
    celeb_a = get_random_celebrity()
    celeb_b = get_random_celebrity()

    while should_continue:
        celeb_a = celeb_b
        celeb_b = get_random_celebrity()
        while celeb_a == celeb_b:
            celeb_b = get_random_celebrity()

        print(f"Compare A: {format_data(celeb_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(celeb_b)}.")

        answer = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()
        if answer != 'a' and answer != 'b':
            print("Invalid choice!")
            break
        a_follower_count = celeb_a["follower_count"]
        b_follower_count = celeb_b["follower_count"]
        is_correct = check_answer(answer, a_follower_count, b_follower_count)

        clear()
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). 
Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between 
Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. 
If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. 
This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of 
choice A keeps going up over the course of the game. Hope that makes sense :-)

'''
