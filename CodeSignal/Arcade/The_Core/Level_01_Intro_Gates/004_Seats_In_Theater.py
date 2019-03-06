# https://app.codesignal.com/arcade/code-arcade/intro-gates/bszFiQAog96G9CXKg
def seatsInTheater(n_cols, n_rows, col, row):
    # You are at (row, col) and you want to exit the theater but the exit
    # is at the left of your row. If you stand up you'll block the viewing
    # of your row and all other rows until the exit. How much people's view
    # will be blocked once you start leaving?
    #
    # Need information about theater layout:
    #     * Columns count from left to right.
    #     * Rows count from bottom to top.
    #     * The screen is at the bottom.
    #     * Exit to the "left" is at the right with bottom screen.
    #     * The blocked people is the top-right corner.
    return (n_cols - col + 1) * (n_rows - row)
