---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 1
layout: cover
background: /pygame-cover.png
rev: "rev1 20241115"
---

# Lecture 5: Pygame Review and 2-D Lists

---

# <BbPython/> Virtual Environments

- Self-contained directory
- Isolates specific Python version
- Isolates Python packages (pygame, etc.)
- Doesn't pollute system-wide Python or packages
- Use different Python version per project
- Use different packages per project
- Use different package versions per project

---

# <BbComputer/> Install Python Environments Extension (Pre-Release)

<img src="/lecture-05-python-environments.png" class="bb-center-horizontally" style="width: 700px" />

---

# <BbComputer/> Enable Use Environments Extension

<img src="/lecture-05-use-environments-extension.png" class="bb-center-horizontally" style="width: 700px" />

---

# <BbComputer/> Create Virtual Environment

<img src="/lecture-05-create-virtual-environment.png" class="bb-center-horizontally" style="width: 700px" />

---

# <BbComputer/> Install Pygame in Your Virtual Environment

<img src="/lecture-05-install-pygame.png" class="bb-center-horizontally" style="width: 650px" />

- Prefer `pygame-ce` over `pygame`
    - Better performance, bug fixes
    - Docs: https://pyga.me/docs/

---
layout: bb-two-cols-header
clicks: 4
---

# <BbPython/> Hello, Pygame!

::left::

- `import pygame`
    - Imports the Pygame module
    - Call Pygame methods with `pygame` variable
- `pygame.init()`
    - Initializes Pygame
- `pygame.quit()`
    - Quits Pygame
- `print` still works
    - Useful for debugging
- Where's the screen?

::right::

<br/>
<br/>

```python
import pygame

pygame.init()
print("Hello, World!")
pygame.quit()
```

<div v-click="[1, 2]">
<Arrow x1="210" y1="115" x2="500" y2="168" color="rgb(92,144,76)" />
</div>
<div v-click="[2, 3]">
<Arrow x1="210" y1="213" x2="500" y2="206" color="rgb(92,144,76)" />
</div>
<div v-click="[3, 4]">
<Arrow x1="210" y1="275" x2="500" y2="244" color="rgb(92,144,76)" />
</div>

---
layout: bb-two-cols-header
---

# <BbPython/> Creating a Screen

::left::

- Remove `print("Hello, World!")`
- Call `pygame.display.set_mode`
    - Initializes our screen
    - Takes tuple argument
    - `(width, height)`
- Program ends right after our screen appears
- Let's fix that...

::right::

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.quit()
```

<div v-click="[1, 2]">
<Arrow x1="340" y1="148" x2="500" y2="170" color="rgb(92,144,76)" />
</div>

<br/>

<img src="/lecture-05-screen-dimensions.png" class="bb-center-horizontally" style="width: 420px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Run Until User Quits

::left::

- `while running`:
    - "Main loop"
    - All of our game code goes here
    - Loops until we set `running` to False
- `pygame.event.get()`
    - Gets *events* since last call
    - More on this next...
- `for event in events:`
    - "Event loop"
    - Handle *events*
    - Quit when `pygame.QUIT` event seen
        - User clicks "x" on window
- Try it!

::right::

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

<br/>
<br/>

<div v-click="4">

- But what are events? ...

</div>

<div v-click="[1, 2]">
<Arrow x1="225" y1="115" x2="500" y2="222" color="rgb(92,144,76)" />
</div>
<div v-click="[2, 3]">
<Arrow x1="260" y1="244" x2="530" y2="243" color="rgb(92,144,76)" />
</div>
<div v-click="[3, 4]">
<Arrow x1="280" y1="341" x2="530" y2="262" color="rgb(92,144,76)" />
</div>

---
layout: bb-two-cols-header
---

# <BbPython/> Pygame Events

::left::

- Occur when "things happen"
    - Press a key on the keyboard
    - Click a mouse button
    - Move the mouse
    - Click the "x" to close the window
    - Lots more...
- Events are "fired" or "emitted"
- Events have associated data
- Example: `pygame.KEYDOWN` data
    - `key`: value of key that was pressed
    - `mod`: state of keyboard modifiers
        - Shift, Ctrl, etc.

::right::

<img src="/lecture-05-event-examples.png" class="bb-center-horizontally" style="width: 420px" />

<br/>
<br/>

Pygame event documentation: https://www.pygame.org/docs/ref/event.html


---
layout: bb-two-cols-header
---

# <BbPython/> `pygame.KEYDOWN` Event

::left::

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("key pressed")
            print(f"    type(event.key): {type(event.key)}")
            print(f"    event.key: {event.key}")
            print(f"    type(event.mod): {type(event.mod)}")
            print(f"    event.mod: {event.mod}")

pygame.quit()
```

