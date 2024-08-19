'''This Hangman game program is a simple text-based version of the classic word-guessing game. Here’s how it works:

1. Choosing a Word:
   - The program imports necessary modules: `random`, `hangman_stages`, and `words_file`.
   - It selects a random word from a list of words stored in `words_file.words`.

2. Setting Up the Game:
   - The player starts with 6 attempts (`attempts = 6`).
   - The `finding_word` variable stores the randomly selected word.
   - An empty `display` list is created to represent the word with underscores (`_`) for each letter, showing what the player has guessed correctly so far.

3. Gameplay Loop:
   - The game runs in a loop until `end_game` is set to `True`.
   - The player is asked to guess a letter (`guessed_letter`), which is converted to lowercase.
   - The program checks if the guessed letter is in the word:
     - If it is, the letter is placed in the correct positions in the `display`.
     - If the guessed letter is not in the word, the player loses an attempt.
     - The hangman’s current stage (visual representation) is printed based on the remaining attempts.
   - The game ends in one of two ways:
     - If the player runs out of attempts (`attempts == 0`), they lose, and the game ends with a "You Lose!!!" message.
     - If the player correctly guesses all the letters in the word (no underscores left in `display`), they win, and the game ends with a "You Win!!!" message.

4. Hangman Stages:
   - The hangman drawing updates after each incorrect guess, providing visual feedback on how many guesses remain before the game is lost.

This game allows players to guess letters one at a time to uncover a hidden word, with the challenge of not exceeding the maximum allowed incorrect guesses.'''


import random
import hangman_stages
import words_file

attempts = 6
finding_word = random.choice(words_file.words)
print(finding_word)
display = []

for i in range(len(finding_word)):
    display += '_'
print(display)

end_game = False

while not end_game:
    guessed_letter = input("Guess a Letter of Colour: ").lower()
    for position in range(len(finding_word)):
        letter = finding_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in finding_word:
        attempts -= 1
        if attempts == 0:
            end_game = True
            print("\nYou Lose!!!")

    if '_' not in display:
        end_game = True
        print("\nYou Win!!!")
    print(hangman_stages.stages[attempts])