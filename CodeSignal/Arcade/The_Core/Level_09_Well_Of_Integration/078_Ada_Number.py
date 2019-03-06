# https://app.codesignal.com/arcade/code-arcade/well-of-integration/Ghe6HWhFft8h6fR49
import re

def adaNumber(line):
    # Create cumulatively the space for each base.
    full_space = "0123456789abcdef"

    # Underscores were used only for visual separating purposes.
    line = line.replace("_", "")
    # There can be upper/lower case characters so make uniform.
    line = line.lower()
    # Split the '#' if present.
    line = line.split("#")

    # If there's '#' present, it must follow the format 'base#number#',
    # this will split in 3 strings, [base, number, '']. If splits more
    # or less it's because there was only one '#' or more than two of them.
    if len(line) > 3 or len(line) == 2:
        return False
    # If there's only one element, there were no '#', so assume it is
    # base 10, and put it in the format as if it had been splitted.
    if len(line) == 1:
        line = ["10", line[0], ""]

    # Now we can safely assume the first element is the base.
    base = line[0]
    if base.isdigit():
        base = int(base)
        # Base has to be between 2 and 16, otherwise it's invalid.
        if base > 16 or base < 2:
            return False
    else:
        # Base has to be a number, otherwise it's invalid.
        return False

    # Match the number against the expected digit space for that base,
    # which effectively is every symbol until that base index.
    p = re.compile('^[{}]+$'.format(full_space[:base]))

    return p.match(line[1]) is not None
