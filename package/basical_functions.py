import time


# Some basical functions
def temperature(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display on the instance of SenseHat() the current temperature (XX,X)"""
    instance.show_message(
        str(round(instance.get_temperature(), 1)),
        text_colour=fg_color,
        back_colour=bg_color
    )


def date(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the date in the french format (dd/mm/yyyy)"""
    instance.show_message(
        time.strftime("%d/%m/%Y"),
        text_colour=fg_color,
        back_colour=bg_color
    )


def day(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the day, the number of the day and the month (name_day,
    number_day, name_month)"""
    instance.show_message(
        time.strftime("%d %b."),
        text_colour=fg_color,
        back_colour=bg_color
    )


def hours(instance, fg_color=[255, 255, 255], bg_color=[0, 0, 0]):
    """Display the hours (24 hours format) and the minutes (hh:mm)"""
    instance.show_message(
        time.strftime("%H:%M"),
        text_colour=fg_color,
        back_colour=bg_color
    )
