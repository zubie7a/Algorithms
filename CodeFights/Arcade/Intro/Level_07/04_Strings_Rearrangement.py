# https://codefights.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
def stringsRearrangement(inputArray):
    # Calculate the distance between strings. This will create
    # a sorts-of adjacency matrix, where the value is the amount
    # of differing characters between any two given strings.
    # 
    # Store such distances. Then do a graph traversal on that
    # 'adjacency matrix'. The shortest-distance traversal should
    # return a length of (n-1), which would be the sum of 1 costs
    # for each pair of strings.
    arr = inputArray[:]
    n, m = len(arr), len(arr[0])
    costs = [[float('inf') for _ in range(n)] for _ in range(n)]
    # For each pair of words arr[i], arr[j]:
    for i in range(n):
        for j in range(n):
            # Avoid it if its the same word. It will remain marked
            # as inf to avoid being visited in the graph traversal.
            if i == j:
                continue
            # The differing character cost between arr[i] and arr[j].
            costs[i][j] = sum([arr[i][k] != arr[j][k] for k in range(m)])
    
    # Each recursive call will have a list of visited indices, and the
    # current position.
    def DFS(visited, pos):
        v = visited[:]
        v.append(pos)
        # If all indices have been visited, the result is valid.
        if len(v) == n:
            return True
        res = False
        # For all indices...
        for i in range(n):
            # Except the ones already visited.
            if i in v:
                continue
            # If from current index to a next one can move with cost
            # 1, then do a recursive call over that next index.
            if costs[pos][i] == 1:
                res |= DFS(v, i)
        # If none of the recursive branches managed to visit all
        # the nodes with the strictly 1-cost jump condition, then
        # it means that they can't be arranged in the special way.
        return res
    
    res = False
    # Try a DFS starting from each index/word, to see if any
    # will visit all other nodes with the strictly 1-cost jump.
    for i in range(n):
        res |= DFS([], i)
    return res
