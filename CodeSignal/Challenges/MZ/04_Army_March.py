# https://app.codesignal.com/company-challenges/mz/jepkCB8BMzTHGSbEc
from math import sqrt 

def armyMarch(a, b, v1, v2):
    # The left side of the chart is field terrain, which has a speed
    # v1 when travelling on it. The right side of the chart is forest
    # terrain, which has a speed v2 when travelling on it.
    # Given a starting point and an ending point, find the optimal
    # point in the terrain change so that we minimize the time from
    # A to B.
    ax, ay = a
    bx, by = b
    # Make sure B is always above A.
    if (ay > by):
        ax, ay, bx, by, v1, v2 = bx, by, ax, ay, v2, v1

    # Time based on two coordinates, a point to reach and a speed.
    # speed = distance / time, so time = distance / speed.
    def time_reach(x, y, mid, v):
        return sqrt((x - 0)**2 + (y - mid)**2) / v

    # There's only one point with the min time. As you get further
    # from that point, time increases, like a parabola. So start
    # in the given range checking both sides. Only one side will be
    # closer to the min than the other, so divide by 2 repeatedly
    # taking the side which time evaluated at a middle point is less
    # than the other.
    def bin_search(dn, up):
        mid_point = (dn + up) / 2
        # Upper half.
        mid_point_up = (mid_point + up) / 2
        time_lu = time_reach(ax, ay, mid_point_up, v1)
        time_ru = time_reach(bx, by, mid_point_up, v2)
        time_up = time_lu + time_ru
        # Lower half.
        mid_point_dn = (mid_point + dn) / 2
        time_ld = time_reach(ax, ay, mid_point_dn, v1)
        time_rd = time_reach(bx, by, mid_point_dn, v2)
        time_dn = time_ld + time_rd
        # If result has converged, just return it.
        if abs(time_dn - time_up) < 0.0000001:
            return time_dn
        # If time in the upper half is lower, iterate there.
        elif time_up < time_dn:
            return bin_search(mid_point, up)
        # If time in the lower half is lower, iterate there.
        elif time_dn < time_up:
            return bin_search(dn, mid_point)

    return bin_search(ay, by)
