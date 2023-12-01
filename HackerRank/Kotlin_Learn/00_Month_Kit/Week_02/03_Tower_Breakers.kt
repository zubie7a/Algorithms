// https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem

fun towerBreakers(n: Int, m: Int): Int {
    // If the height is 1, then P1 can't do anything and loses.
    // If the number of towers is odd, P1 wins.
    // If the number of towers is even, P2 wins.
    return if (m == 1) 2 else 2 - (n % 2)
}

fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()

    for (tItr in 1..t) {
        val first_multiple_input = readLine()!!.trimEnd().split(" ")

        val n = first_multiple_input[0].toInt()

        val m = first_multiple_input[1].toInt()

        val result = towerBreakers(n, m)

        println(result)
    }
}
