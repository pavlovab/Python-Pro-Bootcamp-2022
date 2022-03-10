import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)

display_of_word = ["_"] * word_len

lives = 6
end_of_game = False

print(hangman_art.logo)

while not end_of_game: 
    print(hangman_art.stages[lives])
    print(f"{' '.join(display_of_word)}")
    guess = input("Guess a letter: ").lower()

    if guess in display_of_word:
        print(f"Already guessed the letter {guess}!")

    if guess in chosen_word:
        for n in range(word_len):
            if chosen_word[n] == guess:
                display_of_word[n] = guess
    else: 
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You ran out of lives! You lose!")
            print(hangman_art.stages[lives])

    if "_" not in display_of_word: 
        end_of_game = True
        print("You guessed the word! You win!")
