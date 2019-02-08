#!/usr/bin/env python3

from sense_hat import SenseHat
import time

from binary_clock import binary_clock as bin_clk
from weather_info import display_weather, display_temp

sense = SenseHat()
city = input("Enter a city name.\n")

# Colors values
colors = {
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "purple": [255, 0, 255],
        "white_blue": [0, 255, 255],
        "yellow": [255, 255, 0],
        "white": [255, 255, 255]
}


def temperature(instance):
    """Display on the instance of SenseHat() the current temperature (XX,X)"""
    instance.show_message(str(round(instance.get_temperature(), 1)))


def date(instance):
    """Display the date in the french format (dd/mm/yyyy)"""
    instance.show_message(time.strftime("%d/%m/%Y"))


def day(instance):
    """Display the day, the number of the day and the month (name_day,
    number_day, name_month)"""
    instance.show_message(time.strftime("%d %b."))


def hours(instance):
    """Display the hours (24 hours format) and the minutes (hh:mm)"""
    instance.show_message(time.strftime("%H:%M"))


# All the current functions are in this list
functions = [date, day, hours, temperature, bin_clk]

if city:
    """If a city is given we declare and add the functions which use the city
    for the weather."""
    def weather(instance):
        """Display the weather of the city which is given."""
        display_weather(city, instance)

    def outside_temp(instance):
        """Display the temperature of the city which is given."""
        display_temp(city, instance)

    functions += [weather, outside_temp]


idx = -1

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "right":
                idx += 1
            if event.direction == "left":
                idx -= 1

    functions[(idx + len(functions)) % len(functions)](sense)
