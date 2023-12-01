// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

fun rotLeft(a: Array<Int>, d: Int): Array<Int> {
    // The size of the array is 1 <= n <= 10^5
    // The number of rotations is 1 <= d <= n
    // The value at each position is 1 <= a[i] <= 10^6
    val n = a.size
    
    // This won't be a negative value because 1 <= d <= n
    // e.g. n = 5, d = 4, so the start of the current array
    // will now be moved to position 1.
    // n = 5, d = 4, "1 2 3 4 5" -> "5 1 2 3 4"
    val newStartingPos = n - d

    val rotated = a.toList().slice(n - newStartingPos until n) + 
        a.toList().slice(0 until n - newStartingPos)
    
    return rotated.toTypedArray()
}

fun main(args: Array<String>) {
    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val n = first_multiple_input[0].toInt()

    val d = first_multiple_input[1].toInt()

    val a = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = rotLeft(a, d)

    println(result.joinToString(" "))
}
