# https://app.codesignal.com/arcade/code-arcade/book-market/G9wj2j6zaWwFWsise
def isCaseInsensitivePalindrome(input_string):
    # Check if word is a palindrome ignoring casing.
    word = input_string.lower()
    return word == word[::-1]
