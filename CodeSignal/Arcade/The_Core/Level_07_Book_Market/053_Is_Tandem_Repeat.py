# https://app.codesignal.com/arcade/code-arcade/book-market/2SDWWyHY9Xw5CpphY
def isTandemRepeat(input_string):
    # Check if a given string can be obtained by the concatenation
    # of some string to itself.
    mid = len(input_string)//2
    return input_string[:mid] == input_string[mid:]
