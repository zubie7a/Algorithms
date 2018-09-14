# https://app.codesignal.com/arcade/intro/level-8/rRGGbTtwZe2mA8Wov
def firstDigit(input_string):
    # Return the firstmost digit occurring on a string.
    arr = list(filter(lambda x: x.isdigit(), input_string))
    return arr[0]
