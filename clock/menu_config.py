#!/usr/bin/env python3

from sense_hat import SenseHat
import json

from package.utilities import calculate_brightness, display_pixels
from package.numbers import numbers


def change_fg_color(
    colors_name,
    instance, value, brightness, fg_color, bg_color, colors, *_
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


def change_bg_color(
    colors_name,
    instance, value, brightness, fg_color, bg_color, colors, *_
):
    # Find the idx of our color
    clr = colors_name.index(bg_color)

    # Change the color
    new_color = colors_name[(clr + value) % len(colors_name)]

    # Get the brightness of the new color
    new_color_code = calculate_brightness(brightness, colors[new_color])
    fg_code = calculate_brightness(brightness, colors[fg_color])

    pixels_state = [
        1, 1, 1, 0, 0, 1, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 0,
        1, 0, 0, 1, 1, 0, 0, 0,
        1, 1, 1, 0, 1, 0, 0, 0,
        1, 0, 0, 1, 1, 0, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
        1, 1, 1, 0, 0, 1, 1, 0
    ]

    display_pixels(pixels_state, instance, fg_code, new_color_code)

    return new_color


def change_brightness(
    instance, value, current_multiplicator,
    fg_color, bg_color, colors, *_
):
    # Calculate the new brightness multiplicator
    new_bright_multi = round(current_multiplicator + (value / 10), 1)
    # The brightness multiplicator cant be lower than 0 or upper than 1
    new_bright_multi = min(new_bright_multi, 1)
    new_bright_multi = max(new_bright_multi, 0)

    # Racalculate the color code
    fg_code = calculate_brightness(new_bright_multi, colors[fg_color])
    bg_code = calculate_brightness(new_bright_multi, colors[bg_color])

    pixels_state = [
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 1, 1, 0, 0, 1,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        1, 0, 0, 1, 1, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0
    ]

    display_pixels(pixels_state, instance, fg_code, bg_code)

    return new_bright_multi


def change_rotate(
        instance, value, current_multiplicator,
        fg_color, bg_color, colors, current_rotate, _
):
    # With joystich input, change the rotate
    new_rotate = (current_rotate + value * 90) % 360

    # Racalculate the color code
    fg_code = calculate_brightness(current_multiplicator, colors[fg_color])
    bg_code = calculate_brightness(current_multiplicator, colors[bg_color])

    # Change the rotate on the sense hat
    instance.set_rotation(new_rotate)

    pixels_state = [
        0, 0, 0, 0, 0, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 0, 1, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0,
        1, 0, 1, 0, 0, 1, 1, 0,
        1, 0, 1, 0, 0, 1, 0, 1,
        1, 0, 1, 0, 0, 1, 1, 0,
        1, 1, 1, 0, 0, 1, 0, 0
    ]

    display_pixels(pixels_state, instance, fg_code, bg_code)

    return new_rotate


def change_scroll_speed(
    instance, value, brightness,
    fg_color, bg_color, colors, _, current_scroll_speed
):
    # The new speed
    new_speed = max(round(current_scroll_speed + value/10, 1), 0.0)
    speed = str(new_speed).split(".")

    nbrs = numbers()

    # The first four lines (the numbers)
    numbers_line = tuple(zip(nbrs[int(speed[0])], nbrs[int(speed[1])]))

    pixels_state = [0] * 32

    # Put the first four lines (numbers) in the pixel state
    for nb in numbers_line:
        for digit in nb:
            for pixel in digit:
                pixels_state.append(pixel)

    # Calculate the color code
    fg_code = calculate_brightness(brightness, colors[fg_color])
    bg_code = calculate_brightness(brightness, colors[bg_color])

    display_pixels(pixels_state, instance, fg_code, bg_code)

    return new_speed


def menu_config(
    sense,
    possibles_colors,
    fg_color,
    bg_color,
    brightness_multiplicator,
    rotate,
    scroll_speed
):
    # List of color name
    colors_name = list(possibles_colors.keys())

    # Config function and specific arguments they need
    functions = [
        {
            "func": change_brightness,
            "arguments": (
            )
        },
        {
            "func": change_fg_color,
            "arguments": (
                colors_name,
            ),
        },
        {
            "func": change_bg_color,
            "arguments": (
                colors_name,
            )
        },
        {
            "func": change_rotate,
            "arguments": (
            )
        },
        {
            "func": change_scroll_speed,
            "arguments": (
            )
        }
    ]

    # Value of configured parameters must be in the same order of `functions`
    values = [
        brightness_multiplicator,
        fg_color,
        bg_color,
        rotate,
        scroll_speed
    ]

    idx = 0

    while True:

        # The value is the changer parameter,
        # if he is positive, the function will encreate the changed parameter
        # if he us negative, the function will decrease the changed parameter
        # otherwise, if it's 0 nothing will happend
        value = 0

        # Get joystick events
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    return {
                        "brightness": values[0],
                        "foreground_color": values[1],
                        "background_color": values[2],
                        "rotation": values[3],
                        "scroll_speed": values[4]
                    }
                if event.direction == "right":
                    idx += 1
                if event.direction == "left":
                    idx -= 1

                if event.direction == "up":
                    value = 1
                if event.direction == "down":
                    value = -1

        idx = idx % len(functions)
        values[idx] = functions[idx]["func"](
            *functions[idx]["arguments"],
            sense,
            value,
            values[0],    # brightness_multiplicator
            values[1],    # fg_colog
            values[2],    # bg_color
            possibles_colors,    # colors name and their code
            values[3],    # curent rotate
            values[4]    # scroll speed or refresh rate
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
        180,
        0.1
    ))
