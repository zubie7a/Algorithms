// https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/problem


fun balancedSums(arr: Array<Int>): String {
    // Need to find a point in the array where the sum of all elements
    // to the left is equal to the sum of all elements to the right,
    // if it exists.
    
    // For this, create a new array where you'll store at each point
    // the cumulative sum up to that point. Then iterate over that array,
    // and you'll find out easily the cumulative sum to the right by
    // substracting the cumulative sum up to that point from the cumulative
    // sum until the end of the array.

    var acumArray = Array<Int>(arr.size, { 0 })
    for (index in arr.indices) {
        acumArray[index] = arr[index]
        if (index > 0) {
            acumArray[index] += acumArray[index - 1]
        }
    }
    // Now go over the acum array and check the sums to the left and the right
    // of each element
    for (index in 0 until arr.size) {
        // This case can happen: 2 0 0 0 which starting at 2 the sum to left is 0.
        // This loop handles implicitly the case where array has a single element.
        val acumLeft = if (index > 0) {
            acumArray[index - 1]
        } else {
            0
        }

        val acumRight = acumArray[arr.size - 1] - acumArray[index]

        if (acumLeft == acumRight) {
            return "YES"
        }
    }
    
    return "NO"
}

fun main(args: Array<String>) {
    val T = readLine()!!.trim().toInt()

    for (TItr in 1..T) {
        val n = readLine()!!.trim().toInt()

        val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

        val result = balancedSums(arr)

        println(result)
    }
}
