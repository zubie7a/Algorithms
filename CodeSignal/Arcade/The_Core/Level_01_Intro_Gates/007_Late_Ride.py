# https://app.codesignal.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L
def lateRide(n):
    # Calculate the current time, assuming n minutes have passed and we started
    # counting at 00:00.
    hours = n//60
    minutes = n - (hours * 60)
    # Pad with 0s until reaching 2 total.
    timer = "{:02}:{:02}".format(hours, minutes)
    # Add the total of the digits in the timer.
    total = sum([int(digit) for digit in timer if digit.isdigit()])

    return total
