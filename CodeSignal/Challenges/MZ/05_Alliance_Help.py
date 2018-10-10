# https://app.codesignal.com/company-challenges/mz/mrXdvJsEmBxQvraRo
def allianceHelp(t, alliance_size):
    # Given initial t seconds it takes to build the military academy,
    # and a given number of alliance_size, determine how long it will
    # take to build it considering each member of the alliance can
    # give you a boost of 10% of initial construction time or 1 minute
    # (whichever is greater).

    # There's a limit of 10 boosts, so no matter your alliance size,
    # the boost times caps at 10.
    alliance_size = min(alliance_size, 10)
    time = t
    for i in range(alliance_size):
        # Time will potentially decrease to 1/10th.
        time_decreased = t//10
        # But if that's less than 1min~60sec, bump it up.
        time_decreased = max(time_decreased, 60)
        # Reduce the time it takes by that amount.
        time -= time_decreased
    # If it takes a negative time, then make it 0 and it will be build
    # immediately.
    time = max(time, 0)

    return time
