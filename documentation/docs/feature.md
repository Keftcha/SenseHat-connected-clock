# General features

The goal of this project is to give a little clock.
For that, there multiple files I write.

---

# Programs

Here is the list of programs that are in this project.

- [Clock](#clock "Clock program")  
    The main program of this project  
    **File:** `clock.py`
- [Binary clocks](#binary_clocks "Binary clocks program")  
    Clocks in binary mode  
    **Files:** `binary_clock_block.py` and `binary_clock.py`
- [Digital clock](#digital_clock "Digital clock program")  
    A digital clock  
    **File:** `digital_clock.py`
- [Menu config](#menu_config "Config program")  
    A menu to configure options  
    **File:** `menu_config.py`
- [Diaporama](#diaporama "Diaporama program")  
    Display a diaporama of images  
    **File:** `diaporama.py`

---

## Clock

The main program of the project.  
That program is a switcher for other programs.
With it, you have access to: 

- **Binary clocks**
- **Digital clock**
- **Menu config**
- **Temperature of the clock**
- **The date (with format: *dd/mm/yyyy* and *day_number month_short_name.*)**
- **The time (with format: *hh:mm*)**

---

## Binary clocks

Display a [binary clock](https://en.wikipedia.org/wiki/Binary_clock "Wikipedia - Binary clock").  
Two modes are available.

---

### Block mode

Dots are displayed on the matrix using 2 by 2 LED.  
This mode uses all the space of the LED matrix.

---

### Hyphen mode

Dots are displayed on the matrix using 1 LED for the height and 2 for the width.  
This mode only uses a part of the LED matrix.

---

## Digital clock

Display a digital clock.

The matrix LED is divided into four parts:

- Top Left (hours tens)
- Top Right (hours units)
- Bottom Left (minutes tens)
- Bottom Right (minutes units)

Hours are on the top and minutes on the bottom of the LED matrix

---

## Menu config

Configuration menu.

You can configure:

- The brightness
- The foreground color
- The background color
- The rotation angle
- The text scroll speed

The output is a json formatted string.

---

## Diaporama

Display a diaporama of pictures.

Pictures must have a size of 8 by 8 pixels and
be placed in the folder `./clock/pictures/` of the project.
