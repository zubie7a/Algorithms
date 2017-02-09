# https://www.hackerrank.com/challenges/utopian-tree
t = int(raw_input())
for _ in xrange(t):
    # An Utopian Tree is planted at the start of spring
    # with length 1.
    height = 1
    # Then it will grow for a certain number of cycles.
    cycles = int(raw_input())
    for i in xrange(cycles):
        # At an odd cycle, spring, means the tree will
        # double its height.
        if i % 2 == 0:
            height *= 2
        # At an even cycle, summer, means the tree will
        # increase its height by one.
        else:
            height += 1
    # Print the final height of the Utopian Tree afterwards.
    print height
