// https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem

fun lonelyinteger(a: Array<Int>): Int {
    val countOccurrences = a.toList().groupingBy { it }.eachCount()
    // Per problem statement, it's guaranteed there's one unique element.
    val result = countOccurrences.keys.find { countOccurrences[it] == 1 }!!
    return result 
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val a = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = lonelyinteger(a)

    println(result)
}
