# https://app.codesignal.com/arcade/code-arcade/well-of-integration/8RiRRM3yvbuAd3MNg
def electionsWinners(votes, k):
    # Given an array of votes for each i-th candidate, and a number k of
    # still undecided votes, find out how much candidates can still win
    # the elections.
    lead_candidate = max(votes)
    # Edge case where there's no votes left, check if there's only one winner.
    if k == 0:
        winners = list(filter(lambda x: x == lead_candidate, votes))
        return 1 if len(winners) == 1 else 0

    # If there's votes left, try adding all of them to each of the candidates
    # and figure out if they can outbest the current lead.
    can_win = list(filter(lambda x: x + k > lead_candidate, votes))
    return len(can_win)
