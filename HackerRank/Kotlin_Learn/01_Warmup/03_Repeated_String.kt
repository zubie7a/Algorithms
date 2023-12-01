// https://www.hackerrank.com/challenges/repeated-string/problem

fun repeatedString(s: String, n: Long): Long {
    // String s will have at most length 100.
    // n will be at most 10^12, a very large number, 
    // but for 25% of the test cases n is at most 10^6.
    
    // Find the count of 'a' in the base string.
    val countChars = s.groupingBy { it }.eachCount()
    val countA = countChars.getOrDefault('a', 0)

    // Then find how much times does the base string fit
    // in n length.
    val repeated = n / s.length

    // If it doesn't fit exactly, it will be partially covered,
    // so find up to which point, and find how many 'a' happens
    // until that point.
    val remainder = n % s.length
    val countCharsPartial = s.substring(0, remainder.toInt())
        .groupingBy { it }
        .eachCount()
    val countAPartial = countCharsPartial.getOrDefault('a', 0)
    
    // The total amount of the complete repeated string + the partial amount.
    return (countA * repeated) + countAPartial
}

fun main(args: Array<String>) {
    val s = readLine()!!

    val n = readLine()!!.trim().toLong()

    val result = repeatedString(s, n)

    println(result)
}
