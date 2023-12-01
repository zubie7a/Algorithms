// https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem

fun birthday(s: Array<Int>, d: Int, m: Int): Int {
    // s = [2, 2, 1, 3, 2]
    // d = 4
    // m = 2
    // Find how many continuous segments of length m sum up to d.
    // For this create a moving window and store the sum.
    // Then at every time the window is moved to the right, substract
    // the value from the start, and add the new value found.
    
    // If the segment length is longer than the original array,
    // then this division is not possible.
    if (m > s.size) {
        return 0
    }

    var possibleDivisions = 0
    // Start with summing the segment starting at position 0.
    var sumSegment = (0 until m).map { s[it] }.sum()   
 
    var index = m
    // Now start advancing the window
    while (index < s.size) {
        if (sumSegment == d) {
            possibleDivisions += 1
        }
        
        // Add the new value found to the right.
        sumSegment += s[index]
        // Substract the first value to the left.
        sumSegment -= s[index - m]
        
        index++
    }
    
    // When window is at the end of the array.
    if (sumSegment == d) {
        possibleDivisions += 1
    }
    
    return possibleDivisions
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val s = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val d = first_multiple_input[0].toInt()

    val m = first_multiple_input[1].toInt()

    val result = birthday(s, d, m)

    println(result)
}
