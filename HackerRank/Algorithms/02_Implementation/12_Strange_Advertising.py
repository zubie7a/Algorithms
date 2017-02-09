# https://www.hackerrank.com/challenges/strange-advertising
n = int(raw_input())
# Start advertising to 5 people.
people, likes = 5, 0
for i in range(n):
    # Only half of the people will like the ad. Ignore the
    # people who didn't like it.
    people /= 2
    # Add to the total of people so far who has liked the ad.
    likes += people
    # Of the people who liked it, they will spread it to
    # three of their friends.
    people *= 3
# The total cumulative amount of people who liked the ad.
print likes
