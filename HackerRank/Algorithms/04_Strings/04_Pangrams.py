# https://www.hackerrank.com/challenges/pangrams
# Find if a given string uses all 26 alphabet charactes.
string = filter(lambda c: c.isalpha(), raw_input())
# Upper and lower case are the same for counting purposes.
print "not "*(len(set(string.lower())) != 26) + "pangram"
