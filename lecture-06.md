---
theme: seriph
highlighter: shiki
transition: slide-left
title: Lecture 1
layout: cover
background: /lecture-06-cover.jpg
rev: "rev1 20241115"
---

# Lecture 6: Tiny:Bit

---

# <BbApplications/> What is a Microcontroller

- Small, low-cost computer processor
- Low power
- Used in "embedded" applications
    - Appliances
    - Smart home devices
    - Computer peripherals
    - Cars
    - Consumer electronics
    - Medical equipment
    - Just about everywhere
- Easy to interface with sensors, displays, etc.

---

# <BbApplications/> Microcontroller vs Microprocessor

<div></div>

|      | Microprocessor | Microcontroller |
| ---- |:-------------- |:--------------- |
| Clock Speed | ~2 GHz | 1-200 MHz |
| Number of Cores | 4-32 | 1 |
| Memory | 2-256 GB (external) | 16-512 kB (internal) |
| Storage | 256-2,000 GB | 500-2,000 kB |
| Power Usage | high to moderate | low to very low |
| Cost  | high to moderate | low to very low |
| Peripheral Support | Complex, high bandwidth | Simple, low bandwidth |

---
layout: bb-two-cols-header
---

# <BbPersonalProjects/> Micro:Bit

::left::

- Open-source single board computer (SBC)
- Designed by the BBC for computer education
- Has lots of cool peripherals
    - LED grid
    - Light level sensor
    - Buttons
    - Microphone
    - Speaker
    - Accelerometer (gestures, acceleration)
    - Compass
    - Bluetooth
    - USB
    - Battery connector
- Runs MicroPython!

::right::

<img src="/lecture-06-microbit.png" class="bb-center-horizontally" style="height: 400px;" />

---
layout: bb-two-cols-header
---

# <BbPersonalProjects/> Micro:Bit Editor

::left::

- https://python.microbit.org/v/3
- Use documentation on Micro:Bit site
- Don't use online editor
    - Not aware of Tiny:Bit hardware
    - Will remove our Tiny:Bit firmware

::right::

<img src="/lecture-06-microbit-editor.png" class="bb-center-horizontally" style="height: 260px;" />


---
layout: bb-two-cols-header
---

# <BbPython/> MicroPython

::left::

- A subset of Python
- Designed to run on microcontrollers
- Processor, memory, and storage constraints
- Everything we've learned so far works
- Except f-strings

::right::

```python
# no f-strings in micropython
print(f"{name} has {hp} hit points")

# use string.format instead
print("{} has {} hit points".format(name, hp))

# or just use + to concatenate strings
# remember to use str() to convert non-strings
print(name + " has " + str(hp) + " hit points")
```

---
layout: bb-two-cols-header
---

# <BbPersonalProjects/> Tiny:Bit

::left::

- Motors
- RGB headlights
- RGB taillights
- Ultrasonic distance sensor
- IR receiver and remote
- Line tracking sensors
- Rechargeable battery
- Plus everything on the Micro:Bit!

::right::

<img src="/lecture-06-tiny-bit.png" class="bb-center-horizontally" style="width: 400px" />

---
layout: bb-two-cols
---

# <BbPersonalProjects/> Tiny:Bit Power

- Use charging port to charge
    - Power switch must be off
- Use Micro:Bit port for programming
    - Be careful unplugging: can brick Micro:Bit
    - *Save before programming!*
    - Your program must be called `main.py`
    - Wait 10 seconds before programming after plugging in
    - Can program with power on or off
    - Some things work poorly if power off

::right::

<img src="/lecture-06-tiny-bit-power.png" class="bb-center-horizontally" style="width: 380px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Setting Up Visual Studio Code

- Confirm all our Python extensions are installed
- Install Serial Monitor extension from Microsoft
- Create new project
- Download my `tinybit.zip` file
- Unzip it in your project directory
- Create virtual environment
- Install `microfs2` package in virtual environment
- Flash Micro:Bit with Tiny:Bit firmware
- Put `hybridge_tinybit.py` on Micro:bit
- Create simple `main.py` program
- Put `main.py` on Micro:Bit
- Celebrate! 🥳

---

# <BbPython/> Confirm All our Python Extensions are Installed

<br/>

<img src="/lecture-06-python-extensions.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Install Serial Monitor from Microsoft

<br/>

<img src="/lecture-06-serial-monitor-extension.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Create new Project

<br/>

<img src="/lecture-06-create-new-project.png" class="bb-center-horizontally" style="height: 400px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Download My `tinybit.zip` File

