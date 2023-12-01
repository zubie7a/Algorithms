// https://www.hackerrank.com/challenges/one-month-preparation-kit-recursive-digit-sum/problem

fun superDigit(n: String, k: Int): Int {
    // n = "9875"
    // k = 4
    // The superdigit is the reduction of a string by summing
    // its digits, 9875 -> 29 -> 11 -> 2
    // If the string is to be concatenated k times, e.g.
    // "987598759875" one does not need to do the superdigit
    // for the whole string, finding it for the base string is enough
    // and then multiply that by k and then find superdigit for that
    // result.
    
    // Remember function arguments are `val`.
    var baseString = n
    while (baseString.length > 1) {
        baseString = (baseString.map { it.code - '0'.code }.sum()).toString()
    }
    
    // One recursion for k > 1, because multiplying the superdigit of the
    // segment by k may give a result that's again not a superdigit.
    return if (k > 1) {
        superDigit(
            (baseString.toInt() * k).toString(),
            1
        )
    } else {
        baseString.toInt()
    }
}

fun main(args: Array<String>) {
    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val n = first_multiple_input[0]

    val k = first_multiple_input[1].toInt()

    val result = superDigit(n, k)

    println(result)
}
