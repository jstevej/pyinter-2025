---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 4
layout: cover
background: /lecture-01-cover.png
rev: "rev1 20240903"
---

# Lecture 4: Binary Numbers

---

# <BbHousekeeping/> Roadmap

- Review last class
  - Transistors
  - Digital logic
- Review bonus assignment
- Binary
- Exercise: Adder
- Computer Architecture
- Hexadecimal
- Binary Numbers in Python
- Homework Assignment

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

- Bonus assignment: rock, paper, scissors game
  - Using digital logic on https://logic.ly/demo
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

---
layout: bb-two-cols-header
clicks: 5
---

# <BbComputerScience/> Rock, Paper, Scissors Solution

::left::

<v-switch>
<template #1>
  <img src="/lecture-04-rps-table-1.png" class="bb-center-horizontally" style="width: 400px" />
</template>
<template #2-6>
  <img src="/lecture-04-rps-table-2.png" class="bb-center-horizontally" style="width: 400px" />
</template>
</v-switch>

<div v-click="[3, 6]">
$$
\begin{aligned}
W_A &= S_A \cdot P_B + P_A \cdot R_B + R_A \cdot S_B
\end{aligned}
$$
</div>

<div v-click="[4, 6]">
$$
\begin{aligned}
W_B &= S_B \cdot P_A + P_B \cdot R_A + R_B \cdot S_A
\end{aligned}
$$
</div>

::right::


<div v-click="[5, 6]">
<img src="/lecture-04-rps-solution.png" class="bb-center-horizontally" style="width: 400px" />
</div>

---

# <BbComputerScience/> Base-10 Numeral System

- 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- Each "place" is the next power of 10
- $123_{10} = 1 \times 10^{2} + 2 \times 10^{1} + 3 \times 10^{0}$

<br/>

<img src="/lecture-04-base-10-representation.png" class="bb-center-horizontally" style="width: 600px" />

---

# <BbComputerScience/> Base-2 (Binary) Numeral System

- 2 digits: 0, 1
- Each "place" is the next power of 2
- $101_{2} = 1 \times 2^{2} + 1 \times 10^{0} = 5_{10}$

<br/>

<img src="/lecture-04-base-2-representation.png" class="bb-center-horizontally" style="width: 500px" />

---

# <BbComputerScience/> Base-10 Addition, Example 1

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-10-addition-1.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #1>
<img src="/lecture-04-base-10-addition-1-solution.png" class="bb-center-horizontally" style="width: 200px" />
</template>
</v-switch>

---

# <BbComputerScience/> Base-10 Addition, Example 2

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-10-addition-2.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #1>
<img src="/lecture-04-base-10-addition-2-solution.png" class="bb-center-horizontally" style="width: 200px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 1

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-1.png" class="bb-center-horizontally" style="width: 100px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-1-solution.png" class="bb-center-horizontally" style="width: 100px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 2

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-2.png" class="bb-center-horizontally" style="width: 100px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-2-solution.png" class="bb-center-horizontally" style="width: 100px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 3

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-3.png" class="bb-center-horizontally" style="width: 100px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-3-solution.png" class="bb-center-horizontally" style="width: 100px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 4

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-4.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-4-solution.png" class="bb-center-horizontally" style="width: 340px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 5

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-5.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-5-solution.png" class="bb-center-horizontally" style="width: 350px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition, Example 6

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-base-2-addition-6.png" class="bb-center-horizontally" style="width: 260px" />
</template>
<template #1>
<img src="/lecture-04-base-2-addition-6-solution.png" class="bb-center-horizontally" style="width: 380px" />
</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition Truth Table

<br/>

<v-switch>
<template #0>
<img src="/lecture-04-addition-truth-table.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #1>
<img src="/lecture-04-addition-truth-table-solution.png" class="bb-center-horizontally" style="width: 200px" />
</template>
<template #2>
<img src="/lecture-04-addition-truth-table-solution.png" class="bb-center-horizontally" style="width: 200px" />

<br/>

$$
\begin{aligned}
S &= A \oplus B \\
C_{\mathrm{out}} &= A \cdot B
\end{aligned}
$$

</template>
</v-switch>

---

# <BbComputerScience/> Binary Addition with Carry Truth Table

