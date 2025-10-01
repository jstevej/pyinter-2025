---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 3
layout: cover
background: /lecture-01-cover.png
rev: "rev1 20240903"
---

# Lecture 3: Digital Logic

---

# <BbPython/> Homework Assignment: Evil Hangman

---

# <BbHousekeeping/> Roadmap

- Review homework assignment
- Transistors
- Digital logic
- In-class exercise
- Bonus assignment

---

# <BbComputerScience/> Transistors

- What is a transistor?

<v-click>

- Semiconductor device used to amplify or switch electrical signals
- Proposed in 1925
- First working device 1947
  - Nobel Prize (Physics) 1956
- Made from very pure silicon
- Can be used to make complex logic circuits

</v-click>

---

# <BbComputerScience/> Transistors in Computer Chips

<img src="/lecture-03-die.jpg" class="bb-center-horizontally" style="width: 400px" />

---

# <BbComputerScience/> Moore's Law

<img src="/lecture-03-moores-law.png" class="bb-center-horizontally" style="width: 600px" />

---

# <BbComputerScience/> Logic Gates

- Built from transistors acting as switches
- Implement Boolean logic
- Voltages indicate Boolean value
  - False: low logic level, usually 0 V
  - True: high logic level, usually 5 V, 3.3 V, 3 V, 1.8 V, 0.9 V
- Simulators:
  - https://logic.ly/demo
  - https://circuitverse.org/simulator

---

# <BbComputerScience/> NOT Gate


<img src="/lecture-03-not.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> AND Gate


<img src="/lecture-03-and.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> OR Gate


<img src="/lecture-03-or.png" class="bb-center-horizontally" style="width: 300px" />


---

# <BbComputerScience/> NAND Gate


<img src="/lecture-03-nand.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> NOR Gate


<img src="/lecture-03-nor.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> XOR Gate


<img src="/lecture-03-xor.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> XNOR Gate


<img src="/lecture-03-xnor.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> Exercise: 3-Way Vote

- Three toggle switches used for voting
- Light turns on if at least two switches are on
- Try it:
  - https://logic.ly/demo

---

# <BbComputerScience/> 3-Way Vote: Truth Tables

<img src="/lecture-03-vote-table.png" class="bb-center-horizontally" style="width: 300px" />

---
layout: bb-two-cols-header
---

# <BbComputerScience/> 3-Way Vote: Algebraic Notation

::left::

<img src="/lecture-03-vote-table.png" class="bb-center-horizontally" style="width: 300px" />

::right::

- NOT: $\overline{A}$
- AND: $A \cdot B$
- OR: $A + B$

<br/>

$$
\begin{aligned}
Q &= \overline{A} \cdot (B \cdot C) + A \cdot (B + C)
\end{aligned}
$$

---
layout: bb-two-cols-header
---

# <BbComputerScience/> 3-Way Vote: Solution

::left::

<img src="/lecture-03-vote-table.png" class="bb-center-horizontally" style="width: 300px" />

<br/>

$$
\begin{aligned}
Q &= \overline{A} \cdot (B \cdot C) + A \cdot (B + C)
\end{aligned}
$$

::right::

<img src="/lecture-03-vote-solution.png" class="bb-center-horizontally" style="width: 400px" />

---
layout: bb-two-cols-header
---

# <BbHousekeeping/> Bonus Assignment: Rock, Paper, Scissors

::left::

- Bonus assignment:
  - Optional, no late penalties, can only help your grade
- Build a rock, paper, scissors game
  - Two players
  - Three switches per player
  - Two lights
    - If player 1 wins: light 1 on, light 2 off
    - If player 2 wins: light 1 off, light 2 on
  - Tips
    - Make truth tables for light 1
    - Write algebraic expression for light 1
    - Light 2 should be easy to figure out once you get light 1

::right::

<img src="/lecture-03-rock-paper-scissors.png" class="bb-center-horizontally" style="width: 400px" />
