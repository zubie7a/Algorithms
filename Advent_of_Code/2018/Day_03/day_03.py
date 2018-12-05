# https://adventofcode.com/2018/day/3

claims = []

# test_claims = [
#     "#1 @ 1,3: 4x4",
#     "#2 @ 3,1: 4x4",
#     "#3 @ 5,5: 2x2",
# ]

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = str(input())
        # print(line)
        claims.append(line)
except Exception:
    # print("EOF")
    None

# Area to put claims on. Each position will be a list of claims that
# cover that individual (i, j) cell.
area = [ [ [] for _ in range(1000) ] for _ in range(1000) ]

# Make a set containing all claims, and another containing all claims that
# overlap. The difference between both sets will be the claims that don't
# overlap with any other.
set_all_claims = set([])
set_overlapping_claims = set([])

for claim in claims:
    # Before "@" it's the claim number.
    pre_at = claim.split("@")[0].strip()
    # After "@" it's the claim starting coordinates and dimensions.
    post_at = claim.split("@")[-1]
    # Before ":" it's coordinates, afterwards it's dimensions.
    coords, dims = map(lambda x: x.strip(), post_at.split(":"))
    # Coordinates separated by "," as in "{x},{y}"
    coord_x, coord_y = map(int, coords.split(","))
    # Dimensions separated by "x" as in "{a}x{b}"
    dim_x, dim_y = map(int, dims.split("x"))

    # Keep track of all existing claims.
    set_all_claims.add(pre_at)

    for i in range(dim_y):
        for j in range(dim_x):
            pos_y = i + coord_y
            pos_x = j + coord_x
            # Put the current claim number at this position.
            area[pos_y][pos_x].append(pre_at)


count = 0
# Count the number of cells with overlapping claims, and find the
# non-overlapping claims.
for i in range(len(area)):
    for j in range(len(area[0])):
        if len(area[i][j]) > 1:
            # Add one to the count of overlapping cells.
            count += 1
            # Add all these overlapping claims to a set.
            set_overlapping_claims |= set(area[i][j])

# Both problems are highly dependent on each other so only one file.
# Result: 104241.
print("The count of cells with overlapping claims is {}".format(count))

# Result: #806.
independent_claim = (set_all_claims - set_overlapping_claims)
independent_claim = next(iter(independent_claim))
print("The only non-overlapping claim is {}".format(independent_claim))
