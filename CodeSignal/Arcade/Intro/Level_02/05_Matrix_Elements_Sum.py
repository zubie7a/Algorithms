# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def matrixElementsSum(matrix):
    non_haunted_columns = [1 for _ in range(len(matrix[0]))]
    cost = 0
    # Find the cost of the hotels rooms. The thing is that if
    # a room is haunted, then nobody will rent any room below
    # it on the same column. So once a haunted room is visited,
    # mark the column as haunted so future rooms on same column
    # are avoided.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Add the cost of every cell if its not on a haunted col.
            # If its a haunted room (cost 0) it won't add anything.
            cost += matrix[i][j] * non_haunted_columns[j]
            # Now, if the cost was 0, then label the column as haunted.
            if matrix[i][j] == 0:
                non_haunted_columns[j] = 0

    # Alternatively to not keep extra state, just iterate on columns
    # first and then rows, and break once you find a haunted cell.
    return cost
