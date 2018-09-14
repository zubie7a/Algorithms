# https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3
import re

def longestDigitsPrefix(input_string):
    # Given a string, output its longest prefix which contains only longestDigitsPrefix.
    total = ""
    for char in input_string:
        # For every character, try converting it to int. If it doesn't give an exception
        # then concatenate it to result, otherwise exit the loop.
        try:
            parsed = int(char)
            total += char
        except:
            break

    # Can also do it with regualr expresions. Match the string with a
    # regexp that will capture any number of digits at the start of it.
    # We can expect there to be always one match (even empty string).
    # If the string has any size, then its the digits that are prefix.
    for match in re.finditer(r'^[0-9]*', input_string):
        # if len(match.group(0)) > 0:
        #    return match.group(0)
        return match.group(0)
    # return ""
