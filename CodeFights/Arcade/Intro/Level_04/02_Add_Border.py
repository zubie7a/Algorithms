# https://codefights.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
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
    x, y = len(picture) + 2, len(picture[0]) + 2
    picture.insert(0, "")
    picture.append("")
    res = []
    for i in range(x):
        line = picture[i]
        left = "*"*(math.floor((y - len(line))/2))
        right = "*"*(math.ceil((y - len(line))/2))
        line = left + line + right
        res.append(line)
    return res
