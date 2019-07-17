def display_pixels(pixels_states, instance, fg=[255, 255, 255], bg=[0, 0, 0]):
    """Given the states of each pixels (1 = on, 0 = off) in a list,
    we display the list on the led matrix"""

    instance.set_pixels([fg if state else bg for state in pixels_states])


def calculate_brightness(brightness=1, color_code=[255, 255, 255]):
    """Given a color code (array of three int where 0 =< int =< 255),
    we put the brightness multiplicator on it"""
    return [round(nb * brightness) for nb in color_code]
