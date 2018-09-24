# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/RcK4vupi8sFhakjnh
from math import floor, ceil

def countBlackCells(n, m):
    # Theres a n * m rectangular grid, divided into two parts by a diagonal
    # line from the upper left to the lower right. Now lets paint the grid in
    # two different colors according to some rules:
    #     * A cell is painted black if it has at least one point in common
    #       with the diagonal. If diagonal lands on a corner, it touches
    #       all 4 cells around it.
    #     * Otherwise a cell is painted white.

    # Using the line formulas...
    slope = (n / m)
    # y = m*x, x = y/m.
    # Iterate with integer values and then round down.
    count = 0
    for i in range(1, m + 1):
        # Previous point.
        px, py = (i - 1, ((i - 1) * slope))
        # New point.
        nx, ny = (i, (i * slope))

        # The vertical cells contained between each one unit step in horizontal
        # direction are the floor of previous vertical value and ceil of new one.
        dy = (ceil(ny) - floor(py))
        count += dy
        # If also the new one landed precisely on a corner, then we add
        # two extra cells that touch this corner, but don't do it for the
        # very last corner.
        if ny == ceil(ny) and i < m:
            count += 2

    return count
