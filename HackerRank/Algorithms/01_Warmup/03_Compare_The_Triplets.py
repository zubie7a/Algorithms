# https://www.hackerrank.com/challenges/compare-the-triplets
# For a pair of triplets with scores, get the amount of
# wins from one triplet against the other.
tripletsA = map(int, raw_input().split())
tripletsB = map(int, raw_input().split())
# A win is having strictly greater score than the other
# triplet in the same position.
scoreA = sum([tripletsA[i] > tripletsB[i] for i in range(3)])
scoreB = sum([tripletsB[i] > tripletsA[i] for i in range(3)])
print scoreA, scoreB
