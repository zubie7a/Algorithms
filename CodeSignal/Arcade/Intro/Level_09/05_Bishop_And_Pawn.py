# https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
def bishopAndPawn(bishop, pawn):
    # Determine if a bishop can capture a pawn in a single move.
    def get_coord(piece):
        coord_x = int(ord(piece[0]) - ord('a') + 1)
        coord_y = int(piece[1])
        return (coord_x, coord_y)

    b_coord = get_coord(bishop)
    p_coord = get_coord(pawn)

    # If the pawn is in the same vertical/horizontal axis than the
    # bishop, then it can't be captured in a single move given that
    # the bishop can only move diagonally.
    if b_coord[1] == p_coord[1] or b_coord[0] == p_coord[0]:
        return False

    # Now, check with the formula of the cartesian slope to see if
    # both positions are in a perfect diagonal.
    # m = (y2 - y1) / (x2 - x1)
    m = (b_coord[1] - p_coord[1]) / (b_coord[0] - p_coord[0])
    # The slope can also be negative, all it matters is that the
    # absolute of rate in X is the same than the absolute rate in Y.
    return abs(m) == 1
