import random

words_path = "words.txt"
words = []

with open(words_path, "r", encoding="utf-8") as file:
    for line in file:
        sline = line.strip()
        if (len(sline) >= 4) and (len(sline) <= 7):
            words.append(sline)

num_guesses = 10
index = random.randint(0, len(words) - 1)
word = words[index]
word_with_blanks = "_" * len(word)
incorrect_guesses = []

print("Let's play hangman!")

while True:
    print()
    print(word_with_blanks)
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"You have {num_guesses} guesses left.")
    letter = input("Guess a letter: ").lower()

    if letter in word:
        print(f"Good guess! {letter} is in the word.")
        new_word_with_blanks = ""
        for (i, ch) in enumerate(word_with_blanks):
            if word[i] == letter:
                new_word_with_blanks += letter
            else:
                new_word_with_blanks += ch
        word_with_blanks = new_word_with_blanks
    else:
        if letter not in incorrect_guesses:
            incorrect_guesses.append(letter)
            num_guesses -= 1
            print(f"Sorry, {letter} is not in the word.")
        else:
            print(f"You already guessed {letter}. Try again.")


    if "_" not in word_with_blanks:
        print(f"Congratulations! You guessed the word: {word}")
        break
    if num_guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was: {word}")
        break
