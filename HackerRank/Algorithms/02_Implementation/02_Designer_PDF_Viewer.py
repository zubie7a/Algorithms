# https://www.hackerrank.com/challenges/designer-pdf-viewer
def indexToChar(index):
    return chr(index + ord('a'))
# A list of heights for every lowercase english letter.
heights = map(int, raw_input().split())
# Create a dictionary from character to its height.
heights = {indexToChar(i): heights[i]  for i in range(len(heights)) }
# For a given string, get a list of the heights of its characters.
strHeights = [heights[char] for char in raw_input()]
# When highlighting the word, the area will be its width times the
# height of the tallest character.
print max(strHeights) * len(strHeights)
