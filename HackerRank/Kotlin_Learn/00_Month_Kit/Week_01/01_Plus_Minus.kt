// https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem
 
fun plusMinus(arr: Array<Int>): Unit {
    var positive = 0
    var negative = 0
    var zero = 0
    for (num in arr) {
        if (num > 0) {
            positive++
        } else if (num < 0) {
            negative++
        } else {
            zero++
        }
    }
    
    println("%.6f".format(positive.toDouble() / arr.size))
    println("%.6f".format(negative.toDouble() / arr.size))
    println("%.6f".format(zero.toDouble() / arr.size))
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    plusMinus(arr)
}
