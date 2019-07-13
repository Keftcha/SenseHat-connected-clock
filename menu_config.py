#!/usr/env python3

def change_fg_color(colors, curent_color):
    None


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
    # Config function and arguments they need
    functions = {
        change_fg_color: (possibles_colors, fg_color)
        #change_bg_color: possibles_colors,
        #change_brightness: brightness_multiplicator,
        #change_rotate: rotate
    }

    # Value of parameters (must be in the same order of `functions`
    values = [
        fg_color,
        bg_color,
        brightness_multiplicator,
        rotate
    ]

    idx = 0

    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "middle":
                return (
                    fg_color,
                    bg_color,
                    rotate,
                    brightness_multiplicator
                )
            if event.direction == "right":
                idx += 1
            if event.direction == "left":
                idx -= 1

    idx = idx % len(functions)
    values[idx] = list(functions.keys())[idx](*list(functions.values())[idx])
