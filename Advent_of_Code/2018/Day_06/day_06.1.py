# https://adventofcode.com/2018/day/6

# List of coordinates to read from STDIN.
coords = []

# Result: 17.
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
# Everything on a corner can extend outwards forever.
# Find out the "external" ones and only compute for things inside.
distances = [ [ {} for _ in range(w) ] for _ in range(h) ]

for j in range(h):
    for i in range(w):
        for k in range(len(coords)):
            cx, cy = coords[k]
            dx = abs(i - cx)
            dy = abs(j - cy)
            m_dist = dx + dy
            # The dict goes from distance to coordinates that far,
            # for easy identifying if there's the same distance to
            # two or more coordinates.
            if m_dist not in distances[j][i]:
                distances[j][i][m_dist] = []
            # Add the k-th coordinate to the list of coordinates
            # at a given manhattan distance from current point.
            distances[j][i][m_dist].append(k)

# Now that we have the distances, find the area of each coordinate.
# Also, exclude coordinates which have a point in their area touching
# the grid boundary, those will extend forever, only the "trapped"
# ones are useful.
grid = [ [ -1 for _ in range(w) ] for _ in range(h) ]
for i in range(h):
    for j in range(w):
        # Determine to which coordinate does this point "belong" to,
        # which is the closest one, or if there's a tie then it does
        # not belong to any.
        closest_dist = sorted(distances[j][i].keys())[0]
        closest_coords = distances[j][i][closest_dist]
        if len(closest_coords) == 1:
            grid[j][i] = closest_coords[0]

# Now each cell of 'grid' contains the coordinate that is closest
# to that cell. Count the areas of each of those coordinates,
# remove those touching the edges, and then get the largest one.
coord_areas = {}
infinite_coords = {}
for i in range(h):
    for j in range(w):
        closest_coord = grid[j][i]
        if closest_coord not in coord_areas:
            coord_areas[closest_coord] = 0
        coord_areas[closest_coord] += 1
        # Store separately coordinates that touch edges to exclude them.
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid) - 1:
            infinite_coords[closest_coord] = 1

# Put the areas into a list while excluding areas from coordinates that extend
# infinitely ~ touch the edges because nothing further away will block them.
areas = (
    [v for k, v in coord_areas.items() if k not in infinite_coords]
)

largest_enclosed_area = sorted(areas)[-1]
# Result: 3290.
print(largest_enclosed_area)
