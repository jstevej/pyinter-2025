import random


num_guesses = 6
words = ['code']
index = random.randint(0, len(words) - 1)
word = words[index]
word_with_blanks = "_" * len(word)
incorrect_guesses = []

print("Let's play hangman!")

while True:
    print()
    print(' '.join(word_with_blanks))
    print()
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"You have {num_guesses} guesses left.")
    letter = input("Guess a letter: ").lower().strip()

    if len(letter) != 1:
        print("Please guess a single letter.")
    elif letter in incorrect_guesses or letter in word_with_blanks:
        print(f"You already guessed {letter}. Try again.")
    elif letter in word:
        print(f"Good guess! {letter} is in the word.")
        new_word_with_blanks = ""
        for (i, ch) in enumerate(word_with_blanks):
            if word[i] == letter:
                new_word_with_blanks += letter
            else:
                new_word_with_blanks += ch
        word_with_blanks = new_word_with_blanks
    else:
        incorrect_guesses.append(letter)
        num_guesses -= 1
        print(f"Sorry, {letter} is not in the word.")

    if "_" not in word_with_blanks:
        print(f"Congratulations! You guessed the word: {word}")
        break
    if num_guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was: {word}")
        break
