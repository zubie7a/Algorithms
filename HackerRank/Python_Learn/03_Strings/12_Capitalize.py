# https://www.hackerrank.com/challenges/capitalize
def capitalize(string):
    # Capitalize each word of a string.
    return " ".join(map(lambda x: x.capitalize(), string.split(" ")))
