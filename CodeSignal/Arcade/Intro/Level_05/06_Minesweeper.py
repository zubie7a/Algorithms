# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
def minesweeper(matrix):
    n, m = len(matrix), len(matrix[0])
    # Create a n * m matrix.
    minegrid = [[0 for _ in range(m)] for _ in range(n)]
    '''
    Output a solved MineSweeper grid. 'True' means there's a mine
    in a certain position. The result should have the count of mines
    surrounding a certain position, except itself.

    Input: matrix: 
        [[  true, false, false,  true], 
         [ false, false,  true, false], 
         [  true,  true, false,  true]]

    Output:
        [[0,2,2,1], 
         [3,4,3,3], 
         [1,2,3,1]]
    '''
    # Iterate every cell (i, j) in m*n matrix.
    for i in range(n):
        for j in range(m):
            # Do all possible directions from the current position.
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    # Don't count the current position.
                    if x == 0 and y == 0:
                        continue
                    # Find neighbor positions with the offsets.
                    _x, _y = i + x, j + y
                    # If its outside bounds do nothing.
                    if not (0 <= _x < n and 0 <= _y < m):
                        continue
                    # If there's a mine then add to the count of
                    # neighboring mines.
                    if matrix[_x][_y] == True:
                        minegrid[i][j] += 1

    return minegrid
