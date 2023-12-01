// https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem

fun gridChallenge(grid: Array<String>): String {
    // Rearrange the rows so that they are alphabetically ascending.
    val sortedRowsGrid = grid
        .toList()
        .map { 
            it.toCharArray().sorted()
        }

    val rows = sortedRowsGrid.size
    val cols = sortedRowsGrid[0].size
    
    var doubleSorted = true
    // This implicitly handles the 1x1 matrix case which is always sorted
    // in both rows and cols.
    (0 until cols).forEach { col ->
        (1 until rows).forEach { row ->
            if(sortedRowsGrid[row][col] < sortedRowsGrid[row - 1][col]) {
                doubleSorted = false
            }
        }
    }
    
    return if (doubleSorted) "YES" else "NO"
}

fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()

    for (tItr in 1..t) {
        val n = readLine()!!.trim().toInt()

        val grid = Array<String>(n, { "" })
        for (i in 0 until n) {
            val gridItem = readLine()!!
            grid[i] = gridItem
        }

        val result = gridChallenge(grid)

        println(result)
    }
}
