#!/usr/bin/env python3

from sense_hat import SenseHat
from time import strftime


def numbers():
    # 1 => led on
    # 0 => led off

    zero = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    one = [
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ]

    two = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 0],
        [1, 1, 1, 1],
    ]

    three = [
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    four = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0]
    ]

    five = [
        [0, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    six = [
        [0, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 1]
    ]

    seven = [
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ]

    eight = [
        [0, 1, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 0]
    ]

    nine = [
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1]
    ]

    return [zero, one, two, three, four, five, six, seven, eight, nine]


def make_list():
    """With the hours number and the minutes number
    we return a list to be given to the set_pixels function"""

    hours = strftime("%H")
    hours = {
        "d": int(hours[0]),    # hours dizaines
        "u": int(hours[1])    # hours units
    }

    minutes = strftime("%M")
    minutes = {
        "d": int(minutes[0]),    # minutes dizaines
        "u": int(minutes[1])    # minutes units
    }

    nbrs = numbers()

    pixels = []

    for unit in (hours, minutes):
        for line_number in range(4): # because a number have a height of 4
            pixels.extend(nbrs[unit["d"]][line_number] + nbrs[unit["u"]][line_number])

    return pixels


def display(pixels_states, instance):
    """Given the states of each pixels (1 = on, 0 = off) in a list,
    we display the list on the led matrix"""

    instance.set_pixels([[255, 255, 255] if state else [0, 0, 0] for state in pixels_states])


def digital_clock(instance):
    display(make_list(), instance)



if __name__ in "__main__":
    sense = SenseHat()
    while True:
        digital_clock(sense)
