#poor guy hope he dosen't get hung...
import random
wordlen=0
allottedguesses = 6
guesses = 0
wordempty = ""
words = ["jimmy", "timmy", "billy", "sarah", "phillip", "steve","sandwich","code","github","hello","world", "giovanni"]
random.seed()
index=random.randrange(0,len(words))
randword = words[(index)] 
for ch in randword:
    wordlen+=1
for ch in randword:
    wordempty += "_"
print(f"The word has {wordlen} characters")
print(wordempty)
def guesscode(guesses, randword, wordempty, allottedguesses):
    if guesses > allottedguesses:
        print("You have failed!")
        quit()
    else: 
        pass
    guess1 = input("What is your guess? If you mess up he gets the home depot rope... ")
    guess = guess1.lower()
    if guess in randword and guesses < allottedguesses:
        for x,ch in enumerate (randword):
            if ch == guess:
                wordempty = wordempty[:x] +guess + wordempty[x+1:]
                print("You guess was correct! he lives to see another letterrrrr.... ")
                print (wordempty)
                print(f"You have guessed {guesses}  time(s) out of six!")
                guess = None
                if "_" not in wordempty:
                    print("You got it! The man is in safe living conditions! (Legal Disclaimer)")
                guesscode(guesses, randword, wordempty,allottedguesses)
            else:
                guesses += 1
                print("The rope tightensss.... ")
                print(f"You have guessed {guesses}  time(s) out of six!")
                guess = None
                guesscode(guesses, randword, wordempty,allottedguesses)
guesscode(guesses, randword, wordempty,allottedguesses)
#if guess in guesslist then reguess and also cant guess not letters
