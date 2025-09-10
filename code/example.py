import random

n = random.randint(0, 100) # generate a random number between 0 and 99

words = ["enchilada", "taco", "quesadilla"] # create a list of words
num_words = len(words) # get the number of items in a list
words.append("chimichanga") # add an item to the end of a list

name = input("What is your name? ") # ask the user for their name
name_length = len(name) # get the length of a string
print(f"Hello, {name}!") # print a formatted string

for letter in name: # loop through each character in a string
    print(letter)

if "x" in name: # test if a character or substring is in a string
    print("Your name has an x in it!")

name = name.lower() # convert a string to lowercase
name = name + "!!!" # concatenate strings

', '.join(words) # join a list of strings into a new string with separator





