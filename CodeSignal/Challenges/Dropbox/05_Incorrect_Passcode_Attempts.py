# https://app.codesignal.com/company-challenges/dropbox/ffibMFaS7mzKZkAE3
def incorrectPasscodeAttempts(passcode, attempts):
    counter = 0
    # Check if the account should be locked. During the day a certain group
    # of attempts were done. The account will be locked when there's 10
    # consecutive attempts, but any single successful entry will reset
    # the count of attempts.
    for attempt in attempts:
        if passcode != attempt:
            counter += 1
        else:
            counter = 0
        if counter >= 10:
            return True

    return False
