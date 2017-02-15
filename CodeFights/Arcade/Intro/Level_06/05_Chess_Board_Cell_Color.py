# https://codefights.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
def chessBoardCellColor(cell1, cell2):
    c1x, c1y = cell1[0], cell1[1]
    c2x, c2y = cell2[0], cell2[1]
    c1x = ord(c1x) - ord('A') + 1
    c2x = ord(c2x) - ord('A') + 1
    c1y, c2y = int(c1y), int(c2y)
    # Black: both coordinates odd or both even.
    # White: coordinates are mixed both and even.
    def color(x, y):
        return "black" if x % 2 == y % 2 else "white"
    return color(c1x, c1y) == color(c2x, c2y)
