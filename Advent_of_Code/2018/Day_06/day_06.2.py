# https://adventofcode.com/2018/day/6

# List of coordinates to read from STDIN.
coords = []
limit = 10000

# Result: 16.
# test_limit = 32
# test_coords = [
#     (1, 1),
#     (1, 6),
#     (8, 3),
#     (3, 4),
#     (5, 5),
#     (8, 9)
# ]

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = str(input())
        # print(line)
        x, y = map(int, line.split(","))
        coords.append((x, y))
except Exception:
    # print("EOF")
    None

w, h = 500, 500
# Initialize all cells to have total distance 0 to all coordinates.
distances = [ [ 0 for _ in range(w) ] for _ in range(h) ]

# For each cell, just add the distance to each of the coordinates.
for j in range(h):
    for i in range(w):
        for k in range(len(coords)):
            cx, cy = coords[k]
            dx = abs(i - cx)
            dy = abs(j - cy)
            m_dist = dx + dy
            distances[j][i] += m_dist

area = 0
# The area that is less than 10000 is bound to be a single one
# because the further you go from the center the higher the distance
# to all coordinates go, so it forms sort of a circular shape.
for j in range(h):
    for i in range(w):
        if distances[j][i] < limit:
            area += 1

# Result: 45602.
print(area)
