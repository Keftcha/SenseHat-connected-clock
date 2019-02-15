#!/usr/bin/env python3

from sense_hat import SenseHat

from weather import Weather, Unit


def get_conditions(city):
    """Return the current weather condition of the city"""
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    return location.condition


def display_weather(city, instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the curent weather"""
    condition = get_conditions(city)
    instance.show_message(
        condition.text,
        text_color=fg_color,
        back_color=bg_color
    )


def display_temp(city, instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the curent temperature"""
    condition = get_conditions(city)
    instance.show_message(
        condition.temp,
        text_color=fg_color,
        back_color=bg_color
    )


if __name__ in "__main__":
    sense = SenseHat()
    while True:
        display_weather("saint-ay", sense)
        display_temp("saint-ay", sense)
