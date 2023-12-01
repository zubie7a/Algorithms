// https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem

fun timeConversion(s: String): String {
    
    // "07", "05", "45PM"
    val hourParts = s.split(":")
    val hours = if (hourParts[2].contains("PM")) {
        if (hourParts[0] == "12") {
            "12"
        } else {
            (hourParts[0].toInt() + 12).toString()
        }
    } else {
        if (hourParts[0] == "12") {
            "00"
        } else {
            hourParts[0]
        }
    }
    
    return hours + ":" + hourParts[1] + ":" + hourParts[2].slice(0..1)
}

fun main(args: Array<String>) {
    val s = readLine()!!

    val result = timeConversion(s)

    println(result)
}
