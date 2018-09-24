# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/8rqs3BLpdKePhouQM
def lineUp(commands):
    # 1. Everyone starts looking down in same direction.
    # 2. An [A] command will either keep everyone horizontal or vertical
    # looking, so it only matters if an [A] command came after a vertical.
    # 3. With a single [L] or [R] command they will be looking in different
    # directions, since there's at least one that turns wrong (but not 
    # everyone so there's no way everyone will look same after [L]/[R]).
    # 4. A second [L] or [R] will have everyone up or down again.
    prev = "vertical"
    count = 0
    for command in commands:
        if command == "L" or command == "R":
            # If it was vertically aligned, it no longer is.
            if prev == "vertical":
                prev = "horizontal"
            # If it was horizontal, now in vertical they're aligned.
            else:
                prev = "vertical"
        if prev == "vertical":
            count += 1

    return count
