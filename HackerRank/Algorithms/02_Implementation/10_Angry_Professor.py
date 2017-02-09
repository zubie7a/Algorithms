# https://www.hackerrank.com/challenges/angry-professor
t = int(raw_input())
for _ in xrange(t):
    # n: total number of students
    # k: quorum needed to start the class.
    n, k = map(int, raw_input().split())
    # A list of times, negative means arriving early,
    # zero means arriving on time, and positive means
    # arriving late.
    times = map(int, raw_input().split())
    # Filter out those who arrived after class was
    # supposed to start, leaving only those who arrived
    # either early or on time.
    timely = filter(lambda x: x <= 0, times)
    # If the quorum is less than or equal to the amount
    # of people who arrived timely, the class won't be
    # cancelled.
    if k <= len(timely):
        print "NO"
    # The class will be cancelled if the amount that did
    # not arrive late was not enough to meet the quorum.
    else:
        print "YES"
