# https://leetcode.com/problems/island-perimeter/
from collections import deque

class Solution(object):
    def BFS(self, grid, w, h, i, j):
        # Doing ([-1] * h) * w will repeat the same list pointer, bad!
        visited = [[-1] * h for _ in range(w)]
        dq = deque([(i, j)])
        res = 0
        while len(dq) > 0:
            pos = dq.popleft()
            x, y = pos[0], pos[1]
            if visited[x][y] == 1:
                continue
            visited[x][y] = 1
            for _i, _j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    newX = x + _i
                    newY = y + _j
                    # Increase perimeter value only if next squares are either
                    # boundaries, or not land.
                    if any([newX < 0, newX >= w, newY < 0, newY >= h]):
                        res += 1
                        continue
                    if grid[newX][newY] != 1:
                        res += 1
                        continue
                    dq.append((newX, newY))
        return res
        
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid)
        height = len(grid[0])
        for i in range(width):
            for j in range(height):
                if grid[i][j] == 1:
                    return self.BFS(grid, width, height, i, j)
