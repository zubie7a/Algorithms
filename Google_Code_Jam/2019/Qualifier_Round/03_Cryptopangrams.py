# 03 - Cryptopangrams

# I don't know how to do it for N <= 10^100, only N <= 10^4.
# The "factorize first value" thing will obviously explode for
# such a large N.

num_cases = int(input())
for t in range(1, num_cases + 1):
    # Parse the input.
    n, length = [int(x) for x in input().split(" ")]
    values    = [int(x) for x in input().split(" ")]

    # Take out the first value to factorize only it.
    first_value = values[0]
    first_factor = 2
    while first_value % first_factor != 0:
        first_factor += 1
    second_factor = first_value//first_factor

    prime_factors = {}
    prime_values = []

    def try_result(pos, carry_factor, factors_list, create_result=False):
        # Copy so we can modify this list locally.
        factors = factors_list[:]
        # Append the carried factor to the copied list.
        if create_result == False:
            factors.append(carry_factor)
        # If we already know the mappings, append the character instead.
        else:
            factors.append(prime_factors[carry_factor])

        # We have reached the end, return the factors list.
        if pos == len(values):
            return factors

        next_value = values[pos]
        # We could've carried a bad factor earlier because amibiguity.
        if next_value % carry_factor != 0:
            # This was a bad path.
            return []
        # Now get what the next factor is.
        next_factor = next_value//carry_factor
        return try_result(pos + 1, next_factor, factors, create_result)

    # Now with both initial factors, we don't really know which one
    # to start carrying (and there can even be ambiguity), so let's
    # try both paths.

    real_first, real_second = -1, -1
    # Start carrying the first factor.
    l1 = try_result(1, first_factor, [second_factor])
    # Start carrying the second factor.
    l2 = try_result(1, second_factor, [first_factor])
    # One list will come empty, the other won't.
    if len(l1) > len(l2):
        prime_values = list(sorted(set(l1)))
        real_first = first_factor
        real_second = second_factor
    else:
        prime_values = list(sorted(set(l2)))
        real_first = second_factor
        real_second = first_factor

    # Now that for sure we have 26 unique sorted primes, let's map them
    # to characters of the alphabet in increasing order.
    prime_factors = {
        prime_values[i] : chr(ord('A') + i) for i in range(len(prime_values)) 
    }

    # Now the function instead of building a list of primes, will build
    # a list of the characters mapped with the already found primes.
    res = try_result(1, real_first, [prime_factors[real_second]], create_result=True)
    res = "".join(res)

    # Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
    # Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
    print("Case #{}: {}".format(t, res))