::right::


#### Output from pressing "q"

```
key pressed
    type(event.key): <class 'int'>
    event.key: 113
    type(event.mod): <class 'int'>
    event.mod: 0
```

<br/>

- How do we know 113 is "q"?
- Pygame has defined constants: https://www.pygame.org/docs/ref/key.html#key-constants-label 

---
layout: bb-two-cols-header
---

# <BbPython/> Handling `KEYDOWN` Events

::left::

<v-switch>

<template #0-5>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
```

</template>

<template #5-7>

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

pygame.quit()
```

</template>

</v-switch>

::right::


<br/>
<br/>
<br/>
<br/>
<br/>

<div v-click="1">

- Event loop
- If this is a key down event
    - Check `key` property of event
        - Quit when "q" key pressed
        - Quit when ESCAPE key pressed
    - Combine cases

</div>

<div v-click="[1, 2]">
<Arrow x1="500" y1="248" x2="250" y2="264" color="rgb(92,144,76)" />
</div>

<div v-click="[2, 3]">
<Arrow x1="500" y1="280" x2="370" y2="315" color="rgb(92,144,76)" />
</div>

<div v-click="[3, 4]">
<Arrow x1="545" y1="344" x2="295" y2="352" color="rgb(92,144,76)" />
</div>

<div v-click="[4, 5]">
<Arrow x1="545" y1="376" x2="295" y2="390" color="rgb(92,144,76)" />
</div>

<div v-click="[5, 6]">
<Arrow x1="535" y1="406" x2="300" y2="350" color="rgb(92,144,76)" />
</div>

---
layout: bb-two-cols
---

# <BbPython/> Time to Clean Up

- Clean up code as you go
- Move event handling to a function
- Main loop looks cleaner now
- Use class so no global variables

::right::

```python {*}{class:foo}
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.running = True

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    return False

        return True

    def run(self):
        while self.running:
            self.running = self.handle_events()

        pygame.quit()

game = Game()
game.run()
```

---
layout: bb-two-cols-header
---

# <BbHousekeeping/> Summary

::left::

- We'll always have an event loop
    - Sometimes simple:
        - Just process events to quit
    - Sometimes complex:
        - Process many keys
        - Process mouse events
        - Process screen resize events
        - Process custom events
- Use classes!

::right::

- Next up: drawing

---
layout: bb-two-cols-header
---

# <BbPython/> Drawing

::left::

- Goal: Draw a red rectangle
- What we need:
    - `pygame.draw.rect(surface, color, rect)`
    - `surface`: what to draw on (e.g., screen)
    - `color`: what color to draw
    - `rect`: rectangle shape and position

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

Pygame drawing documentation: https://www.pygame.org/docs/ref/draw.html

::right::

<img src="/lecture-05-simple-rectangle.png" class="bb-center-horizontally" style="width: 422px" />

<br/>

- Let's start with screen coordinates...

---
layout: bb-two-cols-header
---

# <BbPython/> Coordinates

::left::

- Need to tell Pygame where to draw things
- Specified by $x$ and $y$ screen coordinates
- Top left of screen is (0, 0)
- $x$ axis points to the right
- $y$ axis points down
- Common convention in computer graphics

::right::

<img src="/lecture-05-coordinates.png" class="bb-center-horizontally" style="width: 300px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Rectangles (Rects)

::left::

- Fundamental object in Pygame
    - Drawing surface sizes
    - Bounding boxes of sprites
- Usually specified as tuple
    - `(left, top, width, height)`
- Can also be specified as tuple of tuples
    - `((left, top), (width, height))`
    - Convenient when using points `(x, y)`

::right::

<img src="/lecture-05-rect-properties.png" class="bb-center-horizontally" style="width: 300px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Colors

::left::

- Color usually specified as RGB tuple
- RGB stands for red, green, and blue
- Each component is between 0-255 (int or float)
- Combine red, green, and blue to get any color

