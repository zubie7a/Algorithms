# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/8nAgfjhDvKCpxwGWF
def reflectString(input_string):
	# The reflection of a character is taking its alphabetical index
	# and changing the character to another with the same alphabetical
	# index but starting from the end of the alphabet.
    def reflect(char):
        new_pos = ord('z') - ord(char)
        return chr(new_pos + ord('a'))

    return "".join(list(map(reflect, input_string)))
