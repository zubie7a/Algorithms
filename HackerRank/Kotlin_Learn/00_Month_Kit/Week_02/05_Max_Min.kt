// https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem

fun maxMin(k: Int, arr: Array<Int>): Int {
    // First order the elements
    val sorted = arr.toList().sorted()
    // Now let's do a sliding window with size k. 
    // At both ends of the window will be the minimum and maximum
    // elements of the hypothetical new array, and we'll slide this
    // window until we find what's the minimum difference possible.
    var minUnfairness = sorted[sorted.size - 1] - sorted[0]
    for(index in 0 .. sorted.size - k) {
        val start = sorted[index]
        val end = sorted[index + k - 1]
        minUnfairness = Math.min(end - start, minUnfairness)
    }
    
    return minUnfairness
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val k = readLine()!!.trim().toInt()

    val arr = Array<Int>(n, { 0 })
    for (i in 0 until n) {
        val arrItem = readLine()!!.trim().toInt()
        arr[i] = arrItem
    }

    val result = maxMin(k, arr)

    println(result)
}