<br/>
<br/>

<img src="/lecture-05-rgb-colors.png" class="bb-center-horizontally" style="width: 200px" />

::right::

- <span style="color:rgb(255, 0, 0)">red: (255, 255, 0)</span>
- <span style="color:rgb(0, 255, 0)">green: (0, 255, 0)</span>
- <span style="color:rgb(0, 0, 255)">blue: (0, 0, 255)</span>
- <span style="color:rgb(0, 255, 255)">cyan: (0, 255, 255)</span>
- <span style="color:rgb(255, 0, 255)">magenta: (255, 0, 255)</span>
- <span style="color:rgb(255, 255, 0)">yellow: (255, 255, 0)</span>
- <span style="color:rgb(126, 30, 156)">purple: (126, 30, 156)</span>
- <span style="color:rgb(255, 129, 224)">pink: (255, 129, 224)</span>
- <span style="color:rgb(149, 208, 252)">light blue: (149, 208, 252)</span>
- <span style="color:rgb(101, 55, 0)">brown: (101, 55, 0)</span>
- <span style="color:rgb(146, 149, 145)">grey: (146, 149, 145)</span>
- <span style="color:rgb(255, 255, 255)">white: (255, 255, 255)</span>


---
layout: bb-two-cols-header
---

# <BbPython/> Color Transparency

::left::

- Color tuple can contain fourth value
- Alpha value (aka, transparency): 0-255
    - 0: completely transparent
    - 255: completely opaque
- Notice colors in illustration
    - All same shade of blue: (0, 0, 255)
    - Different transparencies

::right::

<img src="/lecture-05-alpha-transparency.png" class="bb-center-horizontally" style="width: 300px" />

---
layout: bb-two-cols
---

# <BbPython/> Drawing a Rectangle

```python
class Game:
    # ...

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0), (490, 240, 300, 200))
        pygame.display.flip()


    def run(self):
        while running:
            running = handle_events()
            self.draw()
```

::right::

<img src="/lecture-05-simple-rectangle-with-dimensions.png" class="bb-center-horizontally" style="width: 422px" />

<br/>

- Draw a rectangle
    - Drawing surface: `screen`
    - Color: `(255, 0, 0)`
    - Rect: `(490, 240, 300, 200)`
- What is `flip`?

---
layout: bb-two-cols
---

# <BbPython/> Double Buffering

- Ever make a flip-book?
- Rendering computer graphics is similar
- We draw to one *buffer*
- While showing the other
- Then we *flip* them
- In Pygame, we do it with `pygame.display.flip()`
- Remember to erase previous drawing


::right::

<Youtube id="p3q9MM__h-M" height="260" width="470" />

<br/>

```python
def draw(self):
    self.screen.fill((0, 0, 0)) # erase screen
    pygame.draw.rect(self.screen, (255, 0, 0), (490, 240, 300, 200))
    pygame.display.flip()
```

---
layout: bb-two-cols-header
---

# <BbPython/> Moving the Rectangle

::left::

```python
def __init__(self):
    # ...
    self.x = 490
    self.dx = 1

def draw(self):
    self.screen.fill((0, 0, 0)) # erase screen
    pygame.draw.rect(self.screen, (255, 0, 0), (self.x, 240, 300, 200))
    pygame.display.flip()

def update(self):
    self.x += self.dx 
    if self.x >= 980:
        self.dx = -1
    elif self.x <= 0:
        self.dx = 1

def run(self):
    while self.running:
        self.running = self.handle_events()
        self.update()
        self.draw()

    pygame.quit()
```

::right::

<img src="/lecture-05-simple-rectangle-moving.png" class="bb-center-horizontally" style="width: 422px" />

- `update` method
    - updates game state
- `draw` method
    - draws game state to screen
- Making these separate
    - Keeps code cleaner
    - Makes code easier to understand
    - "Separation of concerns"


---
layout: bb-two-cols-header
---

# <BbPython/> Smoother motion

::left::

```python
def __init__(self):
    # ...
    self.clock = pygame.time.Clock()
    self.dt = 0 # elapsed time between frames, in seconds

def run(self):
    self.dt = self.clock.tick(30) * 0.001 # get elapsed time in seconds
```

<br/>

- Use Pygame clock
    - Set target frame rate
    - Measure time between frames
    - Gives consistent performance across different devices

