def print_status(secret_word, misses):
    





min_length = 4
max_length = 12
words = []

# and read in the words from the file

file = open("../words_alpha.txt", "r")

for line in file:
    if min_length <= len(line.strip()) <= max_length:
        words.append(line.strip())

file.close()

# choose a word at random

import random

index = random.randint(0, len(words) - 1)
word = words[index]
secret_word = ["_"] * len(word)

# remove words that don't match the length of the chosen word

for i in range(len(words) - 1, -1, -1):
    if len(words[i]) != len(word):
        words.pop(i)
