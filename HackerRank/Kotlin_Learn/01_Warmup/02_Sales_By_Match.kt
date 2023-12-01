// https://www.hackerrank.com/challenges/sock-merchant/problem

fun sockMerchant(n: Int, ar: Array<Int>): Int {
    // Convert the array to a list, to then apply a grouping operation
    // and finally do eachCount to get a map of counts.
    val counts = ar
        .toList()
        .groupingBy { it }
        .eachCount()

    // With the map of counts, get the values and divide by two to find
    // the pairs, then add up this number to find the total number of pairs.
    val pairs = counts
        .entries.map { it.value / 2 }
        .sum()

    return pairs
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val ar = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = sockMerchant(n, ar)

    println(result)
}
