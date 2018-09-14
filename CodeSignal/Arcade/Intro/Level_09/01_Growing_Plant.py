# https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T
from math import ceil

def growingPlant(up_speed, down_speed, desired_height):
    # During day plant grows at up_speed, but in night it goes down
    # again by down_speed. How much days will it take to reach a
    # desired height starting from 0 height? If plant reaches height
    # during the day then it doesn't matter if it will go below the
    # desired height again during night, so we can't just get a
    # difference of growing and shrinking speed and measure after a
    # completed day. So first substract the measure of only a day's
    # growth, and then divide by the delta of day and night.
    delta = up_speed - down_speed
    # It will take at least one day.
    days = 1
    # The desired height will be reached during the day, never after
    # a whole cycle, so substract the day we are assuming has to pass.
    desired_height = desired_height - up_speed
    # Now for the remainder, divide by whole cycles.
    if desired_height > 0:
        days += ceil(desired_height / delta)

    return days
