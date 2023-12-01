// https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/problem

fun dynamicArray(n: Int, queries: Array<Array<Int>>): Array<Int> {
    // Write your code here

    val arr = Array<ArrayList<Int>>(n, { arrayListOf<Int>() } )
    var lastAnswer = 0
    
    var answers = arrayOf<Int>()

    for ((op, x, y) in queries) {
        val idx = (x xor lastAnswer) % n
        if (op == 1) {
            arr[idx].add(y)
        } else {
            lastAnswer = arr[idx][y % arr[idx].size]
            answers += lastAnswer
        }
    }
    
    return answers
}

fun main(args: Array<String>) {
    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val n = first_multiple_input[0].toInt()

    val q = first_multiple_input[1].toInt()

    val queries = Array<Array<Int>>(q, { Array<Int>(3, { 0 }) })

    for (i in 0 until q) {
        queries[i] = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()
    }

    val result = dynamicArray(n, queries)

    println(result.joinToString("\n"))
}
