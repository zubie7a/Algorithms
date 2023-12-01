// https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-valid-string/problem

fun isValid(s: String): String {
    // "abc" => {a: 1, b: 1, c: 1}
    // the string is valid right away 
    // "abcc" => {a: 1, b: 1, c: 2}
    // if 'c' is removed then result is "abc" valid
    // "aabbc" => {a: 2, b: 2, c: 1}
    // if 'c' is removed then result is "aabb" valid
    // "abcddee" => {a: 1, b: 1, c: 1, d: 2, e: 2}
    // this string is not valid in any case

    // Count the unique characters in the string
    val charCounts = s.groupingBy { it }.eachCount()
    
    // Now count how many times a count of characters appear
    // e.g. {a: 1, b: 1, c: 2} => {1: 2, 2: 1}
    val countOfCounts = charCounts.values.groupingBy { it }.eachCount()

    // If the map has a single element, then all characters occurred
    // the same amount of times.
    if (countOfCounts.values.size == 1) {
        return "YES"
    } else if (countOfCounts.values.size == 2) {
        // Special case can occur if there's a certain character where
        // removing it would leave a string where all characters have
        // the same count.
        val (countA, countB) = countOfCounts.keys.toList().sorted()
        // {1: 2, 2: 1}
        // 1: 2 -> characters that appear 1 time occur 2 times in the string
        // 2: 1 -> characters that appear 2 times occur 1 time in the string
        
        // This is when the odd group is one bigger than the common group, so
        // removing that extra element will make all groups the same length.
        if (countA + 1 == countB && countOfCounts[countB] == 1) {
            return "YES"
        }
        // This is when the odd group has a single element, this means removing
        // it will make the string valid because the rest of elements appear
        // the same amount of times.
        else if (countOfCounts[1] == 1) {
            return "YES"
        } else {
            return "NO"
        }
    } else {
        return "NO"
    }
}

fun main(args: Array<String>) {
    val s = readLine()!!

    val result = isValid(s)

    println(result)
}
