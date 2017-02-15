# https://codefights.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov
def firstDigit(inputString):
    # Return the firstmost digit occurring on a string.
    arr = list(filter(lambda x: x.isdigit(), inputString))
    return arr[0]
