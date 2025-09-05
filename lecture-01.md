---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 1
layout: cover
background: /lecture-01-cover.png
rev: "rev1 20240903"
---

# Lecture 1: Introduction

---

# <BbHousekeeping/> Roadmap

- Introduction
- Housekeeping
- A note about AI
- What do we want to do this year?
- Warm-up problems
- Homework assignment

---

# <BbHousekeeping/> Introduction

```python
for person in each_of_us:
    person.tell_your_name_and_pronouns()
    person.tell_cool_projects_this_summer()
    person.tell_what_youre_excited_about_programming_this_year()
```

---

# <BbHousekeeping/> Meeting Times

- Lecture
  - In person: Thursday 10:00 am - 11:30 am
  - Attendance mandatory

---

# <BbHousekeeping/> Communication

- Message me on Jupiter Ed
- Or email me: steve.joiner@hybridgeacademy.org
- I'll help you over email or we can set up a Zoom call
- I'll usually respond quickly, but it may take an hour or more if I'm busy
- Late night messages -- may not respond until next morning

---

# <BbHousekeeping/> Lecture

- Review of previous assignment
- Presentation of new material
- Individual help with project
- Presentation of next homework assignment

---

# <BbHousekeeping/> Grades

- 85% Weekly homework assignments
- 15% Attendance and participation

<br/>

If we decide to do longer individual projects, then:

- 50% Weekly homework assignments
- 35% Individual project
- 15% Attendance and participation

---
layout: bb-two-cols-header
---

# <BbHousekeeping/> Use of AI and Online Resources

::left::


- Do not copy/paste code from the internet
- Do not copy/paste code from AI
- Copy/paste from any source is considered cheating

<br/>
<br/>
<br/>
<br/>
<img src="/lecture-01-vibe-coding.png" class="bb-center-horizontally" style="width: 300px" />

::right::

- AI is everywhere
- Can be very powerful and helpful
- But can be a hindrance to learning
- 1st Semester: don't use AI at all
- 2nd Semester: we'll learn how to use AI effectively

<br/>

- When using online resources:
  - Don't just copy solution -- understand it
  - Then write the code yourself
  - We're here to learn, not "make the code work"
- [Productive struggling](https://www.psychologytoday.com/us/blog/curiosity-code/202504/why-struggling-the-right-way-helps-you-learn) is [part of learning](https://pce.sandiego.edu/productive-struggle-in-the-classroom/)

---
layout: bb-two-cols-header
---

# <BbHousekeeping/> Syllabus

::left::

- Mix of structured units and projects
- Structured units
  - Error handling
  - Use of AI in programming
  - Object-oriented programming
  - Version control (`git`)
  - Computer Science topics
    - Searching, sorting
    - Linked lists
    - Path finding
    - Binary representation
    - Compression algorithms
  - Pygame review
  - Advanced Pygame

::right::

- Projects
  - Artificial life
  - Computer vision
  - Electronics
  - Robotics
  - Godot
  - Web dev

<br/>


What do *you* want to do?

----

# <BbPython/> Warm-up 1: Self-Referential Statement

- Write a program that prints the following:

```
This message contains ? characters.
```

- The `?` should be replaced by a value that makes the statement true.
- Your program should figure out the value for `?`.

---

# <BbPython/> Self-Referential Statement Solution

```python
for i in range(1000000):
    message = f"This message contains {i} characters."
    if len(message) == i:
        print(message)
```

---

# <BbPython/> Warm-up 2: Isograms

- Write a program that asks for a single word as input
- Then your program prints whether or not the word is an isogram
- An isogram is a word in which no letter occurs more than once

<br/>
<br/>
<img src="/lecture-01-isogram.png" class="bb-center-horizontally" style="width: 800px" />

---

# <BbPython/> Isograms: Solution

```python
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
```

---

# <BbPython/> Warm-up 3: Brackets

- Write a program that asks for a statement
- Then the program prints wether or not the brackets in the statement are matched
- Brackets include: `(`, `)`, `[`, `]`, `{`, `}`

<br/>
<br/>
<img src="/lecture-01-brackets.png" class="bb-center-horizontally" style="width: 800px" />

---

# <BbPython/> Brackets: Solution

```python
while True:
    statement = input("Enter a statement: ")
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    matched = True

    for ch in statement:
        if ch in brackets:
            stack.append(ch)
        elif ch in brackets.values():
            if len(stack) == 0 or brackets[stack.pop()] != ch:
                matched = False
                break

    if matched and len(stack) == 0:
        print("Brackets match")
    else:
        print("Brackets don't match")
```

---
layout: bb-two-cols-header
---

# <BbPython/> Homework Assignment 1: Hangman

::left::

- Write a program that plays hangman with you
- The program chooses a word
- The human guesses
- Create a short list of possible words (for now)
- Show:
  - Blanks and correct guesses
  - Incorrect guesses
  - Number of remaining guesses
  - Win/lose message
- Handle invalid input and repeat guesses
- Optional: display the hangman drawing

::right::

<img src="/lecture-01-hangman.png" class="bb-center-horizontally" style="width: 300px" />
