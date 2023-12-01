// https://www.hackerrank.com/challenges/one-month-preparation-kit-counter-game/problem

fun log2n(n: Double) = Math.log(n) / Math.log(2.0)

// The closest power of two is the log base 2
fun counterGame(n: Long): String {

    // 2^x = y
    // x = log2(y)
    // If x is an integer, then y is a power of 2.
    var number = n.toDouble()
    var turns = 0
    while (number != 1.0) {
        val closestLog2n = log2n(number.toDouble())
        if (Math.ceil(closestLog2n) == Math.floor(closestLog2n)) {
            // Number was a power of 2, all subsequent divisions will be
            // powers of 2, so determine the winner now.
            // e.g. 1073741824
            // 2^30 == 1073741824
            // Why doing 30 more rounds?
                        
            if (turns % 2 == 0) {
                // Louise reached the power of two path.
                if (closestLog2n.toInt() % 2 == 0) {
                    // If the remainding turns are even, Richard wins.
                    return "Richard"
                } else {
                    return "Louise"
                }
            } else {
                // Richard reached the power of two path.
                if (closestLog2n.toInt() % 2 == 0) {
                    // If the remaining turns are even, Louise wins.
                    return "Louise"
                } else {
                    return "Richard"
                }
            }
        } else {
            // Number was not a power of two, so substract closest lower
            // power of 2.
            number -= Math.pow(2.0, Math.floor(closestLog2n))
        }
        
        turns += 1
    }
    
    return if (turns % 2 == 1) {
        "Louise"
    } else {
        "Richard"
    }
}

fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()

    for (tItr in 1..t) {
        val n = readLine()!!.trim().toLong()

        val result = counterGame(n)

        println(result)
    }
}
