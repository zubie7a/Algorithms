// https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem

fun pageCount(n: Int, p: Int): Int {
    // Page 1 starts always at the right.
    // Advancing 1 page makes pages 2,3 visible, then 4,5 and so on.
    // Last page may be on the left or the right depending on book's length.
    // If it's on the right, e.g. 5 then 4,5 are visible right away and then
    // retreating 1 page makes pages 2,3 visible.
    // If it's on the left, e.g. 6, then only 6 is visible, and then retreating
    // one page makes 4,5 visible.
    
    // Pages 2,3 are reachable in one turn from 1.
    // Pages 4,5 are reachable in two turns from 1.
    val fromLeft = p / 2
    // Page 4,5 are reachable in one turn from 6.
    // Page 6 is reachable in zero turns from 6.
    // If last page is even, and the sought page is not the last,
    // then we need at least one extra turn.
    val fromRight = (n - p + (if (n % 2 == 0 && n != p) 1 else 0)) / 2 
    return Math.min(fromLeft, fromRight)
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val p = readLine()!!.trim().toInt()

    val result = pageCount(n, p)

    println(result)
}
