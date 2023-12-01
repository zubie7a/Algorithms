// https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem

fun miniMaxSum(arr: Array<Int>): Unit {
    // First sum together all values.
    // Beware of integer overflow! Use long.
    val allSum = arr.toList().map { it.toLong() }.sum()
    var minSum = allSum
    var maxSum = 0L
    arr.toList().forEach {
        // Now substract from the total sum one element at a time
        // and then try to store that in the min and/or max vars.
        minSum = Math.min(minSum, allSum - it.toLong())
        maxSum = Math.max(maxSum, allSum - it.toLong())
    }
    
    println("$minSum $maxSum")
}

fun main(args: Array<String>) {

    val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    miniMaxSum(arr)
}
