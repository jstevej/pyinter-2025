import random
from os import path
# words_path = path.join("..", "words.txt")
words_path = path.join("assignments", "words.txt")
valid_letters = "abcdefghijklmnopqrstuvwxyz"
words = []
num_ltrs = random.randrange(3, 8)
with open(words_path, "r", encoding="utf-8") as file:
    for line in file:
        stline = line.strip()
        if len(stline) == num_ltrs:
            words.append(stline)
num_guesses = 12
incorrect_guesses = ""
correct_guesses = ""
letters_guessed = []
game_win = False
correct_guesses += "_ " * num_ltrs
while num_guesses > 0:
    while len(words) > 1:
        print(f"{correct_guesses}")
        print(f"incorrect guesses: {incorrect_guesses}")
        print(f"you have {num_guesses} left.")
        guess = input("guess a letter: ")
        rmvd_words = []
        if guess not in valid_letters:
            print("that's not a letter, try again.")
        elif guess in letters_guessed:
            print("you've already guessed that, try again")
        else:    
            for word in words:
                if len(words) > 1:
                    if guess in word:
                        rmvd_words.append(word)
                else:
                    continue
            for wd in rmvd_words:
                if len(words) > 1:
                    words.remove(wd)
            if len(words) < 1:
                print(f"{guess} is in the word")
                fnlword = word
                for i, ch in enumerate(fnlword):
                    if ch == guess:
                        cg = correct_guesses.split()
                        cg[i] = ch
                        correct_guesses = " ".join(cg)
            else:
                print(f"{guess} is not in the word")
                incorrect_guesses += guess
                num_guesses -= 1
        letters_guessed.append(guess)
        if num_guesses < 1:
            break
    in_guess = False
    print(f"{correct_guesses}")
    print(f"incorrect guesses: {incorrect_guesses}")
    print(f"you have {num_guesses} left.")
    guess = input("guess a letter: ")
    if guess not in valid_letters:
        print("that's not a letter, try again.")
        continue
    elif guess in letters_guessed:
        print("you've already guessed that, try again")
    else:
        for i, ch in enumerate(word):
            if ch == guess:
                cg = correct_guesses.split()
                cg[i] = ch
                correct_guesses = " ".join(cg)
                in_guess = True
        if in_guess == True:
            print(f"{guess} is in the word.")
        else:
            print(f"{guess} is not in the word.")
            num_guesses -= 1
            incorrect_guesses += guess
        letters_guessed.append(guess)
        cw = correct_guesses.split()
        if "_" in cw:
            game_win = False
        else:
            game_win = True
            break
if game_win == False:
    print("you lost.")
    print(f"word: {word}")
else:
    print("you won.")
    print(f"word: {word}")
