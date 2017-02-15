# https://codefights.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def matrixElementsSum(matrix):
    hauntedColumns = [1 for _ in range(len(matrix[0]))]
    cost = 0
    # Find the cost of the hotels rooms. The thing is that if
    # a room is haunted, then nobody will rent any room below
    # it on the same column. So once a haunted room is visited,
    # mark the column as haunted so future rooms on same column
    # are avoided.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cost += matrix[i][j] * hauntedColumns[j]
            if matrix[i][j] == 0:
                hauntedColumns[j] = 0
    return cost
