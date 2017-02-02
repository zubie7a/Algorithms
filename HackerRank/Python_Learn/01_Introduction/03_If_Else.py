# https://www.hackerrank.com/challenges/py-if-else
def main():
    n = int(raw_input())
    if n % 2 or (n >= 6 and n <= 20):
        print "Weird"
    else:
        print "Not Weird"

if __name__ == '__main__':
    main()
