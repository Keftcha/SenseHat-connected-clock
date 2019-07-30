#!/usr/bin/env python3

from sense_hat import SenseHat
from time import strftime, sleep


def binary_time():
    """Get the time (hours and minutes) and we convert it in the same format
    but each chiffre is convert in binary"""
    hours = strftime("%H")
    minutes = strftime("%M")
    time = [hours[0], hours[1], minutes[0], minutes[1]]
    time = [str(bin(int(nb)))[2:] for nb in time]

    # We put the same number of digit as the maximum number can have
    time = [
        add_caracteres(time[0], "0", 2),    # hours dizaines
        add_caracteres(time[1], "0", 4),    # hours units
        add_caracteres(time[2], "0", 3),    # minutes dizaines
        add_caracteres(time[3], "0", 4),    # minutes units
    ]
    return time


def add_caracteres(string, caractere, len_elem):
    """Add the element "catactere" at the begin of a string named "string" for
    return a string which have "len_elem" caracteres"""
    if len(string) < len_elem:
        nb_elem = len_elem - len(string)
        supplement = caractere * nb_elem
        return supplement + string
    else:
        return string


def display(time, instance, on_color=[255, 255, 255], off_color=[0, 0, 0]):
    if len(time) != 4:
        raise ValueError("Your list must have a len of 4")

    display = [off_color for _ in range(8) for _ in range(8)]

    # We display each digit one by one
    column = 0
    for nb in time:
        nb = list(nb)
        nb.reverse()
        nb = "".join(nb)
        for line, elem in enumerate(nb):
            if elem == "1":
                # Each chiffre take two columns
                display[column + ((7 - line) * 8)] = on_color
                display[1 + column + ((7 - line) * 8)] = on_color
        column += 2

    instance.set_pixels(display)


def binary_clock(instance, fg_color, bg_color, sleep_time):
    display(binary_time(), instance, fg_color, bg_color)
    sleep(sleep_time)


if __name__ in "__main__":
    sense = SenseHat()
    while True:
        binary_clock(sense, [255, 255, 255], [0, 0, 0])
