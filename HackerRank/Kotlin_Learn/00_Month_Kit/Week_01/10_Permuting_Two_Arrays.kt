// https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem

fun twoArrays(k: Int, A: Array<Int>, B: Array<Int>): String {
    // STDIN       Function
    // -----       --------
    // 2           q = 2
    // 3 10        A[] and B[] size n = 3, k = 10
    // 2 1 3       A = [2, 1, 3]
    // 7 8 9       B = [7, 8, 9]
    // 4 5         A[] and B[] size n = 4, k = 5
    // 1 2 2 1     A = [1, 2, 2, 1]
    // 3 3 3 4     B = [3, 3, 3, 4]
    
    val sortedA = A.toList().sorted()
    val reverseSortedB = B.toList().sorted().reversed()
    
    val zippedAB = sortedA.zip(reverseSortedB) { a, b -> Pair(a, b) }
    
    val possible = zippedAB.all {
        it.first + it.second >= k
    }

    return if (possible) {
        "YES"
    } else {
        "NO"
    }
    
}

fun main(args: Array<String>) {
    val q = readLine()!!.trim().toInt()

    for (qItr in 1..q) {
        val first_multiple_input = readLine()!!.trimEnd().split(" ")

        val n = first_multiple_input[0].toInt()

        val k = first_multiple_input[1].toInt()

        val A = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

        val B = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

        val result = twoArrays(k, A, B)

        println(result)
    }
}
