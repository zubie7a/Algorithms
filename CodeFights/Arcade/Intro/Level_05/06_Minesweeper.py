# https://codefights.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
def minesweeper(matrix):
    n, m = len(matrix), len(matrix[0])
    minegrid = [[0 for _ in range(m)] for _ in range(n)]
    dirs = [-1, 0, 1]
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
    for i in range(n):
        for j in range(m):
            for x in dirs:
                for y in dirs:
                    # Don't count the current position.
                    if x == 0 and y == 0:
                        continue
                    _x, _y = i + x, j + y
                    # If its a neighbor outside bounds.
                    if not (0 <= _x < n and 0 <= _y < m):
                        continue
                    if matrix[_x][_y] == True:
                        minegrid[i][j] += 1
    return minegrid
