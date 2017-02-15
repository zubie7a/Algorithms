# https://codefights.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
def sortByHeight(a):
    # There's people in a park. Sort them by height and place them
    # in between the trees in the park (marked by -1).Ellipsis
    # First filter the people out from the trees.
    b = sorted(filter(lambda x: x != -1, a))
    bIter = 0
    # Then put back sorted people at the slots between trees.
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b[bIter]
            bIter += 1
    return a 
