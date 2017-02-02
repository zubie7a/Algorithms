# https://www.hackerrank.com/challenges/python-mutations
def mutate_string(string, position, character):
    # Strings are immutable, so find out a way to modify a char.
    l = list(string)
    l[position] = character
    # return "".join(l)
    return string[:position] + character + string[position + 1:]
