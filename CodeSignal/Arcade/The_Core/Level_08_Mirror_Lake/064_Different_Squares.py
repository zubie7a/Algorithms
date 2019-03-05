# https://app.codesignal.com/arcade/code-arcade/mirror-lake/fQpfgxiY6aGiGHLtv
def differentSquares(matrix):
    # Number of rows.
    n = len(matrix)
    # Number of columns.
    m = len(matrix[0])

    unique_matrices = set([])
    for i in range(n - 1):
        for j in range(m - 1):
            # Let's store here an array-flattened 2x2 matrix that
            # starts at the current coordinate of the original matrix.
            sub_matrix = []
            for di in range(2):
                for dj in range(2):
                    # Store current position in the flattened matrix.
                    sub_matrix.append(matrix[i + di][j + dj])
            # If the flattened matrix doesn't have 4 elements, it means
            # that it was attempted to be build on a bound so it's not 2x2.
            if len(sub_matrix) == 4:
                # Join the elements of the flattened matrix with a "," into
                # a string so that the set can store it because regular
                # arrays can't be hashed in the set.
                unique_matrices.add(",".join(map(str, sub_matrix)))

    # The amount of unique 2x2 sub matrices in a larger NxM matrix.
    return len(unique_matrices)
