# https://app.codesignal.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC
def fileNaming(names):
    # Lets deduplicate names in a given list by putting (k) at their
    # tail to represent a count of how much times the base filename
    # has been previously seen.

    # Dictionary for names that have been seen.
    seen_names = {}
    # Result list for names with additions.
    res = []
    # For each of the names...
    for name in names:
        new_name = ""
        # If the name has already been seen...
        if name in seen_names:
            # Get the possible new name with the count.
            count = seen_names[name]
            new_name = "{}({})".format(name, count)
            # That new name may still be in use, so keep increasing
            # the count until you find an unused one.
            while new_name in seen_names:
                count += 1
                new_name = "{}({})".format(name, count)
            # Mark the unused one as first seen.
            seen_names[new_name] = 1
        # If hasn't been seen, mark it as first seen and then
        # leave it untouched.
        else:
            seen_names[name] = 1
            new_name = name
        res.append(new_name)

    return res
