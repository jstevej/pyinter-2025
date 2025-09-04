while True:
    word = input("Enter a word: ")
    lcword = word.lower()

    letters = []

    for letter in lcword:
        if letter in letters:
            print(f"{word} is not an isogram.")
            break
        letters.append(letter)

    if (len(letters) == len(lcword)):
        print(f"{word} is an isogram.")
