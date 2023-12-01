// https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem

fun flippingBits(n: Long): Long {
    // Long is signed. If doing `inv` then the sign bit
    // is also flipped. In the problem statement it's 32 bit
    // unsigned integers, which Long can represent.
    // Need to convert to UInt, invert (making sure the sign
    // isn't flipped) and then convert back to Long.
    return (n.toUInt()).inv().toLong()
}

fun main(args: Array<String>) {
    val q = readLine()!!.trim().toInt()

    for (qItr in 1..q) {
        val n = readLine()!!.trim().toLong()

        val result = flippingBits(n)

        println(result)
    }
}
