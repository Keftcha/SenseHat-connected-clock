#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep
import os


def diaporama(instance, directory_path, time_sleep=3):
    """Display 8*8 pictures in the directory `directory_path`
    and wait `time_sleep` seconde between each"""
    pictures = os.listdir(directory_path)

    idx = 0
    while True:
        instance.clear()
        instance.load_image(directory_path + pictures[idx])
        sleep(time_sleep)
        idx += 1
        idx = idx % len(pictures)

        # Break if the joystick is touched
        if instance.stick.get_events():
            break


if __name__ in "__main__":
    sense = SenseHat()
    sense.set_rotation(180)

    diaporama(sense, "./pictures/", 1.5)
