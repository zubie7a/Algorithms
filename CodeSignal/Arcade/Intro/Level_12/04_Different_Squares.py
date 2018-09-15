# https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv
def differentSquares(matrix):
    # Find in a given matrix how much different sub-squares (2x2) are in it.
    # Lets store string-flattened squares in a set.
    # For example an square with elements 0, 7, 2, and 1 will be flattened
    # into a string "0,7,2,1" and inserted into the set to keep uniques.
    unique_squares = set([])
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = []
            for k in [0, 1]:
                for l in [0, 1]:
                    _i = i + k
                    _j = j + l
                    cell = matrix[_i][_j]
                    square.append(str(matrix[_i][_j]))
            unique_squares.add(",".join(square))

    return len(unique_squares)
