// https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem

fun diagonalDifference(arr: Array<Array<Int>>): Int {
    // The matrix is square
    val diag1Sum = (0 until arr.size).map { arr[it][it] }.sum()
    val diag2Sum = (0 until arr.size).map { arr[arr.size - it - 1][it] }.sum()
    return Math.abs(diag1Sum - diag2Sum)
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val arr = Array<Array<Int>>(n, { Array<Int>(n, { 0 }) })

    for (i in 0 until n) {
        arr[i] = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()
    }

    val result = diagonalDifference(arr)

    println(result)
}
