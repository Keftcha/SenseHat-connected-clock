#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import argparse
import json

from utilities import calculate_brightness
from binary_clock import binary_clock as bin_clk
from weather_info import display_weather, display_temp
from digital_clock import digital_clock as dgt_clk
from menu_config import menu_config

# Load colors possibilites
# Colors values are read in the ./colors file
with open("colors.json", "r") as colors:
    colors = json.loads(colors.read())

# Arguments which can be given
parser = argparse.ArgumentParser()
parser.add_argument(
    "-fg", "--foreground",
    type=str,
    choices=colors.keys(),
    help="Color used for display in foreground"
)
parser.add_argument(
    "-bg", "--background",
    type=str,
    choices=colors.keys(),
    help="Color used for display in background"
)
parser.add_argument(
    "-r", "--rotation",
    type=int,
    choices=(0, 90, 180, 270),
    help="Set the rotation, possibles values: 0, 90, 180, 270"
)
parser.add_argument(
    "-b", "--brightness",
    type=float,
    help="Set a brightness multiplicator, it must be between 0 and 1"
)
parser.add_argument(
    "-l", "--location",
    type=str,
    help="Give the location you want to get the weather"
)
parser.add_argument(
    "-i", "--interactive",
    help="Launch the program in interactive mode",
    action="store_true"
)

# Load the configuration
# Configuration values are read in the ./config.json file
# It arguments aren't in the config, we give defaults values
with open("config.json", "r") as config:
    config = json.loads(config.read())

    # Foreground color
    if (
        "foreground_color" in config and
        config["foreground_color"] in colors.keys()
    ):
        fg_color = config["foreground_color"]
    else:
        fg_color = "white"
    # Background color
    if (
        "background_color" in config and
        config["background_color"] in colors.keys()
    ):
        bg_color = config["background_color"]
    else:
        bg_color = "black"
    # Rotation
    if (
        "rotation" in config and
        config["rotation"] in (0, 90, 180, 270)
    ):
        rotate = int(config["rotation"])
    else:
        rotate = 0
    # Brightness
    if (
        "brightness" in config and
        config["brightness"] and 0 <= config["brightness"] <= 1
    ):
        brightness = float(config["brightness"])
    else:
        brightness = 1
    # City, fot the weather
    if "city" in config:
        city = config["city"] or None

# If arguments aren't given, we use the one in the config
args = parser.parse_args()
fg_color = args.foreground if args.foreground else fg_color
bg_color = args.background if args.background else bg_color
rotate = args.rotation if args.rotation else rotate
brightness = args.brightness if args.brightness else brightness
city = args.location if args.location else None


# Begin the interactive mode if needed
if args.interactive:
    fg_interactive = input("Choose a foreground color.\n\
Choices: {}\n\
Current: {}\n".format(list(colors.keys()), fg_color))
    bg_interactive = input("Choose a background color.\n\
Choices: {}\n\
Current: {}\n".format(list(colors.keys()), bg_color))
    rotate_interactive = input("Choose a rotation for the display\n\
Choices: 0, 90, 180, 270\n\
Current: {}\n".format(rotate))
    brightness_interactive = input("Choose the brightness intensity.\n\
0 is the lowest, 1 is the highest, choose a number between.\n\
Current: {}\n".format(brightness))
    city_interactive = input("Choose the city \
from where you want the weather\n\
Current: {}\n".format(city))

    # If nothing is given or arguments given are invalid
    # in the interactive mode, we use values given in parameters
    if fg_interactive in colors.keys():
        fg_color = fg_interactive
    if bg_interactive in colors.keys():
        bg_color = bg_interactive
    if rotate_interactive in ("0", "90", "180", "270"):
        rotate = int(rotate_interactive)
    if brightness_interactive and 0 <= float(brightness_interactive) <= 1:
        brightness = float(brightness_interactive)
    city = city_interactive or city

    # Display final parameters
    print("\n\
The foreground color is: {fg}\n\
The background color is: {bg}\n\
The rotation is set to: {rt}\n\
The brightness is set to: {brtns}\n\
The choosen city is: {city}\n\
    ".format(
        fg=fg_color, bg=bg_color, rt=rotate,
        brtns=brightness, city=city
    ))


# Create our sense hat instance
sense = SenseHat()


# Some basical functions
def temperature(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display on the instance of SenseHat() the current temperature (XX,X)"""
    instance.show_message(
        str(round(instance.get_temperature(), 1)),
        text_colour=fg_color,
        back_colour=bg_color
    )


def date(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the date in the french format (dd/mm/yyyy)"""
    instance.show_message(
        time.strftime("%d/%m/%Y"),
        text_colour=fg_color,
        back_colour=bg_color
    )


def day(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the day, the number of the day and the month (name_day,
    number_day, name_month)"""
    instance.show_message(
        time.strftime("%d %b."),
        text_colour=fg_color,
        back_colour=bg_color
    )


def hours(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the hours (24 hours format) and the minutes (hh:mm)"""
    instance.show_message(
        time.strftime("%H:%M"),
        text_colour=fg_color,
        back_colour=bg_color
    )


# All current functions are in this list
functions = [date, day, hours, temperature, bin_clk, dgt_clk]


# Weather functions
if city:
    # If a city is given we declare and add the functions which
    # use the city for the weather.
    def weather(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
        """Display the weather of the city which is given."""
        display_weather(
            city,
            instance,
            text_colour=fg_color,
            back_colour=bg_color
        )

    def outside_temp(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
        """Display the temperature of the city which is given."""
        display_temp(
            city,
            instance,
            text_colour=fg_color,
            back_colour=bg_color
        )

    functions += [weather, outside_temp]

# Initializing
idx = -1
# Code of the color as a list of three int between 0 and 255
fg_code = calculate_brightness(brightness, colors[fg_color])
bg_code = calculate_brightness(brightness, colors[bg_color])
sense.set_rotation(rotate)


# Program loop
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "right":
                idx += 1
            if event.direction == "left":
                idx -= 1
            if event.direction == "middle":
                new_configured_values = menu_config(
                    sense,
                    colors,
                    fg_color,
                    bg_color,
                    brightness,
                    rotate
                )

                # Write the new configuration in the ./config.json
                with open("config.json", "w") as config:
                    config.write(json.dumps(new_configured_values))

                brightness = new_configured_values["brightness"]
                fg_color = new_configured_values["foreground_color"]
                bg_color = new_configured_values["background_color"]
                rotate = new_configured_values["rotation"]

                # Re-set values after the config
                fg_code = calculate_brightness(brightness, colors[fg_color])
                bg_code = calculate_brightness(brightness, colors[bg_color])
                sense.set_rotation(rotate)

    functions[idx % len(functions)](sense, fg_code, bg_code)
