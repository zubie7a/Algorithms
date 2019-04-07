# 02 - You Can Go Your Own Way

# Try to solve the labyrinth without repeating Lydia's path.
# The good news is that she has solved it. And it is a NxN grid.
# No matter what she has done, you can mirror her path and it's
# sure that you won't move between two cells same as she did.
# Just swap all her "S" for "E" and all her "E" for "S"!

num_cases = int(input())
for t in range(1, num_cases + 1):
    length = int(input())
    old_path = input()
    new_path = ""
    for step in old_path:
        if step == "S":
            new_path += "E"
        if step == "E":
            new_path += "S"

    # Case #1: ES
    # Case #2: SEEESSES
    print("Case #{}: {}".format(t, new_path))
