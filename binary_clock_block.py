#!/usr/bin/env python3

from sense_hat import SenseHat
from time import strftime, sleep

from package.utilities import display_pixels


def binary_time():
    """Get the time (hours and minutes) and we convert it in the same format
    but each chiffre is convert in binary"""
    hours = strftime("%H")
    minutes = strftime("%M")
    # Fromat numbers in binary with 4 digits
    time = [
        "{:04b}".format(int(hours[0])),
        "{:04b}".format(int(hours[1])),
        "{:04b}".format(int(minutes[0])),
        "{:04b}".format(int(minutes[1]))
    ]

    return time


def display(time, instance, on_color=[255, 255, 255], off_color=[0, 0, 0]):
    if len(time) != 4:
        raise ValueError("Your list must have a len of 4")

    pixels_state = [0] * 64

    for digit_place in range(4):    # Each number have 4 digits
        for idx, nb in enumerate(time):
            if nb[digit_place] == "1":
                line = digit_place * 2
                column = idx * 2

                pixels_state[line * 8 + column] = 1
                pixels_state[line * 8 + column + 1] = 1
                pixels_state[(line + 1) * 8 + column] = 1
                pixels_state[(line + 1) * 8 + column + 1] = 1

    display_pixels(pixels_state, instance, on_color, off_color)


def binary_clock_block(instance, fg_color, bg_color, sleep_time):
    display(binary_time(), instance, fg_color, bg_color)
    sleep(sleep_time)


if __name__ in "__main__":
    sense = SenseHat()
    sense.set_rotation(180)
    while True:
        binary_clock_block(sense, [255, 255, 255], [0, 0, 0])
