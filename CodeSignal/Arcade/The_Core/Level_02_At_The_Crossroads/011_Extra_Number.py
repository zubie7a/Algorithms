# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/sgDWKCFQHHi5D3Szj
def extraNumber(a, b, c):
    # You have 3 integers, a, b, and c. Two of them are equal to each other,
    # what is the third value?
    set_nums = set([])
    for num in [a, b, c]:
        # The repeated number won't be added to the set, plus its previous occurrence
        # will be deleted.
        if num in set_nums:
            set_nums.remove(num)
        else:
            set_nums.add(num)

    # The only value remaining at the end will be the unique value.
    return list(set_nums)[0]
