# https://www.hackerrank.com/challenges/append-and-delete
s, t, k = raw_input(), raw_input(), int(raw_input())

i = 0
# Advance an iterator until the last point both strings
# have sequential characters in common from the start.
while i < len(s) and i < len(t) and s[i] == t[i]:
    i += 1

# spareS/T are the amount of characters from the point
# where the common sequence stops for both strings.
spareS, spareT = len(s) - i, len(t) - i
# A way to match S and T, is to delete the spares from
# S and insert the spares from T.
needed = spareS + spareT
# To match this way, the needed amount has to be less or
# equal than k, and if there's a remaining amount, it 
# has to be even so it can be done away with repeated
# deletions and insertions of the last character.
withSpares = (needed <= k and (k - needed) % 2 == 0)

# A match can also be made by completely erasing one
# string, this may be particularly useful to consume a
# large k until making it even or odd as needed because
# deletions on empty space keep giving empty space. Then
# with the remaining k recreate the other string.
withEmpty = k - len(s) >= len(t)
if withSpares or withEmpty:
    print "Yes"
else:
    print "No"
