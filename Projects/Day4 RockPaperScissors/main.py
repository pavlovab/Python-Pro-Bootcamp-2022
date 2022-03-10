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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game_choices = [rock, paper, scissors]

print(game_choices[user_choice])

computer_move = random.randint(0, len(game_choices) - 1)

print("Computer chose: ")
print(game_choices[computer_move])

if user_choice > 2 or user_choice < 0:
    print("You typed in invalid number!")
elif user_choice == computer_move:
    print("It's a draw")
elif user_choice == 0 and computer_move == 2:
    print("You win!")
elif user_choice == 2 and computer_move == 0:
    print("You lose!")
elif user_choice > computer_move:
    print("You win!")
elif user_choice < computer_move:
    print("You lose!")