#!/usr/bin/env python3

from sense_hat import SenseHat

from weather import Weather, Unit


def get_conditions(city):
    """Return the current weather condition of the city"""
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    return location.condition


def display_weather(city, instance):
    """Display the curent weather"""
    condition = get_conditions(city)
    instance.show_message(condition.text)


def display_temp(city, instance):
    """Display the curent temperature"""
    condition = get_conditions(city)
    instance.show_message(condition.temp)


if __name__ in "__main__":
    sense = SenseHat()
    while True:
        display_weather("saint-ay", sense)
        display_temp("saint-ay", sense)
