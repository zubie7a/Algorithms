# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/oL7YuygJKtMSNLeJn
def weakNumbers(n):
    # Define the weakness of a given number x as the number of positive
    # integers smaller than x that have more divisors than x.
    # Given a number n, what is the weakest number in the range [1, n],
    # and how many other numbers have this weakness?

    divisors = [2 for _ in range(n + 2)]
    # One only has 1 divisor. Every other number by default has two,
    # one and itself.
    divisors[1] = 1
    for i in range(2, n + 1):
        # Check all values up to the number (1-i) non inclusive either.
        for j in range(2, i):
            if i % j == 0:
                # Keep adding up divisors.
                divisors[i] += 1

    weaknesses = []
    # Now again for all values...
    for i in range(1, n + 1):
        more_divisors = 0
        # For all other values to its left (non-inclusive)...
        for j in range(1, i):
            # Compare the amount of divisors and add up if it has more.
            if divisors[j] > divisors[i]:
                more_divisors += 1
        # Store the weakness of this value.
        weaknesses.append(more_divisors)
    
    # Return the highest weakness value and how many numbers have it too.
    weakest = max(weaknesses)
    times = weaknesses.count(weakest)
    return [weakest, times]
