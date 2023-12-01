// https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem

fun pangrams(s: String): String {
    // Convert to lowercase to not have to deal with both cases.
    // Remove whitespaces too so that all that's left is letters.
    val cleanedString = s.lowercase().replace(" ", "")
    // Group and count the characters in the string.
    val letterCounts = cleanedString
        .groupingBy { it }
        .eachCount()
    
    // We can assume this due to removing whitespaces and lowering the
    // case, from statement there won't be other kinds of characters.
    return if(letterCounts.keys.size == 26) {
        "pangram"
    } else {
        "not pangram"
    }
}

fun main(args: Array<String>) {
    val s = readLine()!!

    val result = pangrams(s)

    println(result)
}
