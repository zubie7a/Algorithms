# https://www.hackerrank.com/challenges/alphabet-rangoli
from __future__ import print_function

def print_rangoli(size):
    # The whole alphabet.
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # The subset on which we are operating.
    subset = alpha[:size]
    
    # The base string, will be something like "e-d-c-b-a"
    # It will go in the middle, every row will be made from that base
    # string, and also be mirrored.
    base = "-".join(reversed(subset))
    rows = []
    # Generate the top-left square like this:
    '''--------e
       ------e-d
       ----e-d-c
       --e-d-c-b
       e-d-c-b-a'''
    for i in range(size):
        # Generate each row by removing trailing chars from the base string.
        row = base[:len(base) - i*2]
        # Pad that row to match length of the base string
        row = ("-" * (len(base) - len(row))) + row
        rows.insert(0, row)
    # Now that upper left corner is generated, mirror it downwards like this,
    # without adding again the base string:
    '''--------e
       ------e-d
       ----e-d-c
       --e-d-c-b
       e-d-c-b-a
       --e-d-c-b
       ----e-d-c
       ------e-d
       --------e'''
    rows.extend(reversed(rows[:-1]))
    # Now that the left half is generated, mirror each row to the right.
    for i in range(len(rows)):
        row = rows[i]
        # Reverse the row.
        rev_row = row[::-1]
        # Append the reversed row without the initial character.
        rows[i] = row + rev_row[1:] 
    '''--------e--------
       ------e-d-e------
       ----e-d-c-d-e----
       --e-d-c-b-c-d-e--
       e-d-c-b-a-b-c-d-e
       --e-d-c-b-c-d-e--
       ----e-d-c-d-e----
       ------e-d-e------
       --------e--------'''
    # The result is ready to be printed.  
    print(*rows, sep="\n")
