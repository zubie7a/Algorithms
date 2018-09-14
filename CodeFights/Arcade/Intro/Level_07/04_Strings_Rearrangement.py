# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
def stringsRearrangement(input_array):
    # Given an array of equal-length strings, check if its possible to
    # rearrange the strings in such a way that after the rearrangement
    # the strings at consecutive positions would differ by exactly one
    # character. This sounds like a graphs problem!

    # Calculate the distance between strings. This will create
    # a sorts-of adjacency matrix, where the value is the amount
    # of differing characters between any two given strings. Then see
    # if we can traverse all strings by making jumps of exactly one
    # character!

    # Then do a graph traversal on that 'adjacency matrix'. The 
    # shortest-distance traversal should return a length of (n-1)
    # visited elements, which would be the sum of 1 costs for each
    # pair of strings.
    arr = input_array[:]
    n, m = len(arr), len(arr[0])
    costs = [[float('inf') for _ in range(n)] for _ in range(n)]
    # For each possible pair of words arr[i], arr[j]:
    for i in range(n):
        for j in range(n):
            # Avoid it if its the same word. It will remain marked
            # as cost inf to avoid being visited in the graph traversal!
            # Otherwise comparing with itself would return cost 0.
            if i == j:
                continue
            # The differing character cost between arr[i] and arr[j].
            costs[i][j] = sum([arr[i][k] != arr[j][k] for k in range(m)])

    # Each recursive call will have a list of visited indices (starting with
    # an empty list), and the current position.
    def DFS(visited, pos):
        v = visited[:]
        # Put current index as visited.
        v.append(pos)
        # If all strings/indices have been visited, the result is valid.
        if len(v) == n:
            return True
        # Start assuming the result is False.
        res = False
        # For all indices/strings...
        for i in range(n):
            # Except the ones already visited to prevent loops...
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
        # If any result is True, then res will become True until end.
        res |= DFS([], i)
    return res
