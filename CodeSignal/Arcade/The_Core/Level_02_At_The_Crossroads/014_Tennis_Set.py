# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/7jaup9HprdJno2diw
def tennisSet(score1, score2):
    # Determine whether the current finished tennis set scores are valid.
    score1, score2 = max(score1, score2), min(score1, score2)
    # Set finishes if one player reaches 6 and the other has less than 5.
    # If both players made at least 5, then can only end 7-5 or 7-6.
    # There's no way for a set to end with 7 on one side and less than 5 in other.
    return (score1 == 6 and score2 < 5) or (score1 == 7 and score2 in [5, 6])
