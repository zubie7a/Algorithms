# https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
def chessKnight(cell):
    # Find the number of available cells where a Knight can move to.
    coord_x = int(ord(cell[0]) - ord('a') + 1)
    coord_y = int(cell[1])
    res = 0
    # Possibilities: +1+2, +1-2, -1+2, -1-2, +2+1, +2-1, -2+1, -2-1
    moves1 = [1, -1]
    moves2 = [2, -2]
    # Pick one from moves1 and one from moves2, for both x and y coords.
    for dx in moves1:
        for dy in moves2:
            new_x = coord_x + dx
            new_y = coord_y + dy
            # Create bounds conditions.
            bounds_x = 1 <= new_x and new_x <= 8
            bounds_y = 1 <= new_y and new_y <= 8
            if bounds_x and bounds_y:
                res += 1
    # Now combine using values the opposite way.
    for dx in moves2:
        for dy in moves1:
            new_x = coord_x + dx
            new_y = coord_y + dy
            # Create bounds conditions.
            bounds_x = 1 <= new_x and new_x <= 8
            bounds_y = 1 <= new_y and new_y <= 8
            if bounds_x and bounds_y:
                res += 1

    return res
