---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 2
layout: cover
background: /lecture-01-cover.png
rev: "rev1 20240903"
---

# Lecture 2: Debugging and Files

---

# <BbHousekeeping/> Roadmap

- Homework assignment
- How to level up as a programmer
- Debugging
- File I/O
- Homework Assignment

---

# <BbPython/> Homework Assignment: Hangman

<img src="/lecture-01-hangman.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbPython/> How to Level Up as a Programmer (1/4)

- [How to go from ok programmer to good programmer?](https://www.reddit.com/r/AskProgramming/comments/1nbzudg/how_to_go_from_ok_programmer_to_good_programmer/)

<br/>
<br/>

<v-click>

<img src="/lecture-02-reddit-01.png" class="bb-center-horizontally" style="width: 400px" />

</v-click>
---

# <BbPython/> How to Level Up as a Programmer (2/4)

- [How to go from ok programmer to good programmer?](https://www.reddit.com/r/AskProgramming/comments/1nbzudg/how_to_go_from_ok_programmer_to_good_programmer/)

<br/>
<br/>

<img src="/lecture-02-reddit-02.png" class="bb-center-horizontally" style="width: 400px" />

---

# <BbPython/> How to Level Up as a Programmer (3/4)

- [How to go from ok programmer to good programmer?](https://www.reddit.com/r/AskProgramming/comments/1nbzudg/how_to_go_from_ok_programmer_to_good_programmer/)

<br/>
<br/>

<img src="/lecture-02-reddit-05.png" class="bb-center-horizontally" style="width: 600px" />

---

# <BbPython/> How to Level Up as a Programmer (4/4)

- [How to go from ok programmer to good programmer?](https://www.reddit.com/r/AskProgramming/comments/1nbzudg/how_to_go_from_ok_programmer_to_good_programmer/)

<br/>
<br/>

<img src="/lecture-02-reddit-04.png" class="bb-center-horizontally" style="width: 600px" />

---
layout: bb-two-cols-header
---

# <BbDebugging/> Debugging

::left::

1. Understand the System
2. Make it fail
3. Quit thinking and look
4. Divide and conquer
5. Change one thing at a time
6. Keep an audit trail
7. Check the plug
8. Get a fresh view
9. If you didn't fix it, it ain't fixed

::right::

<img src="/lecture-02-debugging-book.png" class="bb-center-horizontally" style="width: 250px" />

[Debugging by David J. Agans](https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems-ebook/dp/B00PDDKQV2/)

---

# <BbPython/> Back to Hangman...

- What about more words?
- Let's read them from a file

---
layout: bb-two-cols-header
---

# <BbPython/> Reading Files

::left::

<img src="/lecture-02-file-open-syntax.png" class="bb-center-horizontally" style="width: 400px" />


<br/>
<br/>

#### Example

```python
file = open("file.txt", "r", encoding="utf-8")
# do stuff with file...
file.close()
```

::right::

- File name:
  - If no path, then file is in same directory from which you ran the program
  - Path can specify other location
- Mode:
  - `"r"`: open for reading
  - `"w"`: open for writing (erases existing content)
  - `"x"`: open for exclusive creation (fails if file already exists)
  - `"a"`: open for appending
  - `"b"`: binary mode
  - `"t"`: text mode
  - `"+"`: open for updating (reading and writing)

---
layout: bb-two-cols-header
---

# <BbPython/> File Paths

::left::

- Files are organized on your hard drive in *directories* (also called folders)
- Separated by `/` on Mac and Linux, `\` on Windows
- Mac and Linux example:
  - `/home/Users/steve/stuff/words.txt`
- Windows Example:
  - `C:\Users\Steve\stuff\words.txt`
  - Note: Windows also includes drive letter
- These are *absolute* paths
  - Specify exact location starting from system root
- Relative paths specify location relative to your current directory
  - `..` means go up one directory
  - Example: `../../other-files/words.txt`

::right::

<img src="/lecture-02-folders.png" class="bb-center-horizontally" style="width: 200px" />

---

# <BbPython/> `os.path` Module

- Lets us deal with paths, files, and directories in an OS-agnostic way

```python
from os import path

# results in:
#     ../stuff/words.txt on Mac/Linux
#     ..\stuff\words.txt on Windows

mypath = path.join('..', 'stuff', 'words.txt')

path.dirname(mypath) # returns ../stuff
path.exists(mypath) # returns True if the file exists

path.isdir(mypath)  # returns True if path is a directory
path.isfile(mypath)  # returns True if path is a file
```

- See documentation for `os.path` for more useful functions

---
layout: bb-two-cols-header
---

# <BbPython/> `with` Statement

::left::

```python
from os import path

words_path = path.join('stuff', 'words.txt')

with open(words_path, 'r', encoding="utf-8") as file:
    # do stuff with file
```

<br/>
<br/>

- Alternative to `open` and `close`
- Automatically opens and closes the file for us
- Prevents errors from forgetting to close the file
- Expresses intent

::right::

```python
from os import path

words_path = path.join('stuff', 'words.txt')

file = open(words_path, 'r', encoding="utf-8")
# do stuff with file
file.close()
```

---
layout: bb-two-cols-header
---

# <BbPython/> File Not Found Error

::left::

```python
from os import path

words_path = path.join('stuff', 'words.txt')

with open(words_path, 'r', encoding="utf-8") as file:
    # do stuff with file
```

::right::

<img src="/lecture-02-file-error.png" class="bb-center-horizontally" style="width: 400px" />

<br/>
<br/>

- You'll see this if:
  - Your filename doesn't match
  - Your path is wrong
  - Your file isn't in the directory
  - Your code is in a different directory

---
layout: bb-two-cols-header
---

# <BbBonus/> Shell Commands

::left::

- List files and directories
  - Linux / Mac: `ls`
  - Windows: `dir`
- Print working directory
  - Linux / Mac: `pwd`
  - Windows: `cd` (no arguments)
- Change directory
  - Linux / Mac: `cd foo`
  - Windows: `cd foo`

::right::

<img src="/lecture-02-shell-commands.png" class="bb-center-horizontally" style="width: 400px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Reading from the File

::left::

- `file.read()`
  - read the entire file as a string
- `file.readline()`
  - read the next line as a string
- `file.readlines()`
  - read the file as a list of strings
- `for line in file:`
  - iterate over each line in the file

<br/>

- line contains newline character(s) `\n`, or `\r\n`
- remove them with `string.strip()`

::right::

```python
from os import path

words_path = path.join("stuff", "words.txt")
words = []

with open(words_path, "r", encoding="utf-8") as file:
    for line in file:
          sline = line.strip()
          if len(sline) >= 4 and len(sline) <= 7:
              words.append(sline)
```

<br/>

- Now you can read words from a file for your hangman program
  - [10,000 most common english words](https://www.mit.edu/~ecprice/wordlist.10000)
  - [Scrabble word list](https://gist.github.com/deostroll/7693b6f3d48b44a89ee5f57bf750bd32)
  - [Large english words list](https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt)

---
layout: bb-two-cols-header
---

# <BbPython/> Improve Your Program

- Get words from file
- Handle invalid input
- Handle guessing a letter that was already guessed

---
layout: bb-two-cols-header
---

# <BbPython/> Homework 2: Evil Hangman

::left::

Evil Hangman is a computer program that cheats at the classic game of Hangman. Normally, the picks a single word and accurately represents it as the human player tries to guess all of the letters. In Evil Hangman, the computer instead maintains a large list words, then continuously pares down the word list to try to dodge the player's guesses.

::right::

- Start with your improved hangman program
- Read words from file
- Determine number of letters in starting words
- Pare down list of words by word length
- When the player makes a guess, pare down word list by removing words containing guessed letter
  - If there are words remaining after paring down, then tell the player their guess was incorrect and update your word list
  - If there aren't any words remaining after paring down, then choose a word at random from the list before paring down. Use this word to continue playing hangman normally