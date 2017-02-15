# https://codefights.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
def alphabeticShift(inputString):
    # Shift alphabetic characters in a string by one.
    def shift(char):
        pos = ord(char) - ord('a')
        pos = (pos + 1) % 26
        return chr(pos + ord('a'))
    return "".join(map(shift, inputString))
