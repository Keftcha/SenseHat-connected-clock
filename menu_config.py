#!/usr/bin/env python3

from sense_hat import SenseHat
import json

from utilities import calculate_brightness, display_pixels

def change_fg_color(
    colors_name, colors, brightness,
    value, fg_color, bg_color, instance
):
    # Find the idx of our color
    clr = colors_name.index(fg_color)

    # Change the color
    new_color = colors_name[(clr + value) % len(colors_name)]

    # Get the brightness of the new color
    new_color_code = calculate_brightness(brightness, colors[new_color])
    bg_code = calculate_brightness(brightness, colors[bg_color])

    pixels_state = [
        1, 1, 1, 1, 0, 1, 1, 1,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 0,
        1, 1, 1, 0, 1, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 1, 1,
        1, 0, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 0, 1, 0, 0, 1,
        1, 0, 0, 0, 0, 1, 1, 0
    ]

    display_pixels(pixels_state, instance, new_color_code, bg_code)

    return new_color



def change_bg_color(colors):
    None


def change_brightness(current_multiplicator):
    None


def change_rotate(current_rotate):
    rotates = (0, 90, 180, 270)
    idx = rotates.index(current_rotate)

    # With joystich input, change the rotate


def menu_config(
    sense,
    possibles_colors,
    fg_color,
    bg_color,
    brightness_multiplicator,
    rotate
):
    # List of color name
    colors_name = list(possibles_colors.keys())

    # Config function and specific arguments they need
    functions = {
        change_fg_color: (
            colors_name,
            possibles_colors,
            brightness_multiplicator
        )
        #change_bg_color: possibles_colors,
        #change_brightness: brightness_multiplicator,
        #change_rotate: rotate
    }

    # Value of configured parameters must be in the same order of `functions`
    values = [
        fg_color,
        bg_color,
        brightness_multiplicator,
        rotate
    ]

    idx = 0

    while True:

        # The value is the changer parameter,
        # if he is positive, the function will encreate the changed parameter
        # if he us negative, the function will decrease the changed parameter
        # otherwise, if it's 0 nothing will happend
        value = 0

        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    return values
                if event.direction == "right":
                    idx += 1
                if event.direction == "left":
                    idx -= 1

                if event.direction == "up":
                    value = 1
                if event.direction == "down":
                    value = -1

        idx = idx % len(functions)
        values[idx] = list(functions.keys())[idx](
            *list(functions.values())[idx],
            value,
            values[0],    # fg_colog
            values[1],    # bg_color
            sense
        )

if __name__ in "__main__":
    sense = SenseHat()
    sense.set_rotation(180)

    with open("colors.json", "r") as colors:
        possibles_colors = json.load(colors)

    print(menu_config(
        sense,
        possibles_colors,
        "blue",
        "yellow",
        1,
        180
    ))
