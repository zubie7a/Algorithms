# 02 - Nesting Depth

# tl;dr Given a string of digits S, insert a minimum number of opening and
# closing parentheses into it such that the resulting string is balanced and
# each digit d is inside exactly d pairs of matching parentheses.

num_cases = int(input())
for t in range(1, num_cases + 1):
    numbers = input()

    opens = 0
    to_close = 0
    result = ""
    for i in range(len(numbers)):
    	# Iterate over each digit...
        digit = int(numbers[i])
    	# Now we need to add opens as the difference between this digit value
    	# and current amout of opens.
        to_open = digit - opens
        # If this value is negative, it means we need to actually add closes.
        if (to_open > 0):
        	# Add the opens to the result string and to the count of opens.
            result += to_open * "("
            opens += to_open
        else:
        	# Add closes to the return string and substract that from count
        	# of opens.
	        result += abs(to_open) * ")"
	        opens -= abs(to_open)

        result += str(digit)
    # At the end of processing if there were still x opens, just add x closes.
    if (opens > 0):
    	result += opens * ")"

    print("Case #{}: {}".format(t, result))
