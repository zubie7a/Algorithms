# https://app.codesignal.com/arcade/intro/level-12/uRWu6K8E7uLi3Qtvx
def spiralNumbers(n):
    # Create a n*n matrix and store in it increasing numbers in a spiral.
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # 4 possible directions to go around
    dirs = ["right", "down", "left", "up"]
    # Index of the current direction we're taking, increasing it while
    # also wrapping around with modulus to go in "circles".
    dir_index = 0
    # The boundaries which will keep shrinking so that traversal while
    # changing directions will result in a spiral.
    min_x, max_x = -1, n
    min_y, max_y = -1, n
    value = 1
    # The indices to iterate cells.
    i, j = 0, 0
    # The limit of the simulation is the total number of cells.
    for k in range(n * n):
        # Store the current value in the cell we landed and increase the
        # value for the next iteration so all numbers are increasing.
        matrix[i][j] = value
        value += 1
        dir = dirs[dir_index]
        # Update the position based on the traversing direction, but
        # mind that one of the boundaries could be reached, if so then
        # change direction and shrink previous boundary.
        if dir == "right":
            j += 1
            # Reached right boundary, so start going down and shrink
            # the upper boundary.
            if j == max_x:
                j -= 1
                i += 1
                min_y += 1
                dir_index = (dir_index + 1) % 4
        elif dir == "down":
            i += 1
            # Reached bottom boundary, so start going left and shrink
            # the right boundary.
            if i == max_y:
                i -= 1
                j -= 1
                max_x -= 1
                dir_index = (dir_index + 1) % 4
        elif dir == "left":
            j -= 1
            # Reached left boundary, so start going up and shrink
            # the bottom boundary.
            if j == min_x:
                j += 1
                i -= 1
                max_y -= 1
                dir_index = (dir_index + 1) % 4
        elif dir == "up":
            i -= 1
            # Reached top boundary, so start going right and shrink
            # the left boundary.
            if i == min_y:
                i += 1
                j += 1
                min_x += 1
                dir_index = (dir_index + 1) % 4
        
    return matrix
