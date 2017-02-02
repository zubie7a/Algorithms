# https://www.hackerrank.com/challenges/finding-the-percentage
if __name__ == "__main__":
    n = int(raw_input())
    students = {}
    # Get students with grades for maths, physics, chemistry, store their avg.
    for i in range(n):
        line = raw_input().split()
        name = line[0]
        scores = map(float, line[1:])
        avg = sum(scores) / 3
        students[name] = avg
    # Print the avg for a queried student name.
    query = raw_input()
    print "%.2f" % students[query]
