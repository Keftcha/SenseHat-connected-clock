#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import argparse

from binary_clock import binary_clock as bin_clk
from weather_info import display_weather, display_temp
from digital_clock import digital_clock as dgt_clk

# Arguments which can be given
parser = argparse.ArgumentParser()
parser.add_argument(
    "-c", "--color",
    type=str,
    choices=("red", "green", "blue", "purple", "cyan", "yellow", "white", "black"),
    help="Color used for display, possibles values: red, green, blue, purple, cyan, yellow, white, black"
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

# If arguments aren't given, we give defaults values
args = parser.parse_args()
color = args.color if args.color else "white"
rotate = args.rotation if args.rotation else 0
brightness = args.brightness if args.brightness else 1
city = args.location if args.location else None

# Create our sense hat instance
sense = SenseHat()

# Colors values
colors = {
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "purple": [255, 0, 255],
        "cyan": [0, 255, 255],
        "yellow": [255, 255, 0],
        "white": [255, 255, 255],
        "black": [0, 0, 0]
}


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
    """If a city is given we declare and add the functions which use the city
    for the weather."""
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
color = [round(nb * brightness) for nb in colors[color]]
sense.set_rotation(rotate)


# Program loop
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "right":
                idx += 1
            if event.direction == "left":
                idx -= 1

    functions[idx % len(functions)](sense, color)