- [tinybit.zip](https://www.dropbox.com/scl/fi/9cy1castdbe3mxdv396nb/tinybit.zip?rlkey=ow7tdw6icrw3dvws3p9jgk745&dl=0)


<br/>

::left::

<img src="/lecture-06-tinybit-download-1.png" class="bb-center-horizontally" style="height: 250px" />

::right::

<img src="/lecture-06-tinybit-download-2.png" class="bb-center-horizontally" style="height: 250px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Copy `tinybit.zip` to Your Project Folder

<br/>

::left::

<img src="/lecture-06-tinybit-copy-1.png" class="bb-center-horizontally" style="height: 370px" />

::right::

<img src="/lecture-06-tinybit-paste-1.png" class="bb-center-horizontally" style="height: 320px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Extract `tinybit.zip` File in Your Project Folder

<br/>

::left::

<img src="/lecture-06-tinybit-extract-1.png" class="bb-center-horizontally" style="height: 360px" />

::right::

<img src="/lecture-06-tinybit-extract-folder-1.png" class="bb-center-horizontally" style="height: 210px" />
<img src="/lecture-06-tinybit-extract-folder-2.png" class="bb-center-horizontally" style="height: 210px" />


---

# <BbPython/> Delete `tinybit.zip` File in Your Project Folder

<br/>

<img src="/lecture-06-tinybit-delete-1.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Confirm Pylance is Enabled

<br/>

<img src="/lecture-06-pylance-settings.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Disable `reportMissingModuleSource`

<br/>

<img src="/lecture-06-report-missing-module-source.png" class="bb-center-horizontally" style="height: 420px" />

---

# <BbPython/> Create Virtual Environment

<br/>

<img src="/lecture-06-create-virtual-environment.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Activate Virtual Environment in PowerShell

<br/>

<img src="/lecture-06-activate-virtual-environment.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Activate Virtual Environment Error

<br/>

If you see this:

<img src="/lecture-06-activate-error.png" class="bb-center-horizontally" style="width: 800px" />

Then do this:

<img src="/lecture-06-activate-fix.png" class="bb-center-horizontally" style="width: 800px" />

And try again:

<img src="/lecture-06-activate-retry.png" class="bb-center-horizontally" style="width: 800px" />

---

# <BbPython/> Automatically Activate Virtual Environment

<br/>

<img src="/lecture-06-auto-activate-virtual-environment.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Install `microfs2` Package in Virtual Environment

<br/>

<img src="/lecture-06-install-microfs2.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Flash Micro:Bit with Tiny:Bit Firmware

<br/>

<img src="/lecture-06-microbit-flash.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Put `hybridge_tinybit.py` on Micro:Bit

<br/>

<img src="/lecture-06-put-hybridge-tinybit-py.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Create Simple `main.py` Program

<br/>

<img src="/lecture-06-first-main-py.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Put `main.py` on Micro:Bit

<br/>

<img src="/lecture-06-put-main-py.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Yay!

<br/>

<img src="/lecture-06-all-done.jpg" class="bb-center-horizontally" style="height: 400px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Normal Development Flow

::left::

1. Modify `main.py`
2. *Save* `main.py`
3. If you need to plug in Micro:Bit USB programming port, wait 10 seconds afterwards
4. In your venv: `ufs put main.py`

::right::

<img src="/lecture-06-development-flow.png" class="bb-center-horizontally" style="height: 270px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Debugging

::left::

- Option 1:
    - Micro:Bit display
    - Tiny:Bit LEDs
- Option 2:
    - Use `print`
    - View with the Serial Monitor extension
    - Have to keep USB cable attached

::right::

<img src="/lecture-06-serial-monitor-debugging.png" class="bb-center-horizontally" style="height: 340px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Common Problems

::left::

- Did you forget to save your `main.py`?
- Is your serial monitor connected?
    - Can't `ufs put main.py` while connected
- Are you in your virtual environment?
    - You should see `(.venv)` left of your prompt
    - If not, `.venv\Scripts\Activate.ps1`
- Is the Tiny:Bit power switch on?
- Is your battery charged?
- Did you brick your Micro:Bit?

::right::

<img src="/lecture-06-development-flow.png" class="bb-center-horizontally" style="height: 270px" />

---
layout: bb-two-cols-header
---

# <BbPersonalProjects/> If You Brick Your Micro:Bit

::left::

1. Turn off Tiny:Bit power switch
3. Unplug Micro:Bit and wait 10 seconds
3. Plug USB into Micro:Bit programming port and wait 10 seconds
4. Copy `Tinybit-micropythonV2.hex` to Micro:Bit USB Drive
5. In your venv: `ufs put hybridge_tinybit.py`
6. In your venv: `ufs put main.py`
7. It should work now

::right::

<br/>
<br/>
<img src="/lecture-06-brick.png" class="bb-center-horizontally" style="height: 250px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Tiny:Bit Lights

::left::

```python
import hybridge_tinybit as tinybit

color_white_full = (255, 255, 255)
color_white_half = (128, 128, 128)
color_white_quarter = (64, 64, 64)
red = (64, 0, 0)
green = (0, 64, 0)
blue = (0, 0, 64)

tinybit.set_headlights(color_white_quarter)

tinybit.set_taillight_left(blue)
tinybit.set_taillight_right(green)

tinybit.set_taillights(blue, green)
```

<br/>

- Colors set with RGB values (0-255) as tuple or list
- Brighter drains battery faster
- I like 64

::right::

<img src="/lecture-06-tiny-bit-lights.png" class="bb-center-horizontally" style="height: 400px" />

---
layout: bb-two-cols
---

# <BbPython/> Tiny:Bit IR Remote

```python
import hybridge_tinybit as tinybit

ir_code = tinybit.get_ir_code()

if ir_code == tinybit.IR_LEFT:
    tinybit.set_motors_spin_left(50)
elif ir_code == tinybit.IR_LIGHT:
    tinybit.set_headlights((64, 64, 64))
elif ir_code != tinybit.IR_NO_SIGNAL:
    print("unhandled code {}".format(ir_code))
```

<br/>

- Best reception from the front
- But kinda works from the back too
- The Micro:Bit's music interferes with the IR signal
    - Short sound effects are fine
    - Long songs cause problems
        - Codes get missed
        - Incorrect codes reported

::right::

<img src="/lecture-06-tiny-bit-ir-codes.png" class="bb-center-horizontally" style="height: 490px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Tiny:Bit Motors

::left::

```python
import hybridge_tinybit as tinybit

# go forward with speed 50 (0-255)
tinybit.set_motors_forward(50)

# go backward with speed 50 (0-255)
tinybit.set_motors_backward(50)

# spin left with speed 50 (0-255)
tinybit.set_motors_spin_left(50)

# spin right with speed 50 (0-255)
tinybit.set_motors_spin_right(50)

# stop motors
tinybit.set_motors_stop()
```

- 50 is a good speed for hard floors
- Will go slower as battery runs down
- Best battery life on hard floors
- Battery will wear down much faster on carpet

::right::

<img src="/lecture-06-tiny-bit-motors.png" class="bb-center-horizontally" style="height: 400px" />

---
layout: bb-two-cols
---

# <BbPython/> Tiny:Bit Motor Trim (Optional)

```python
import hybridge_tinybit as tinybit

tinybit.set_motors_trim(3)
tinybit.set_motors_forward(50)
tinybit.set_motors_spin_left(50)
```

- Tiny:Bit can pull to one side
- Due to electrical and mechanical differences
- Can compensate with trim
- Positive: increase speed of left motor
- Negative: increase speed of right motor
- Set it once at top of `main.py`
- Gets applied to all other motor functions
- Drift will change as battery wears down
- Drift will changes as motors wear in

::right::

<img src="/lecture-06-tiny-bit-motor-trim-2.png" class="bb-center-horizontally" style="height: 500px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Tiny:Bit Line Sensors

::left::

```python
import hybridge_tinybit as tinybit

red = (64, 0, 0)

if tinybit.has_left_track():
    tinybit.set_taillight_left(red)
elif tinybit.has_right_track():
    tinybit.set_taillight_right(red)
```

<br/>

- IR emitter/detectors
- Detect black/white
    - `True` if black
    - `False` if white
- We will use for line following

::right::

<img src="/lecture-06-tiny-bit-line-sensors.png" class="bb-center-horizontally" style="height: 400px" />

---
layout: bb-two-cols-header
---

# <BbPython/> Tiny:Bit Ultrasonic Distance Sensor

::left::

```python
import hybridge_tinybit as tinybit

dist = tinybit.get_sonar_distance()
```

<br/>

- Returns distance (in cm)
- Best results in 10 cm - 250 cm range
- Can give erroneous results outside that range
- Blind spot around 3 cm
- ~40° field of view

::right::

<img src="/lecture-06-tiny-bit-distance-sensor.png" class="bb-center-horizontally" style="height: 400px" />

---

# <BbPython/> Sample Program

<img src="/lecture-06-sample-program.png" class="bb-center-horizontally" style="height: 450px" />

---
layout: bb-two-cols-header
---

# <BbPersonalProjects/> Homework

::left::

- Control the Tiny:Bit with the IR remote
- Must at least:
    - Do things when IR remote buttons are pressed
    - Do something with the headlights
    - Do something with the taillights
    - Do something with the motors
    - Do something with the Micro:Bit display
- Have fun!
- Bring it next time to demo

::right::

- Optional ideas:
    - Play sounds with the Micro:Bit
    - Use Micro:Bit buttons
    - Detect tilt with Micro:Bit
    - Detect gestures with Micro:Bit
    - Detect light levels with Micro:Bit
    - Detect distance with Tiny:Bit ultrasonic sensor



