// https://www.hackerrank.com/challenges/one-month-preparation-kit-new-year-chaos/problem

fun minimumBribes(q: Array<Int>): Unit {
    var bribes = 0
    
    for (index in q.indices) {
        val person = q[index]
        val originalPos = person - 1

        if (originalPos - index > 2) {
            println("Too chaotic")
            return
        }
        
        for(j in Math.max(0, originalPos - 1) until index) {
            if (q.get(j) > q.get(index)) {
                bribes++;
            }
        }
    }
    println(bribes)
}

fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()

    for (tItr in 1..t) {
        val n = readLine()!!.trim().toInt()

        val q = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

        minimumBribes(q)
    }
}
