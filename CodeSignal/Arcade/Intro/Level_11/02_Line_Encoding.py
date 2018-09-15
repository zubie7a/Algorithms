# https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR
from functools import reduce

def lineEncoding(s):
    # Keep track of what the previous character was.
    pre_char = s[0]
    # Keep accumulating the same character.
    acum_str = s[0]
    strings = []
    for i in range(1, len(s)):
        pos_char = s[i]
        # Once you find a different character...
        if pos_char != pre_char:
            # Change what the previous character was.
            pre_char = pos_char
            # Append the string built so far with equal characters.
            strings.append(acum_str)
            # Reinitialize the accumulated string to the current char.
            acum_str = pos_char
        else:
            # Keep accumulating the same character.
            acum_str += pos_char
    # One final append because reaching the end of the string will never
    # cause the accumulated to be pushed inside of the loop, unless we
    # inserted a final control character that we can make sure will never
    # occur inside of the original string.
    strings.append(acum_str)

    for i in range(len(strings)):
        string = strings[i]
        # In the encoding, the character will be accompanied by the amount
        # of times it occurrs, unless it was just once.
        num = str(len(string)) if len(string) > 1 else ""
        # Create the encoding with the number of occurrences and with the
        # single character representative of the whole string.
        encoded = "{}{}".format(num, string[0])
        strings[i] = encoded

    # Concatenate all the encoded strings.
    return reduce(lambda x, y: x + y, strings)
