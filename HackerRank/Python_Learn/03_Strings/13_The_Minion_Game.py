# https://www.hackerrank.com/challenges/the-minion-game
from collections import Counter
def minion_game(string):
    # your code goes here
    string = string.lower()
    consonants = set("bcdfghjklmnpqrstvwxyz")
    vowels = set("aeiou")
    # Stuart will get 1 point for every non-distinct substring that starts
    # with a consonant, Kevin for every that starts with a vowel.
    score_S, score_K = 0, 0
    length = len(string)
    for i in range(length):
        # No need to compute the substrings, once we know the starting char,
        # we can simply calculate the number of substrings that can be formed
        # from here on to the end of the string.
        if string[i] in consonants:
            score_S += length - i
        if string[i] in vowels:
            score_K += length - i
    if score_S > score_K:
        print "Stuart %d" % score_S
    elif score_S < score_K:
        print "Kevin %d" % score_K
    else:
        print "Draw"
