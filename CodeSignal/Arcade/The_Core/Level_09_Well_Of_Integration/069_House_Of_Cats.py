# https://app.codesignal.com/arcade/code-arcade/well-of-integration/RaWLwT2eb96hp4N5Z
def houseOfCats(legs):
    # We have a total number of legs in the house. Cats have four legs, people
    # have two legs, whats the possible amount of people in the house?
    # Perhaps there is no cats!

    # Create a memoization table.
    cache = {}

    def recurse_legs(people, leg_count):
        # Don't recurse further if we had already found a result for this
        # same number of people so far and number of legs left onwards.
        if (people, leg_count) in cache:
            return cache[(people, leg_count)]

        if leg_count == 0:
            # The count of people found so far to make this valid path.
            return [people]
        elif leg_count < 0:
            # Nothing, effectively ignoring an invalid path.
            return []

        # Go one level deeper assuming we found a person.
        arr1 = recurse_legs(people + 1, leg_count - 2)
        # Go one level deeper assuming we found a cat.
        arr2 = recurse_legs(people, leg_count - 4)

        # Store the result for this given number of people so far and
        # this given number of legs onwards.
        cache[(people, leg_count)] = arr1 + arr2

        return cache[(people, leg_count)]

    # The recursion could've found different paths with effectively the same
    # amount of people in different positions, so just get unique occurrences.
    return list(set(recurse_legs(0, legs)))
