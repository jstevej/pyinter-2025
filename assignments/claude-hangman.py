import random

WORDS = [
    "python", "hangman", "programming", "keyboard", "monitor",
    "function", "variable", "algorithm", "database", "network",
    "elephant", "astronaut", "butterfly", "chocolate", "adventure",
    "symphony", "labyrinth", "mysterious", "telescope", "hurricane",
]

MAX_WRONG = 6

HANGMAN_STAGES = [
    # 0 wrong guesses
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # 1 wrong guess
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # 2 wrong guesses
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # 3 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # 4 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    # 5 wrong guesses
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    # 6 wrong guesses — dead
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]


def display_state(word, guessed_letters, wrong_letters):
    """Print the current game state."""
    print(HANGMAN_STAGES[len(wrong_letters)])

    # Word display: show guessed letters, hide the rest with underscores
    display = " ".join(ch if ch in guessed_letters else "_" for ch in word)
    print(f"  Word: {display}\n")

    if wrong_letters:
        print(f"  Wrong guesses ({len(wrong_letters)}/{MAX_WRONG}): {', '.join(sorted(wrong_letters))}")
    else:
        print(f"  Wrong guesses: none yet")

    remaining = MAX_WRONG - len(wrong_letters)
    print(f"  Remaining guesses: {remaining}\n")


def get_guess(guessed_letters):
    """Prompt the user for a valid, new single letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.\n")
        elif guess in guessed_letters:
            print(f"  ⚠  You already tried '{guess}'. Pick a different letter.\n")
        else:
            return guess


def play():
    word = random.choice(WORDS)
    guessed_letters = set()   # all letters tried so far
    wrong_letters = set()     # letters not in the word

    print("\n" + "=" * 40)
    print("        W E L C O M E  T O")
    print("          H A N G M A N")
    print("=" * 40)
    print(f"\n  I'm thinking of a {len(word)}-letter word.")
    print(f"  You have {MAX_WRONG} wrong guesses before it's over.\n")

    while True:
        display_state(word, guessed_letters, wrong_letters)

        # Check win
        if all(ch in guessed_letters for ch in word):
            print(f"  🎉  You won! The word was '{word}'. Well done!\n")
            break

        # Check loss
        if len(wrong_letters) >= MAX_WRONG:
            print(f"  💀  Game over! The word was '{word}'. Better luck next time!\n")
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"\n  ✔  '{guess}' is in the word!\n")
        else:
            wrong_letters.add(guess)
            print(f"\n  ✘  '{guess}' is not in the word.\n")


def main():
    while True:
        play()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye.\n")
            break


if __name__ == "__main__":
    main()