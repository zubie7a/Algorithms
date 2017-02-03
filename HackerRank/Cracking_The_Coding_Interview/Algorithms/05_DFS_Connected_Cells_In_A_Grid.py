# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

def DFS(grid, i, j):
    # If coordinates exceed bounds, return 0.
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
        return 0
    # If coordinates are empty or already visited, return 0.
    if grid[i][j] == -1 or grid[i][j] == 0:
        return 0
    # If its here, it must be a 1. So count and mark visited.
    count, grid[i][j] = 1, -1
    # Now visit all neighbors recursively and add found areas.
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            count += DFS(grid, i + x, j + y)
    return count

# n, m: dimensions of the grid.
n, m = int(raw_input()), int(raw_input())
# Read grid line by line.
grid = [map(int, raw_input().split()) for _ in range(n)]
# res will hold the max area value.
res = -1
for i in range(n):
    for j in range(m):
        # Do a DFS from each starting point, but the ones
        # already visited or nothing there, will be skipped.
        if grid[i][j] == 1:
            # Store the max area value found.
            res = max(res, DFS(grid, i, j))
print res
