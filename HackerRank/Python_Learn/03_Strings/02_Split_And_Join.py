# https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line):
    # Split a string by spaces, then join together with dashes.
    return "-".join(line.split(" "))
