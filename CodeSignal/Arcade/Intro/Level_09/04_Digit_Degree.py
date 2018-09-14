# https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo
def digitDegree(number):
    
    def recursive_replace(n):
        # Convert the number to a string.
        str_n = str(n)
        # If the length of the number is one, then don't need to reduce
        # it anymore.
        if len(str_n) == 1:
            return 0
        # Replace n to the sum of its digits.
        n = sum([int(x) for x in str_n])
        # Now that we did one replacement, lets recurse to do it more.
        return 1 + recursive_replace(n)

    # The result is the recursive function call with the original value.
    return recursive_replace(number)
