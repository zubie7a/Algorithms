import math

t = int(raw_input())
for i in xrange(1, t+1):
    p, x, y = map(int, raw_input().split(" "))
    # Centralize the coordinates.
    x, y = x - 50, y - 50
    # Get the regular angle of the pie progress, converting from
    # 90' start and clockwise to 0' start and counterclockwise.
    pA = (450 - (p/100.0) * 360) % 360
    # Radius of the Pie.
    pRad = 50
    # Angle of the given coordinate from 0' counterclockwise.
    cA = (360 + math.degrees(math.atan2(y, x))) % 360
    # Radius of the coordinate.
    cRad = math.sqrt(x**2 + y**2)
    res = ""
    if p == 0:
        # No progress is done if p is 0, so result is always white.
        res = "white"
    elif pA < 90:
        # coord rad <= pie rad, pie angle <= coord angle <= 90.
        # or the given point is 0,0 meaning that if there's any progress
        # then this point will always be black.
        if (cRad <= pRad and (pA <= cA and cA <= 90)) or (x, y) == (0, 0):
            res = "black"
        else:
            res = "white"
    elif pA >= 90:
        # coord rad <= pie rad, 
        # pie angle <= coord angle OR coord angle <= 90 (because split at 0')
        # or the given point is 0,0 meaning that if there's any progress
        # then this point will always be black.
        # If progress is 100%, then pA == 90 and pa <= cA or cA <= 90 is True.
        if (cRad <= pRad and (pA <= cA or cA <= 90)) or (x, y) == (0, 0):
            res = "black"
        else:
            res = "white"
    # Problem didn't pass because used %r instead of %s :-(
    # So it printes "Case #1: 'black'" instead of "Case #1: black"
    # %r leaves the string quotes, %s removes them.
    print "Case #%d: %s" % (i, res)
