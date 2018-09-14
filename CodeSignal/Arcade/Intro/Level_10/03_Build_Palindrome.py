# https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx
def buildPalindrome(st):
    # Whats the minimum number of characters that can be appended to
    # the end of a string in order to make it a palindrome? At least
    # we know that the max is the whole string except the last element
    # because it can serve as the single individual middle element.
    
    # Reverse the string and omit the first character.
    rev_st = st[::-1][1:]
    # The limit of shifting is the length of the original string itself.
    shift = 0
    for i in range(len(st) + 1):
        concat_str = st + rev_st[i:]
        # If a palindrome is found, store the shifting value. But keep
        # trying as more palindromes with more shifting can be found,
        # and the higher the shifting it means the less characters
        # have to be added. It will always find a match with shifting
        # equal to 0, because of concatenating with the whole string
        # reversed save the last element.
        if concat_str == concat_str[::-1]:
            shift = i

    palindrome = st + rev_st[shift:]
    return palindrome
