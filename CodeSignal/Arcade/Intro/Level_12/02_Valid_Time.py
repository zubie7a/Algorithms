# https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5
def validTime(time):
    hh, mm = time.split(":")

    return int(hh) < 24 and int(mm) < 60
