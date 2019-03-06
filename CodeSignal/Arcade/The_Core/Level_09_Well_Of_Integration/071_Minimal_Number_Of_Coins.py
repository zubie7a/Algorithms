# https://app.codesignal.com/arcade/code-arcade/well-of-integration/sGwCfM5FzX7LhLcdk
def minimalNumberOfCoins(coins, price):
    # I have an infinite number of coins of certain specified values, and
    # I want to buy a banana of a certain price. Whats the minimum number
    # of coins I need to use to purchase this banana?

    # Dictionary to store memoization of recursive calculations.
    cache = {}
    def recurse_coins(used_coins, price_left):

        # This was a feasible combination of coins, so it's a valid path.
        if price_left == 0:
            return used_coins
        # These coins exceeded the price, so it's an invalid path.
        elif price_left < 0:
            return 1<<30

        # If the state for coins used up to this point and price left
        # onwards is the same, use that already stored result.
        if (used_coins, price_left) in cache:
            return cache[(used_coins, price_left)]

        # Default result is a very large number, we want the minimum.
        result = 1<<30
        for idx in range(len(coins)):
            # For each possible coin value, try consuming it at this point.
            coin_value = coins[idx]
            # Recurse with one more used coin (won't store information about which)
            # and substract from the remaining price the value of that coin.
            coins_total = recurse_coins(used_coins + 1, price_left - coin_value)
            # If this leads down a feasible path, pick the minimum one, if unfeasible
            # will return a really large value.
            result = min(result, coins_total)

        # Store the computed state in the memoization.
        cache[(used_coins, price_left)] = result
        return result

    return recurse_coins(0, price)
