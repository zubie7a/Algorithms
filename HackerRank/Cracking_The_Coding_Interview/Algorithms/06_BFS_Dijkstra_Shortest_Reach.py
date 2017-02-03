# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
from __future__ import print_function
import heapq

class Graph(object):
    def __init__(self, n):
        self.n = n
        # Each node will have a list of nodes it goes to. 
        self.nodes = {i: [] for i in xrange(n)}
        
    def connect(self, x, y):
        # Bidirectional graph, add an edge in both ways.
        self.nodes[x].append(y)
        self.nodes[y].append(x)
        
    def find_all_distances(self, s):
        # This will return a list of distances from s to
        # all other nodes.
        distances = self.dijkstra(self.nodes, s)
        res = []
        for distance in distances:
            # Nodes with infinite distances weren't reached,
            # so replace 1<<31 with -1.
            if distance == 1<<31:
                res.append(-1)
            # Node with distance 0 is the starting node, skip.
            elif distance == 0:
                continue
            # Just append the distance found.
            else:
                res.append(distance)
        return res
        
    def dijkstra(self, nodes, s):
        # For shortest distances, use dijkstra.
        # By default the distance to each node will be
        # a huge number. Its like BFS but with a heap.
        distances = [1<<31 for _ in range(len(nodes))]
        # Mark the distance from starting node to itself
        # as 0, to avoid printing it later.
        distances[s] = 0
        # Now, use a priority queue (heap). Its first node
        # will be the starting node, and cost to itself, 0.
        pq = [(0, s)]
        # While there's elements in the priority queue.
        while len(pq) > 0:
            # The element at the top has the less
            # cumulative distance (Since its a min-heap).
            top = heapq.heappop(pq)
            top_weight = top[0]
            top_index = top[1]
            # For all neighbors of this node...
            for node_id in self.nodes[top_index]:
                # New distance = cumulative + 6.
                new_weight = top_weight + 6
                # This prevents loops, as nodes will only
                # enter the heap if the acum distance is
                # is less than the previous one recorded,
                # and revisiting nodes in a loop will only
                # reach it again and again with much bigger
                # distances.
                if new_weight < distances[node_id]:
                    distances[node_id] = new_weight
                    # Push new node, with its cumulative
                    # weight up to that point.
                    heapq.heappush(pq, (new_weight, node_id))
        return distances

for _ in range(int(raw_input())):
    # n: nodes, m: edges.
    n,m = map(int, raw_input().split())
    # Initialize a graph with n nodes.
    graph = Graph(n)
    # Read all edges. Since its undirected, do it in both
    # directions (x to y is the same as y to x).
    for _ in xrange(m):
        x, y = map(int, raw_input().split())
        graph.connect(x - 1, y - 1) 
    s = int(raw_input())
    res = graph.find_all_distances(s - 1)
    print(*res, sep=" ")
