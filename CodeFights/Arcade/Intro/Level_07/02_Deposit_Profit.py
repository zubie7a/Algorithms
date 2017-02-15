# https://codefights.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
def depositProfit(deposit, rate, threshold):
    years = 0
    while deposit < threshold:
        deposit += (rate/100) * deposit
        years += 1
    return years
