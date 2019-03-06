# https://app.codesignal.com/arcade/code-arcade/well-of-integration/kvGfZZxGyjNbD7yxv
def integerToStringOfFixedWidth(number, width):
    # Given a number and a width, either crop it or expand it.
    # Expansion is adding 0s, cropping is removing left-to-right digits.
    str_num = str(number)
    # "0" times a negative value will return empty string.
    str_num = "0" * (width - len(str_num)) + str_num
    # If width is less than the length, will crop, if it's longer, a really huge
    # negative index will effectively start from 0 in the string.
    return str_num[-width:]
