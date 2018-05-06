# https://www.hackerrank.com/challenges/gem-stones
rock_num = int(raw_input())
rocks = []
for _ in range(rock_num):
    rock = raw_input()
    # Add just the unique elements of the rock, not
    # the repetitions.
    rocks.append(set(rock))
# Each element of rocks is a set of elements. Reduce
# doing the set 'intersection' operation, in the end
# the result will only have the elements present in
# all the sets because its the intersection of all.
print len(reduce(lambda x, y: x&y, rocks))
