# https://codefights.com/interview/EDaACHNYHyH6qQFAL
# Word Ladder: LinkedIn, Amazon, Facebook.
import heapq
def wordLadder(beginWord, endWord, wordList):
    wordList = [beginWord] + wordList
    # The cost of transforming a word to another is the amount
    # of differing characters between both.
    def cost(w1, w2):
        return sum([w1[i] != w2[i] for i in range(len(w1))])
    
    # Dictionary to keep track of distances to each word,
    # initialized as infinite distances.
    distances = {
        word : float('inf') for word in wordList
    }
    distances[endWord] = float('inf')
    
    # Do a Dijkstra to find shortest distance from starting
    # word to last one.
    pq = [(1, beginWord)]
    while len(pq):
        topDist, topWord = heapq.heappop(pq)
        for nextWord in wordList:
            # The 'neighboring' words are those with cost 1
            # to move to.
            if cost(topWord, nextWord) == 1:
                nextDist = topDist + 1
                if nextDist < distances[nextWord]:
                    distances[nextWord] = nextDist
                    heapq.heappush(pq, (nextDist, nextWord))
    # If the last word wasn't visited, mark it with distance 0.
    if distances[endWord] == float('inf'):
        return 0
    # Return the found shortest distance to the last word. 
    return distances[endWord]