::right::

<img src="/lecture-05-simple-rectangle-moving.png" class="bb-center-horizontally" style="width: 422px" />

---
layout: bb-two-cols-header
---

# <BbPython/> 2-Dimensional Lists

::left::

- Also called "list of lists"
- Let's start by looking at 1-dimensional lists

<br/>

```python
list_0 = ['blue', 'red', 'yellow']
```


<v-click>

```python
print(list_0[0]) # blue
print(list_1[1]) # red
print(list_2[2]) # yellow
```

</v-click>

::right::

<v-click>

- We can imagine the list as a drawer with slots

<br/>

<img src="/lecture-05-2d-list-01.png" class="bb-center-horizontally" style="height: 185px"/>

</v-click>

---
layout: bb-two-cols-header
---

# <BbPython/> 2-Dimensional Lists, continued

::left::

```python
# three lists
list_0 = ['blue', 'red', 'yellow']
list_1 = ['orange', 'green', 'cyan']
list_2 = ['magenta', 'pink', 'black']
‎ 
‎ 
```

<v-click at="1">

<img src="/lecture-05-2d-list-02.png" class="bb-center-horizontally" style="height: 185px"/>

</v-click>

<v-switch>

<template #2>
```python
print(list_0[2])
print(list_1[1])
print(list_2[0])
```
</template>

<template #3>

```python
print(list_0[2]) # yellow
print(list_1[1])
print(list_2[0])
```

</template>

<template #4>

```python
print(list_0[2]) # yellow
print(list_1[1]) # green
print(list_2[0])
```

</template>

<template #5-12>

```python
print(list_0[2]) # yellow
print(list_1[1]) # green
print(list_2[0]) # magenta
```

</template>

</v-switch>

::right::

<v-click at="6">

```python
# one 2-dimensional list
list = [
    ['blue', 'red', 'yellow'],
    ['orange', 'green', 'cyan'],
    ['magenta', 'pink', 'black'],
]
```

</v-click>

<v-click at="7">

<img src="/lecture-05-2d-list-03.png" class="bb-center-horizontally" style="height: 185px"/>

</v-click>

<v-switch at="9">

<template #0>

```python
print(list[2][1])
print(list[0][2])
print(list[1][0])
```

</template>

<template #1>

```python
print(list[2][1]) # pink
print(list[0][2])
print(list[1][0])
```

</template>

<template #2>

```python
print(list[2][1]) # pink
print(list[0][2]) # yellow
print(list[1][0])
```

</template>

<template #3>

```python
print(list[2][1]) # pink
print(list[0][2]) # yellow
print(list[1][0]) # orange
```

</template>

</v-switch>

---
layout: bb-two-cols-header
---

# <BbPython/> 2-Dimensional Lists, continued

::left::

- Indices often referred to as row and column
- Sometimes referred to as y, x or x, y
- Common mistake to mix up your row and column
- (or x and y)

::right::

```python
# one 2-dimensional list
list = [
    ['blue', 'red', 'yellow'],
    ['orange', 'green', 'cyan'],
    ['magenta', 'pink', 'black'],
]
```

<br/>

<img src="/lecture-05-2d-list-03.png" class="bb-center-horizontally" style="height: 185px"/>

<br/>

```python
print(list[2][1]) # pink
print(list[0][2]) # yellow
print(list[1][0]) # orange
```

---

# <BbPython/> Use Cases for 2-Dimensional Lists

- Game boards
- Pixels in an image
- Grids of buttons (or anything)

<br/>

- Can treat as list of lists when convenient
    - Use list methods, e.g., `append`, `join`, etc.
- Can use row, column or x,y coordinates when convenient

---
layout: bb-two-cols-header
---

# <BbPython/> Homework

::left::

- Screen size: 1280 px x 720 px
- Create 2-D list of integers
  - 128 rows x 72 columns, initialize to all zeros
- In update function,
  - For each cell:
    - Set to random value between 0 and 3
- In draw function
  - For each cell:
    - If cell value is 0:
        - Don't do anything
    - Else:
        - Figure out rect coordinates for this cell
        - Draw rect
            - Colors: 1 = red, 2 = blue, 3 = green

::right::

<img src="/lecture-05-homework.png" class="bb-center-horizontally" style="height: 185px"/>