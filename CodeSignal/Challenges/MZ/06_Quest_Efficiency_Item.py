# https://app.codesignal.com/company-challenges/mz/zCYv3tuxRE4JajQNY
def questEfficiencyItem(hours, points, time_for_quests):
    # Time is short, you want to complete as many quests as possible
    # but it's difficult to do so. So we want to maximize the points
    # we can obtain with quests in a given limited time.
    # hours: hours it takes to complete a quest
    # points: points each quest gives you
    # time_for_quests: the limit of time to do stuff.

    # Recursively, at each position, decide whether to take this quest
    # or not. This 'iteration' can be done since the order of the quests
    # doesn't matter so you can check from left to right whether to take
    # each one or not, generating unique combinations.
    def recursive(idx, score_acum, time_left):
        # Time ran out, acum with last step is invalid.
        if time_left < 0:
            return 0
        # Time was precise, return until here.
        if time_left == 0:
            return score_acum
        # Ran out of quests to 
        if idx == len(hours):
            return score_acum

        score = 0
        hours_idx = hours[idx]
        points_idx = points[idx]
        # At each position decide whats better, whether to consume it or
        # advance to the next without consuming current.
        res_1 = recursive(idx + 1, score_acum + points_idx, time_left - hours_idx)
        res_2 = recursive(idx + 1, score_acum, time_left)
        return max(res_1, res_2)

    # Start with 0 accumulated points and all the time left.
    return recursive(0, 0, time_for_quests)
