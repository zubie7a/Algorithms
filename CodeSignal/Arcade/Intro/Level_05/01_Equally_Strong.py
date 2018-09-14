# https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL
def areEquallyStrong(your_left, your_right, friends_left, friends_right):
    # Two arms are equally strong if the heaviest weights they each are
    # able to lift are equal. Two people are equally strong if their
    # strongest arms are equally strong and so are their weakest arms.
    my_max = max(your_left, your_right)
    my_min = min(your_left, your_right)
    fr_max = max(friends_left, friends_right)
    fr_min = min(friends_left, friends_right)

    # Check if me and my friend are equally strong!
    return my_max == fr_max and my_min == fr_min

