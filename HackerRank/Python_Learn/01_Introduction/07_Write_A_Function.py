# https://www.hackerrank.com/challenges/write-a-function
def is_leap(yr):
    leap = False
    # Leap year:
    #   * Divisible by 4
    #   * Not divisible by 100, unless divisible by 400 too.
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 100 == 0 and yr % 400 == 0):
        leap = True
    return leap
