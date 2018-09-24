# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LAKReA3CR9EwkZGSz
def candles(candles_number, make_new):
    # When a candle burns, it leaves a leftover. Then, it takes `make_new`
    # leftovers to make a new candle, which in turn leaves one leftover.
    # How many candles can you burn in total?
    total = 0
    remains = 0
    while candles_number:
        # Add the current total of available candles.
        total += candles_number
        # With consumed candles, you can immediately assemble these new ones.
        new_candles = (candles_number//make_new)
        # Remains that could not be used
        remains += (candles_number % make_new)

        # Candles for next iteration
        candles_number = new_candles
        # See if the spare remains now can make candles.
        candles_number += (remains//make_new)
        # Remove the used remains from remains pile.
        remains -= (remains//make_new)*make_new

    return total
