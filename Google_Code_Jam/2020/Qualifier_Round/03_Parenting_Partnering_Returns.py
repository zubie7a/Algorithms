# 03 - Parenting Partening Returns

# Scheduling kid activities and domestic necesities is a challenge for a couple
# parents of a 3 year old child. They have a list of N activities to take care
# during the day, each activity happens during a specified interval in the day.

# Thet need to assign each activity to any of the parents, so that neither of
# them is responsible of 2 activities that overlap. An activity that ends at
# time t is not considered to overlap with an activity that starts at time t.

# The parents names are Jamie and Cameron. Output who will do each activity
# from the given input in a way that someone doesn't have to do two activities
# that overlap, or show that it's impossible if there's no arrangement for it.

num_cases = int(input())
for t in range(1, num_cases + 1):
    # The number of activities to perform per test case.
    n = int(input())
    # An array to hold the input activities.
    activities = []
    for i in range(n):
        # Input is two values, starting and ending minute in the day.
        # Convert into a list the starting and ending minute.
        activity = list(map(lambda x: int(x), input().split(" ")))
        # Append the index of the current activity as given in input, since
        # we'll sort this list, it's so that we are able to restore the original
        # order of activities as given.
        activity.append(i)
        # Append a partner by default to handle all activities.
        activity.append("C")
        # Now add this activity to the list of activities.
        activities.append(activity)

    activities = sorted(activities)
    
    # Keep track of the most recent activity assigned to each parent.
    c_last_activity, j_last_activity = activities[0], []
    possible = True

    # Check activities pair by pair as their real order in the day is.
    for i in range(0, len(activities) - 1):
        cur_activity  = activities[i]
        next_activity = activities[i + 1]

        # Compare an activity with the one chronologically coming after it.
        cur_ends = cur_activity[1]
        next_starts = next_activity[0]

        # This means that another parent has to do it.
        if next_starts < cur_ends:
            cur_parent = cur_activity[3]
            # Given the parent of the current activity that overlaps with the
            # next activity, try to reassign the next activity to the other.
            # If the other already has an activity that overlaps with next,
            # then it's impossible.
            if cur_parent == "C":
                # Try to give next activity to "J".
                # If "J" didn't already have an activity, give them next.
                if len(j_last_activity) != 0:
                    j_last_ends = j_last_activity[1]
                    if next_starts < j_last_ends:
                        # It's impossible because neither can take it.
                        possible = False
                        break
                # If it's possible to give "J" the next activity, just give it.
                next_activity[3] = "J"
                j_last_activity = next_activity
                activities[i + 1] = next_activity
            elif cur_parent == "J":
                # Try to give next activity to "C"
                c_last_ends = c_last_activity[1]
                if next_starts < c_last_ends:
                    # It's impossible because neither can take it.
                    possible = False
                    break
                next_activity[3] = "C"
                c_last_activity = next_activity
                activities[i + 1] = next_activity
        else:
            # If there's no overlap between current pair... See that there's no
            # overlap with last "C" and last "J"
            cur_parent = cur_activity[3]
            c_last_ends = c_last_activity[1]
            if next_starts < c_last_ends:
                # Try giving it to "J".
                j_last_ends = j_last_activity[1]
                if next_starts < j_last_ends:
                    # Neither "J" can take it, so it's impossible.
                    possible = False
                    break
                next_activity[3] = "J"
                j_last_activity = next_activity
                activities[i + 1] = next_activity
            else:
                # Remember to update "C" last activity!
                c_last_activity = next_activity

    original_order = sorted(activities, key=lambda activity: activity[2])
    parents_result = [activity[3] for activity in original_order]
    result_string = "".join(parents_result)
    if not possible:
        result_string = "IMPOSSIBLE"

    print("Case #{}: {}".format(t, result_string))
