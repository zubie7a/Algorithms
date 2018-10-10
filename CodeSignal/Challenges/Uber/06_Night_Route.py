# https://app.codesignal.com/company-challenges/uber/tucq8L9FB7QyDZ4M6
import heapq

def nightRoute(city):
    # The number of islands.
    n = len(city)
    # Do the Dijkstra algorithm!
    # Array with recorded distances up to each island, seeking to minimize it.
    dists = [ 1<<30 for _ in range(n) ]
    # Priority queue via heap!
    pq = []
    # Start at the 0th island, with cost 0 to reach it. We want to know the
    # minimum distance to the (n - 1)-th island.
    heapq.heappush(pq, (0, 0))
    # While there's something in the priority queue...
    while len(pq):
        cur_dist, cur_node = heapq.heappop(pq)
        for next_node in range(n):
            next_dist = city[cur_node][next_node]
            # This means it's either a closed bridge or would be
            # visiting the same city.
            if next_dist == -1:
                continue
            # If the distance up to this point + the cost of transitioning
            # is less than the previously recorded distance for next node.
            if cur_dist + next_dist < dists[next_node]:
                dists[next_node] = cur_dist + next_dist
                heapq.heappush(pq, (dists[next_node], next_node))

    # Return the minimum distance found to the last island.
    return dists[-1]
