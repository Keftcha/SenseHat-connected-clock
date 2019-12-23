from time import strftime


# Some basical functions
def temperature(
    instance,
    fg_color=[255, 255, 255], bg_color=[0, 0, 0],
    scroll=0.1
):
    """Display on the instance of SenseHat() the current temperature (XX,X)"""
    instance.show_message(
        str(round(instance.get_temperature(), 1)),
        text_colour=fg_color,
        back_colour=bg_color,
        scroll_speed=scroll
    )


def date(
    instance,
    fg_color=[255, 255, 255], bg_color=[0, 0, 0],
    scroll=0.1
):
    """Display the date in the french format (dd/mm/yyyy)"""
    instance.show_message(
        strftime("%d/%m/%Y"),
        text_colour=fg_color,
        back_colour=bg_color,
        scroll_speed=scroll
    )


def day(
    instance,
    fg_color=[255, 255, 255], bg_color=[0, 0, 0],
    scroll=0.1
):
    """Display the day, the number of the day and the month (name_day,
    number_day, name_month)"""
    instance.show_message(
        strftime("%d %b."),
        text_colour=fg_color,
        back_colour=bg_color,
        scroll_speed=scroll
    )


def hours(
    instance,
    fg_color=[255, 255, 255], bg_color=[0, 0, 0],
    scroll=0.1
):
    """Display the hours (24 hours format) and the minutes (hh:mm)"""
    instance.show_message(
        strftime("%H:%M"),
        text_colour=fg_color,
        back_colour=bg_color,
        scroll_speed=scroll
    )
