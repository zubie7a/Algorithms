# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/pdw3izd7SpMTBJqSy
def pagesNumberingWithInk(current_page, number_of_digits):
    # You are on a current page, and you want to print its digits, and those
    # of the pages afterwards, but you only have ink left for a certain amount
    # of digits. Whats the last page of the book that you can print its digits?

    while number_of_digits >= 0:
        number_of_digits -= len(str(current_page))
        current_page += 1

    # The last page you weren't able to print.
    return current_page - 2
