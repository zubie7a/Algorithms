# https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg
def electionsWinners(votes, k):
    max_votes = max(votes)
    # No votes left, lets tally votes and find winner (or none).
    # There must be at most one person with the max number of votes.
    if k == 0:
        top = list(filter(lambda x: x == max_votes, votes))
        if len(top) == 1:
            # A single winner was found.
            return 1
        else:
            # No winners, there's a draw at the top.
            return 0
    else:
        # Add to everyone their potential votes. If someone doesn't
        # beat current leader with all remaining votes added to them,
        # then they have no chances to win.
        winners = [candidate_votes + k > max_votes for candidate_votes in votes]

        return sum(winners)
