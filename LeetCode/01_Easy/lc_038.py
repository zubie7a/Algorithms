# 038 - Count and Say (Easy)
# https://leetcode.com/problems/count-and-say/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # "1": "11" -> 1 one.
        # "11" : "21" -> 2 ones.
        # "21" : "1211" -> 1 two, 1 one.
        # ...etc.

        def recursive(n):
            # Base case of the recursion.
            if n == 1:
                return "1"

            # Build the character sequence recursively.
            seq_n = recursive(n - 1)

            # To store the counts of consecutive identical characters.
            counts = []
            for char in seq_n:
                # Initialize counts with the first character found.
                if len(counts) == 0:
                    counts.append((char, 1))
                else:
                    # Get the last group of consecutive identical characters.
                    last_char, last_count = counts[-1]
                    # If current character is yet another of the same, update the count.
                    # ... otherwise create a new group from scratch with count one.
                    if char == last_char:
                        counts[-1] = (last_char, last_count + 1)
                    else:
                        counts.append((char, 1))

            result = ""
            # Create a result string where you put the count and the character.
            for (char, count) in counts:
                result += "{}{}".format(count, char)

            return result

        return recursive(n)
