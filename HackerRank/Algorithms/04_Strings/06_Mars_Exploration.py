# https://www.hackerrank.com/challenges/mars-exploration
# A message should be a repetition of SOSSOSSOS... but
# it may have been distorted in the way.
msg = raw_input()
sos = "SOS" * (len(msg)/3)
# Count the differences as True values, then sum that.
print sum([sos[k] != msg[k] for k in range(len(msg))])
