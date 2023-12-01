// https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

fun caesarCipher(s: String, k: Int): String {
    val encoded = s.map {
        // Do nothing with non-alphabetic characters.
        if (!it.isLetter()) {
            it
        } else {
            // Now handle the alphabetic characters.
            val pos = if(it.isUpperCase()) {
                // Do this to convert from ASCII code to alphabet index.
                it.code - 'A'.code
            } else {
                it.code - 'a'.code
            }
            val newPos = (pos + k) % 26
            if (it.isUpperCase()) {
                // To this to convert back from alphabet index to char.
                ('A'.code + newPos).toChar()
            } else {
                ('a'.code + newPos).toChar()
            }
        }
    }
    
    return encoded.joinToString("")
}

fun main(args: Array<String>) {
    val n = readLine()!!.trim().toInt()

    val s = readLine()!!

    val k = readLine()!!.trim().toInt()

    val result = caesarCipher(s, k)

    println(result)
}
