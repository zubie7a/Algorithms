# https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
def depositProfit(deposit, rate, threshold):
    years = 0
    # Given an initial deposit and an interest rate, how long will in
    # take for your money to reach a certain threshold?
    while deposit < threshold:
        deposit += (rate / 100) * deposit
        years += 1

    return years
