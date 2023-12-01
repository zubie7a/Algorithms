// https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem

fun countingSort(arr: Array<Int>): Array<Int> {
    // Initialize an array of size 0 with all positions 0
    // The value of each element is max 100.
    val counts = Array<Int>(100, { 0 })
    
    // For each element in the input array increase the count.
    arr.toList().forEach {
        counts[it]++
    }
    
    return counts
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = countingSort(arr)

    println(result.joinToString(" "))
}
