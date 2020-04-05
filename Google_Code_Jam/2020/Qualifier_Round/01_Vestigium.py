# 01 - Vestigium

# Vestigium means "trace" in Latin. In this problem we work with Latin squares
# and matrix traces. The trace of a square matrix is the sum of the values on
# the main diagonal (which runs from the upper left to the lower right).

# An N-by-N square matrix is a Latin Square if each cell contains one of N
# different values, and no value is repeated within a row or a column. In this
# problem we'll deal only with "natural Latin Squares", in which the N values
# are the integers between 1 and N.

# Given a matrix that contains only integers between 1 and N, we want to
# compute its trace and check whether it is a natural Latin square. To give
# some additional information, instead of simply telling us whether the matrix
# is a natural Latin Square or not, please compute the number of rows and the
# number of columns that contain repeated values.

from collections import Counter

num_cases = int(input())
for t in range(1, num_cases + 1):
	# The dimension of the matrix.
    n = int(input())
    # Now read the matrix.
    matrix = []
    for i in range(n):
    	row = list(map(lambda x: int(x), input().split(" ")))
    	matrix.append(row)

    # 1. Compute the trace.
    trace = 0
    for i in range(n):
        trace += matrix[i][i]

    # 2. Compute how many rows and how many columns have repeated values.
    # Build a set of values for each row and column, the set should have N
    # values, anything lower than that means the row/column has duplicates.
    rows_w_dups = 0
    for i in range(n):
        row = set(matrix[i])
        if (len(row) < n):
        	rows_w_dups += 1

    cols_w_dups = 0
    for i in range(n):
    	col = set([matrix[j][i] for j in range(n)])
    	if (len(col) < n):
    		cols_w_dups += 1

    print("Case #{}: {} {} {}".format(t, trace, rows_w_dups, cols_w_dups))
