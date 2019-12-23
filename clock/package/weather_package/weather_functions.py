#!/usr/bin/env python3

from sense_hat import SenseHat

from .weather_info import display_weather, display_temp


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
