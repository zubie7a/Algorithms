# https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
def chessBoardCellColor(cell1, cell2):
    def color(cell):
        # Each 'cell' is a 2-char string with a letter and a number.
        # The char indicates the columns (A-H), the number the rows (1-8).
        # Convert the alphabetic position to the respective numerical index.
        coor_x = int(ord(cell[0]) - ord('A') + 1)
        # Just parse as int the already numerical position.
        coor_y = int(cell[1])
        # Distribution of colors in a chess board...
        # Black: both coordinates odd or both even.
        # White: coordinates are mixed both and even.
        return "black" if coor_x % 2 == coor_y % 2 else "white"

    return color(cell1) == color(cell2)
