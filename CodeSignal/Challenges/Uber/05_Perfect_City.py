# https://app.codesignal.com/company-challenges/uber/gsjPcfsuNavxhsQQ7
from math import floor

def perfectCity(departure, destination):
    # Consider a city where all the blocks are squares, so the
    # distance between any pair of points can be found with the
    # Manhattan Distance formula. Given a pair of points, find
    # the shortest distance between both. But then, the points
    # can be not in corners but in the middle of a street.
    p1, p2 = departure
    n1, n2 = destination

    dx, dy = 0, 0
    # Arrange them so that p is the leftmost and n rightmost.
    if (p1 > n1):
        p1, n1 = n1, p1
    # Arrange them so that p is lower and n the upper.
    if (p2 > n2):
        p2, n2 = n2, p2

    if floor(n1) != floor(p1):
        # If they are not in the same cell, just compute the
        # horizontal distance.
        dx = n1 - p1
    else:
        # If they are in the same cell, then through the side
        # we go on one cell we return on the other.
        dx = min(
            p1 - floor(p1) + n1 - floor(n1),
            floor(p1 + 1) - p1 + floor(n1 + 1) - n1
        )

    if floor(n2) != floor(p2):
        # If they are not in the same cell, just compute the
        # vertical distance.
        dy = n2 - p2
    else:
        # If they are in the same cell, then through the side
        # we go on one cell we return on the other.
        dy = min(
            p2 - floor(p2) + n2 - floor(n2),
            floor(p2 + 1) - p2 + floor(n2 + 1) - n2
        )

    return dx + dy
