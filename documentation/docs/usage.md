# Introduction

Here is the explanation of all programs.

- What arguments you can give when you execute them
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

The clock is the main program of the project.

### Colors

First, I'll explain you the `colors.json` file (located in the `clock/` folder).

This file is a json object. Keys are colors names and values are the RGB color
value as a list. The list contains three integers (between 0 and 255).

```json
{
   "color_name": [<red_value>, <green_value>, <blue_value>]
}
```

To see an example of what the `colors.json` should contain, you can look the
content of that file on GitHub.

This file is made for people who want to add their custom colors.

### Arguments

Here I'll explain all argument you can give to the clock program.

To get help on the clock program and see what arguments it take, call it with the
`-h` or `--help` argument as follow `./clock.py -h`.

- `-h` or `--help` → *Show the help.*
- `-fg` or `--foreground` with one of the color name which is in the
`colors.json` file → *Set the foreground color.*
- `-bg` or `--background` with one of the color name which is in the
`colors.json` file → *Set the background color.*
- `-r` or `--rotation` with the rotation angle (0, 90, 180, 270) → *Set the
    rotation of the LED matrix.*
- `-b` or `--brightness` with a float number between 0 and 1 → *Set the
    brightness, higher is brighter.*
- `-l` or `--location` with a string which is the name of the location you want
    the weather → *Set the location you want the weather.*
- `-i` or `--interactive` → *Launch the program in interactive mode.*
- `-s` or `--speed` with any int of float number higher than 0 → *Set the scoll
    speed and refresh rate, lower fastest.*

### Config

I'll now explain how configuration this program work and his default values.

The clock program has 4 configuration type:

- The [defaults](#defaults) configuration. This is the configuration used in
    last resort
- The [config file](#config_file). This configuration file is persistent.
- The [arguments](#arguments_1) given. This is configuration given when you start
    the program.
- The [interactive mode](#interactive). This mode asks you each value which can
    be confugured at the program start.

The priroty of configuration is like this:

|   Very Prior     |   Prior   | Less Prior  | Not Prior|
|:----------------:|:---------:|:-----------:|:--------:|
| Interactive mode | Arguments | Config file | Defaults |

#### defaults

Defaults values are used when:

- The `config.json` file is not found.
- No arguments are given.
- The interactive mode is not used.

Defaults values are:

| Parameter | Default value |
|-----------|---------------|
| foreground|     white     |
| background|     black     |
| rotation  |       0       |
| brightness|       1       |
| location  |     None      |
|   speed   |      0.1      |

#### config file

Values in the configuration file are used when:

- The file `config.json` is present.
- The value for a setting is valid.
- No arguments are given.
- The interactive mode is not used.

You can change the configuration in this file:

- By hand (not recommended).
- By using the [Menu config](#menu_config "Menu config program") program and
    copying the output in the `config.json` file.
- By accessing the **Menu config** feature while the clock is running (recommended).
    To know how to do that, see the [usage](#usage) section.

***Warning:***  
*Using the **Menu config** feature of clock program will overwrite the previous
config in the `config.json` file*.


#### arguments

Values in arguments are used when:

- The argument is present.
- The value of the argument is valid.
- The interactive mode is not used.

To know available arguments and their values, refer to the
[Arguments](#arguments) section.

Giving arguments will not overwrite the `config.json` file.

#### interactive

Values given in interactive mode are used when:

- The interactive mode is used.

Using the interactive mode will not overwrite the `config.json` file.

### Usage

When the clock is started (it may take a little time to display things on the
LED matrix) use the joystick to navigate.

| Joystick action |                    Action                    |
|-----------------|----------------------------------------------|
|  Pushing Right  | Switch to the next feature                   |
|  Pushing Left   | Switch to the previous feature               |
|  Pushing Up     | Nothing                                      |
|  Pushing Down   | Nothing                                      |
|  Pressing it    | Start the menu config (press agait to exit)  |

Each config work exactly the same as when they are started as the main program.  
To know how to use features, see below.

---

## Binary clocks

The two binary clocks both don't take any arguments.
They just display the time in binary.  
The time is continuously displayed.

Time is displaied as explained in the [feature section](feature.md#binary_clocks "Binary clocks feature").


### Block mode

The rotation is set to 0° (that mean the up is up and the down is down).

### Hyphen mode

The rotation is set to 180° (that mean the up is down and the down is up).

---

## Digital clock

The digital clock program take no arguments. It just displays the time.  
The time is continuously displayed.
The rotation is set to 0° (that mean the up is up and the down is down).

Time is displayed as explained in the [feature section](feature.md#digital_clock "Digital clock feature").

---

## Menu config

The menu config program is used to make the config.  
The rotation is set to 180° (that mean the up is down and the down is up).
The foreground color is set to blue while the background color is set to yellow.

When you execute the program you'll first can change the brightness.  
Pushing the joystick on the left you'll can change the text scroll speed
(lower is speediest, highest is slowest).  
Pushing the joystick on the left again, you'll can change the rotation.  
Pushing the joystick on the left again, you'll can change the background color.   
Pushing the joystick on the left again, you'll can change the foreground color.   
Pushing the joystick one last time on the left you go back to the brightness settings.  

Pushing the joystick to the right will browse settings in the reverse order.

To change value of a setting, push the joystick up or down.  
For example, pushing down the joystick on the brightness settings will
reduce it, while pushing it up will increase the brightness.

**Changes take effect immediately.**

> When you set the rotate, only the display rotates.  
> The joystick directions **don't** change.

When you have configured your settings as you like, press the joystick to quit
the program. It will print on screen you json configuration.  
You can copy it to the [config file](#config_file "Clock configuration file")
of the clock program.

---

## Diaporama

The diaporama program takes no arguments. It just pass images.  
Images are displayed `1.5` seconds.
The rotation is set to 180° (that mean the up is down and the down is up).

You can add your custom images in the folder `clock/pictures/`. Images you add
should have a size of **8 by 8 pixels**.
