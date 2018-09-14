# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM
def sortByHeight(heights):
    # There's people in a park. Sort them by height and place them
    # in between the trees in the park (marked by -1).
    # First filter the people out from the trees and sort them.
    people = sorted(filter(lambda x: x != -1, heights))
    people_index = 0
    # Then put back sorted people at the slots between trees.
    for i in range(len(heights)):
        # Leave trees quiet.
        if heights[i] != -1:
            heights[i] = people[people_index]
            people_index += 1

    return heights
