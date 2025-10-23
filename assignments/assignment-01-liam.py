import random
valid_letters = "abcdefghijklmnopqrstuvwxyz"
words = ["jump", "vampire", "milk", "coffee", "cane"]
num = random.randrange(len(words))
word = words[num]
num_guesses = 6
incorrect_guesses = ""
correct_guesses = ""
letters_guessed = []
game_win = False
for l in word:
    correct_guesses += "_ "
while num_guesses > 0:
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
else:
    print("you won.")


