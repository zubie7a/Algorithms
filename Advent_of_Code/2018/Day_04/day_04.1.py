# https://adventofcode.com/2018/day/4
import re

# List of logs to read from STDIN.
logs = []

# test_logs = [
#     ("1518-11-01 00:00", "Guard #10 begins shift"),
#     ("1518-11-01 00:05", "falls asleep"),
#     ("1518-11-01 00:25", "wakes up"),
#     ("1518-11-01 00:30", "falls asleep"),
#     ("1518-11-01 00:55", "wakes up"),
#     ("1518-11-01 23:58", "Guard #99 begins shift"),
#     ("1518-11-02 00:40", "falls asleep"),
#     ("1518-11-02 00:50", "wakes up"),
#     ("1518-11-03 00:05", "Guard #10 begins shift"),
#     ("1518-11-03 00:24", "falls asleep"),
#     ("1518-11-03 00:29", "wakes up"),
#     ("1518-11-04 00:02", "Guard #99 begins shift"),
#     ("1518-11-04 00:36", "falls asleep"),
#     ("1518-11-04 00:46", "wakes up"),
#     ("1518-11-05 00:03", "Guard #99 begins shift"),
#     ("1518-11-05 00:45", "falls asleep"),
#     ("1518-11-05 00:55", "wakes up")
# ]

# Any better way to read until EOF without any clear number of lines?
try:
    while True:
        line = str(input())
        # print(line)
        date, event = map(lambda x: x.strip(), line.split("]"))
        # Remove the starting "[".
        date = date[1:]

        logs.append((date, event))
except Exception:
    # print("EOF")
    None

# Guard ID is the key, then there's another hash which has as keys the 'minute'
# and as values the count of times the guard was asleep at that minute.
guards_to_minutes_asleep = {}

# Since logs are tuples, will sort the timestamps while leaving the event
# unsorted unless there were identical timestamps which the statements
# guarantee there's not since there's only one guard at a given night.
logs = sorted(logs);

i = 0
# Iterate by index until finding a guard, then sub-iterate checking all
# their times they got asleep ~ woke up, stop sub-iterating when you find
# a new guard, then move the outer iterator to that position and repeat.
while i < len(logs):
    log = logs[i]
    date, event = log

    # Check if we found a guard beginning their shift in the logs.
    if re.findall(r'Guard', event):
        guard_num = int(re.findall(r'[0-9]+', event)[0])
        if guard_num not in guards_to_minutes_asleep:
            guards_to_minutes_asleep[guard_num] = {}

        j = i + 1
        asleep_minute = -1
        # Start advancing from current "Guard" until next one or end of logs.
        while j < len(logs):
            next_date, next_event = logs[j]

            if re.findall(r'Guard', next_event):
                break

            # Keep track of the last moment this guard fell asleep.
            if re.findall(r'asleep', next_event):
                cur_minute = int(next_date.split(":")[-1])
                asleep_minute = cur_minute

            # When the guard wakes up, count all individual minutes before
            # this moment and the minute they fell asleep as minutes slept.
            if re.findall(r'wakes', next_event):
                cur_minute = int(next_date.split(":")[-1])
                wokeup_minute = cur_minute
                for i in range(wokeup_minute - asleep_minute):
                    minute_slept = asleep_minute + i
                    if minute_slept not in guards_to_minutes_asleep[guard_num]:
                        guards_to_minutes_asleep[guard_num][minute_slept] = 0

                    guards_to_minutes_asleep[guard_num][minute_slept] += 1

            j += 1
        # Resume regular iteration at the last moment we kept finding logs for
        # previous guard, to not unnecessarily iterate over all those again.
        i = j

# Now that we the count of times each guard has been asleep on individual
# minutes for any midnight, let's use the strategy to determine which guard
# slept the most overall, and on which minute that guard was asleep the most.
guards_to_total_asleep = {}

# Aggregate the count of times a guard was asleep on any given minute.
for guard in guards_to_minutes_asleep.keys():
    total = 0
    for minutes in guards_to_minutes_asleep[guard].keys():
        total += guards_to_minutes_asleep[guard][minutes]
    guards_to_total_asleep[guard] = total

# Put the map into inverse tuples we can sort by value (total minutes asleep)
# while preserving the original key.
inverse_tuples = [ (v, k) for k, v in guards_to_total_asleep.items()]
most_sleepy_guard = sorted(inverse_tuples)[-1][-1]

# Now find the minute this guard was asleep the most.
# Tuple consist of the minute, and the count of times asleep in that minute.
most_minute_asleep = (-1, -1)
for minute, count in guards_to_minutes_asleep[most_sleepy_guard].items():
    max_count = most_minute_asleep[1]
    if count > max_count:
        most_minute_asleep = (minute, count)

# Multiply the ID of the guard by the individual minute they were asleep the most.
# Result: 85296.
print(most_minute_asleep[0] * most_sleepy_guard)
