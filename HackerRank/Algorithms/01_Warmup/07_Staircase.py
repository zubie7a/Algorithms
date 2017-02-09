# https://www.hackerrank.com/challenges/staircase
n = int(raw_input())
# Print a staircase like
'''
n = 6
     #
    ##
   ###
  ####
 #####
######
'''
for i in range(n):
    print " "*(n - i - 1) + "#"*(i + 1)
