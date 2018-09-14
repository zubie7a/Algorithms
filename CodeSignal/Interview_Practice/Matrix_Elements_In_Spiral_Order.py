# https://codefights.com/interview/dx3iqAeokok6KoLHb
# Matrix Elements in Spiral Order: Google, Microsoft. Uber.
def matrixElementsInSpiralOrder(matrix):
    if len(matrix) == 0:
        return []
    if len(matrix[0]) == 0:
        return []
    # Direction marker.
    cur = 0
    # Directions: to right, downwards, to left, upwards.
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n, m = len(matrix), len(matrix[0])
    # Boundaries. Upon reaching any of these, direction
    # will change, and also these will shrink.
    l, r, u, d = -1, m, -1, n
    # Coordinates (rows, columns)
    i, j = 0, 0
    res = []
    # Do this until all m*n values have been visited.
    while len(res) != m*n:
        # Append visited cell to result.
        res.append(matrix[i][j])
        # Retrieve the delta for current direction marker.
        _i, _j = dirs[cur]
        i += _i
        j += _j
        # Right boundary was reached.
        # Only reachable while going rightwards on upper bound.
        if j == r:
            j -= 1 # Go back from right boundary.
            i += 1 # Go one space downwards.
            u += 1 # Shrink the upper boundary.
            cur = (cur + 1) % 4 # Advance current direction.
        # Down boundary was reached.
        # Only reachable while going downwards on right bound.
        if i == d:
            i -= 1 # Go back from down boundary.
            j -= 1 # Go one space to the left.
            r -= 1 # Shrink the right boundary.
            cur = (cur + 1) % 4 # Advance current direction.
        # Left boundary was reached.
        # Only reachable by going leftwards on lower bound.
        if j == l:
            j += 1 # Go back from left boundary.
            i -= 1 # Go one space upwards.
            d -= 1 # Shrink the lower boundary.
            cur = (cur + 1) % 4 # Advance current direction.
        # Up boundary was reached.
        # Only reachable by going upwards on left bound.
        if i == u:
            i += 1 # Go back from up boundary.
            j += 1 # Go one space to the right.
            l += 1 # Shrink the left boundary.
            cur = (cur + 1) % 4 # Advance current direction.
    return res
