# https://app.codesignal.com/company-challenges/mz/jNLxCZe7feQMDvjH4
from math import floor
def resourceCatchUp(log_out, log_in):
    out_ts, out_food = log_out
    in_ts, in_food = log_in
    
    # Let's find the logout hourstamp.
    out_epoch_hours = out_ts//3600 + 1
    # Let's find the login hourstamp.
    in_epoch_hours = in_ts//3600
    # Time in hours that has occurred.
    diff_hours = in_epoch_hours - out_epoch_hours + 1
    diff_food = (out_food - in_food)
    food_rate = diff_food//diff_hours

    return food_rate
