# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
import math

def addBorder(picture):
    '''
    picture = ["abc",
               "ded"]
               
    addBorder(picture) = ["*****",
                          "*abc*",
                          "*ded*",
                          "*****"]
    '''
    # The borders add a margin of thickness 1 so total 2 extra units.
    rows, cols = len(picture) + 2, len(picture[0]) + 2
    # Put two empty lines at top and bottom of picture.
    picture.insert(0, "")
    picture.append("")
    res = []
    # For each row...
    for i in range(rows):
        line = picture[i]
        # Amount of "*" to complete the expected width.
        left = "*" * (math.floor((cols - len(line))/2))
        right = "*" * (math.ceil((cols - len(line))/2))
        line = left + line + right
        # Keep appending to the resulting picture.
        res.append(line)

    return res
