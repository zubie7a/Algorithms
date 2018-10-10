# https://app.codesignal.com/company-challenges/uber/4c3qzzQg8Zg9AfLKH
def fancyRide(l, fares):
    types = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    best_idx = -1
    best_cost = -1<<30
    for i in range(len(fares)):
        cost = fares[i] * l
        # The total cost has to be within the bounds of the initial $20
        # and also it has to be more expensive than previous cost, seeking
        # to minimize the difference between cost and the $20.
        if 20 - cost >= 0 and cost > best_cost:
            best_idx = i
            best_cost = cost

    return types[best_idx]
