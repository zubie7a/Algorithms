# https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta
def phoneCall(min1, min2_10, min11, cents):
    # Some phone usage rate may be described as follows:
    #     * First minute of a call cost min1 cents.
    #     * each minute the 2nd up to 10th (inclusive) costs min2_10 cents
    #     * each minute after 10th costs min11 cents.
    # With a particular number of individual cents, whats the longest you can call?
    total_minutes = 0
    # First minute.
    if cents >= min1:
        total_minutes += 1
        cents -= min1
    # Minutes from 2nd to 10th.
    minute = 2
    # Start looping until you reach 10 minutes or run out of money.
    while minute <= 10 and cents >= min2_10:
        total_minutes += 1
        cents -= min2_10
        minute += 1
    # Only apply this final step if minutes from 11th onwards.
    if minute > 10:
        total_minutes += (cents//min11)

    return total_minutes
