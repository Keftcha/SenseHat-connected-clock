# Introduction

Here are the explaination on all programs.

- What arguments you can give when you execute theme
- How to use them

To execute a file, you must be in the folder `clock/` of the project and do
`./<file>` in a terminal.  
Replace `<file>` by the python file you want to execute in the `clock/` folder.

---

# Programs

- [Clock](#clock "Clock program")  
    **File:** `clock.py`
- [Binary clocks](#binary_clocks "Binary clocks program")  
    **Files:** `binary_clock_block.py` and `binary_clock.py`
- [Digital clock](#digital_clock "Digital clock program")  
    **File:** `digital_clock.py`
- [Menu config](#menu_config "Config program")  
    **File:** `menu_config.py`
- [Diaporama](#diaporama "Diaporama program")  
    **File:** `diaporama.py`

---

## Clock

### Colors

to do

### Arguments

To get help on the clock progam and see what arguments it take, call it with the
`-h` or `--help` argument as follow `./clock.py -h`.  

### Config

#### defaults
#### config file
#### arguments
#### interactive

---

## Binary clocks

The two binary clock both don't take any arguments.
They just display time in binary.  
The time is continously displayed.

Time are displaied as explained in the [feature section](feature.md#binary_clocks "Binary clocks feature").


### Block mode

The rotation is set to 0° (that mean the up is up and the down is down).

### Hyphen mode

The rotation is set to 180° (that mean the up is down and the down is up).

---

## Digital clock

The digital clock profram take no arguments. It just display time.  
The time is continously displayed.
The rotation is set to 0° (that mean the up is up and the down is down).

Time is displaied as explained in the [feature section](feature.md#digital_clock "Digital clock feature").

---

## Menu config

The menu config program is use to make the config.  
The rotation is set to 180° (that mean the up is down and the down is up).
The foreground color is set to blue while the background color is set to yellow.

When you execute the program you'll first can change the brightness.  
Pushing the joystick on the left you'll can change the text scroll speed
(lower is speediest, highest is slowest).  
Pushing the joystick on the left again you'll can change the rotation.  
Pushing the joystick on the left again you'll can change the background color.   
Pushing the joystick on the left again you'll can change the foreground color.   
Pushing the joystick one last time on the left you go back to the brightness settings.  

Pushing the joystick to the right will browse settings in the reverse order.

To change value of a settings, push the joystick up of down.  
For example, pushing down the joystick on the the brightness settings will
reduce it, while pushing it up will increase the brihtness.

**Changes take effect immediatly.**

> When you set the rotate, only the display rotate.  
> The joystick directions **don't** change.

When you have configured your settings as you like, press the joystick to quit
the program. It will print on screen you json configuration.  
You can copy it to the [config file](#config_file "Clock configuration file")
of the clock program.

---

## Diaporama

The diaporama program take no arguments. It just pass images.  
Images are displaied `1.5` secondes.
The rotation is set to 180° (that mean the up is down and the down is up).

You can add your custom images in the folder `clock/pictures/`. Images you add
should have a size of **8 by 8 pixels**.
