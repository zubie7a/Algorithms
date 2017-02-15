# https://codefights.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    myMax = max(yourLeft, yourRight)
    myMin = min(yourLeft, yourRight)
    frMax = max(friendsLeft, friendsRight)
    frMin = min(friendsLeft, friendsRight)
    return myMax == frMax and myMin == frMin
