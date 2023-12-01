// https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem

fun matchingStrings(strings: Array<String>, queries: Array<String>): Array<Int> {
    // Strings contains a list of strings which may be repeated.
    val inputCounts = strings
        .toList()
        .groupingBy { it }
        .eachCount()
        
    // Queries contains certain strings that we want to find how many times
    // do they occurr in the original input list.
    val result = queries
        .toList()
        .map { inputCounts.getOrDefault(it, 0) }
        .toTypedArray()
    
    return result
}

fun main(args: Array<String>) {
    val stringsCount = readLine()!!.trim().toInt()

    val strings = Array<String>(stringsCount, { "" })
    for (i in 0 until stringsCount) {
        val stringsItem = readLine()!!
        strings[i] = stringsItem
    }

    val queriesCount = readLine()!!.trim().toInt()

    val queries = Array<String>(queriesCount, { "" })
    for (i in 0 until queriesCount) {
        val queriesItem = readLine()!!
        queries[i] = queriesItem
    }

    val res = matchingStrings(strings, queries)

    println(res.joinToString("\n"))
}
