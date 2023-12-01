// https://www.hackerrank.com/challenges/counting-valleys/problem

fun countingValleys(steps: Int, path: String): Int {
    // Hiker always starts and ends at sea level.    
    var elevation = 0
    var valleys = 0
    for (pathStep in path) {
        if (pathStep == 'U') {
            elevation += 1
            // If took one step up and reached elevation 0, means that the
            // hiker has just exited a valley.
            if (elevation == 0) {
                valleys += 1
            }
        }
        if (pathStep == 'D') {
            elevation -= 1
        }
    }
    return valleys
}

fun main(args: Array<String>) {
    val steps = readLine()!!.trim().toInt()

    val path = readLine()!!

    val result = countingValleys(steps, path)

    println(result)
}
