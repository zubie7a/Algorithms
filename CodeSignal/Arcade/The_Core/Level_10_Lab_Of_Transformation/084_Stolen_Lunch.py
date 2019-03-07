# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/M97sbwRp3tGy8uAb8
def stolenLunch(note):
    # There's a note which has all [0-9] digits replaced to the characters in the same
    # alphabet location [a-j], and such characters replaced by those same digits.
    # We need to translate this note back.
    #
    # Create a table which holds mappings between digits [0-9] and the respective chars.
    table_a = { str(i) : chr(i + ord('a')) for i in range(10) }
    table_b = {}
    # Create a temporary table with the values flipped around.
    for k, v in table_a.items():
        table_b[v] = k
    # Merge the temporary table so we now have a single table with bidirectional mappings.
    table_a.update(table_b)

    # Substitute the mapped characters to the original ones.
    res = [char if char not in table_a else table_a[char] for char in note]
    # return "".join(res)

    # From another user solution, this is a very neat trick to do a
    # character translation~substitution.
    digits = "0123456789"
    alphas = "abcdefghij"
    # Creates a translation from "0123456789abcdefghij" to "abcdefghij0123456789".
    tr = str.maketrans(digits + alphas, alphas + digits)

    return note.translate(tr)
