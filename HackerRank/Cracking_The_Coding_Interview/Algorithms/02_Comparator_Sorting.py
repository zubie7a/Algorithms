# https://www.hackerrank.com/challenges/ctci-comparator-sorting

class Player:
    # Initialize the class.
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # Method to return a string representable version of object.
    def __repr__(self):
        return "%s %d" % (self.name, self.score)
    # Comparator method for the object.
    # Usually when passing a cmp function, comparing a and b, 
    # -1 denotes that a is less than b,
    #  0 denotes that a is equal than b,
    #  1 denotes that a is greater than b.
    # To do a reverse ordering, swap -1 and 1.
    def comparator(a, b):
        # To sort descending by score, lets make a<b return
        # 1 so sorting algorithm takes it as the opposite.
        if a.score < b.score:
            return 1
        # If both scores are equal, then sort by name.
        elif a.score == b.score:
            # Since we do want the sorting to be done ascendent,
            # return the usual values, a<b = -1, a==b = 0, a>b = 1
            if a.name < b.name:
                return -1
            elif a.name == b.name:
                return 0
            elif a.name > b.name:
                return 1
        # To sort descending by score, lets make a>b return
        # -1 so sorting algorithm takes it as the opposite.
        elif a.score > b.score:
            return -1

n = int(raw_input())
data = []
'''
5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150
'''
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
# Sort students by descending score, then alphabetically.
data = sorted(data, cmp=Player.comparator)
# Could also sort by using a key tuple!
# data = sorted(data, key=lambda x: (-x.score, x.name))
for i in data:
    print i.name, i.score
'''
aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
'''
