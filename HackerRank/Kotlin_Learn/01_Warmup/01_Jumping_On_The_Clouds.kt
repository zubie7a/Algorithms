// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

fun jumpingOnClouds(c: Array<Int>): Int {
    // Write your code here
    var pos = 0
    var jumps = 0
    while (pos < c.size - 1) {
        // Look one position ahead
        val jump1 = c[pos + 1]
        // Look two positions ahead, but be careful if already
        // near the end of the array, in this case assume after
        // the end it's a position not good to jump to.
        val jump2 = if (pos + 2 < c.size) c[pos + 2] else 1
        pos += if (jump2 == 0) 2 else 1
        jumps += 1 
    }
    return jumps
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val c = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = jumpingOnClouds(c)

    println(result)
}
