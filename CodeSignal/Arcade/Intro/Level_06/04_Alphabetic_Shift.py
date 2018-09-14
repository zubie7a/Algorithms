# https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
def alphabeticShift(input_string):
    # Shift alphabetic characters in a string by one.
    # Define a function to shift a character.
    def shift(char):
        # Normalize the position of the character between 0 and 26.
        pos = ord(char) - ord('a')
        # Shift it by one.
        pos = (pos + 1) % 26
        # Convert it back to a character.
        return chr(pos + ord('a'))
    # Use the function in a `map` call to apply it to every character.
    return "".join(map(shift, input_string))
