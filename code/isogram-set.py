while True:
    word = input("Enter a word: ")
    is_isogram = len(word) == len(set(word.lower()))
    if is_isogram:
        print(f"{word} is an isogram.")
    else:
        print(f"{word} is not an isogram.")
