# https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2
def knapsackLight(value1, weight1, value2, weight2, max_weight):
    # You can take one item, the other, both, or none, depending on their
    # weight and the max weight you can carry. Whats the max value you can
    # carry considering these constraints?
    if weight1 + weight2 <= max_weight:
        return value1 + value2
    if value1 > value2:
        if weight1 <= max_weight:
            return value1
        elif weight2 <= max_weight:
            return value2
    else:
        if weight2 <= max_weight:
            return value2
        elif weight1 <= max_weight:
            return value1

    # We can't carry anything :-(
    return 0
