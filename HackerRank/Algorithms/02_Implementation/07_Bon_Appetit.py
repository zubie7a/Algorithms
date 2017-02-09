# https://www.hackerrank.com/challenges/bon-appetit
# Anna and Brian ate n dishes, but anna didn't eat from the kth one
# because of an allergy, so that one doesn't go into tab splitting.
n, k = map(int, raw_input().split())
# The list of costs for the n dishes.
costs = map(int, raw_input().split())
# What Anna should ideally pay, is the total of the dishes minus
# the one she didn't eat from, divided by two.
ideal = (sum(costs) - costs[k]) / 2.0
# The actual amount she paid.
paid = int(raw_input())
# If the paid the ideal, then Bon Appetit!
if paid == ideal:
    print "Bon Appetit"
# She either overpaid or underpaid, so print the difference.
else:
    print int(abs(paid - ideal))
