from os import path
import random

random.seed()

print("Let's play hangman!")

min_length = 4
max_length = 12
words = []

# read in the words from the file

with open(path.join("assignments", "words.txt"), "r", encoding="utf-8") as file:
    for line in file:
        if min_length <= len(line.strip()) <= max_length:
            words.append(line.strip())

# determine word length by choosing a word at random

word_length = len(words[random.randint(0, len(words) - 1)])

# remove words that don't match the length of the chosen word

new_words = []
word_with_blanks = ["_"] * word_length
correct_word = None
incorrect_guesses = []
num_guesses = 10

for word in words:
    if len(word) == word_length:
        new_words.append(word)

words = new_words

# game loop

while True:
    print()
    print(' '.join(word_with_blanks))
    print()
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"You have {num_guesses} guesses left.")
    if correct_word is None:
        print(f"{len(words)} possible words remain.")
    else:
        print("1 possible word remains.")
    letter = input("Guess a letter: ").lower().strip()

    if len(letter) != 1:
        print("Please guess a single letter.")
    elif letter in incorrect_guesses or letter in word_with_blanks:
        print(f"You already guessed {letter}. Try again.")
    else:
        if correct_word is None:
            new_words = []

            for word in words:
                if letter not in word:
                    new_words.append(word)

            if len(new_words) > 0:
                words = new_words
                incorrect_guesses.append(letter)
                num_guesses -= 1
                print(f"Sorry, {letter} is not in the word.")
            else:
                # choose a random word from the remaining words
                correct_word = words[random.randint(0, len(words) - 1)]

        if correct_word is not None:
            if letter in correct_word:
                print(f"Good guess! {letter} is in the word.")
                new_word_with_blanks = ""
                for (i, ch) in enumerate(word_with_blanks):
                    if correct_word[i] == letter:
                        new_word_with_blanks += letter
                    else:
                        new_word_with_blanks += ch
                word_with_blanks = new_word_with_blanks
            else:
                incorrect_guesses.append(letter)
                num_guesses -= 1
                print(f"Sorry, {letter} is not in the word.")

    if "_" not in word_with_blanks:
        print(f"Congratulations! You guessed the word: {correct_word}")
        break

    if num_guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was: {correct_word}")
        break