<v-switch>
<template #0>
<img src="/lecture-04-addition-with-carry-truth-table.png" class="bb-center-horizontally" style="width: 220px" />
</template>
<template #1>
<img src="/lecture-04-addition-with-carry-truth-table-solution.png" class="bb-center-horizontally" style="width: 220px" />
</template>
<template #2>
<img src="/lecture-04-addition-with-carry-truth-table-solution.png" class="bb-center-horizontally" style="width: 220px" />

<br/>

$$
\begin{aligned}
S &= \overline{C_{\mathrm{in}}} \cdot (A \oplus B) + C_{\mathrm{in}} \cdot \overline{A \oplus B} \\
&= A \oplus B \oplus C \\
C_{\mathrm{out}} &= \overline{C_{\mathrm{in}}} \cdot \overline{A \cdot B} + C \cdot (A + B) \\
&= (A \oplus B) \cdot C_{\mathrm{in}} + A \cdot B
\end{aligned}
$$

</template>
</v-switch>

---

# <BbComputerScience/> One-Bit Adder

<br/>

<img src="/lecture-04-1-bit-adder.png" class="bb-center-horizontally" style="width: 300px" />

---

# <BbComputerScience/> Two-Bit Adder

<br/>

<img src="/lecture-04-2-bit-adder.png" class="bb-center-horizontally" style="width: 500px" />

---

# <BbComputerScience/> Three-Bit Adder

<br/>

<img src="/lecture-04-3-bit-adder.png" class="bb-center-horizontally" style="width: 600px" />

---

# <BbComputerScience/> Computer Architecture

<br/>

<img src="/lecture-04-computer-architecture.png" class="bb-center-horizontally" style="width: 400px" />


---

# <BbComputerScience/> Base-16 (Hexadecimal) Numeral System

- 16 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
- Each "place" is the next power of 16
- $1C_{16} = 1 \times 16^1 + 12 \times 16^0 = 28_{10}$

<br/>

<img src="/lecture-04-base-16-representation.png" class="bb-center-horizontally" style="width: 600px" />

---
layout: bb-two-cols-header
---

# <BbComputerScience/> ASCII Character Encoding

::left::

- Everything in computers is stored as bits
- How do we represent characters in bits?
- Create an encoding:
  - A dictionary that maps binary values to characters
  - Most common encodings:
    - ASCII (8-bit, 1 byte)
    - UTF-8 (multi-byte unicode)

::right::

<img src="/lecture-04-ascii-table.png" class="bb-center-horizontally" style="width: 600px" />

---

# <BbPython/> Binary Numbers in Python: Literals

```python
x = 5
y = 0b101 # integer literal in binary
print(f"x = {x}, y = {y}")
```

<br/>

#### Output

```
x = 5, y = 5
```

---
layout: bb-two-cols-header
---

# <BbPython/> Binary Numbers in Python: Formatting

::left::

<img src="/lecture-04-format-function-binary.png" class="bb-center-horizontally" style="width: 400px" />


::right::

```python
x = 5
x_base_2 = format(x, "08b")
print(f"x = {x}, x_base_2 = {x_base_2}")

# Can also use same syntax inside f-string
print(f"x = {x} (base 10) = {x:08b} (base 2)")
```

<br/>

#### Output

```
x = 5, y = 00000101
x = 5 (base 10) = 00000101 (base 2)
```

---

# <BbPython/> Character Encoding in Python

- `ord` converts a character to its integer value
- `chr` converts an integer to its character value

```python
ch1 = "a"
x = ord(ch) # ord stands for "ordinal"
print(f'ch1 = "{ch1}" = {x}')

y = 98
ch2 = chr(y)
print(f'ch2 = "{ch2}" = {y}')
```

<br/>

#### Output

```
ch1 = "a" = 97
ch2 = "b" = 98
```

- 97 corresponds to "a" in the ASCII table
- 98 corresponds to "b" in the ASCII table

---
layout: bb-two-cols-header
---

# <BbHousekeeping/> Homework

::left::

- Write a binary encoder and decoder
- Two separate programs
- Submit both on Jupiter Ed
- Hints
  - No fancy math needed; only things like `format`, `ord`, `chr`, etc.
  - Might also need other Python functions like `input` to prompt for message and string methods like `split`. Google for them if you forgot how to use them.
  - Write the encoder first so you can use its output to test your decoder.

::right::

<img src="/lecture-04-homework-encoder-output.png" class="bb-center-horizontally" style="width: 400px" />

<br/>

<img src="/lecture-04-homework-decoder-output.png" class="bb-center-horizontally" style="width: 400px" />