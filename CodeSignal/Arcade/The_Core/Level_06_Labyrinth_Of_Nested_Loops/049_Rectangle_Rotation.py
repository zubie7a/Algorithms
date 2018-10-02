# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/tuKA5f3zpzkKKejJx/
import math

def rectangleRotation(a, b):
    # We have a rectangle of sides a and b which is rotated 45 degrees
    # in the cartesian planes. How many integer coordinates fall inside
    # of it (even in the sides)?
    # If we look at it like this:
    #  ___________________
    # |o o o o o o o o o o|
    # | x x x x x x x x x |
    # |o o o o o o o o o o|
    # | x x x x * x x x x |
    # |o o o o o o o o o o|
    # | x x x x x x x x x |
    # |o_o_o_o_o_o_o_o_o_o|
    # 
    # From the center (*) vertically, the units are sqrt(2), 
    # the side of one square, the same happens horizontally.
    # You can find the areas of two rectangles, one that has
    # points in even rows (o) a bit shifted from the points of
    # one in the odd rows (x).
    # 
    rows = (a // math.sqrt(2)) + 1
    cols = (b // math.sqrt(2)) + 1
    # The odds positions and the evens positions areas.
    total = (rows * cols) + ((rows - 1) * (cols - 1))
    total -= 1 if total % 2 == 0 else 0
    return total
