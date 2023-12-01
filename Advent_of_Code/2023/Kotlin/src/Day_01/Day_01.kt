fun main() {

    fun parseContents(input: List<String>): List<Int> {
        val numbers = input.map {
            val row = it.filter { char ->
                // Filter out non-digit characters
                char.isDigit()
            }.fold("") {
                // Concatenate all the digits filtered.
                acc, elem -> acc + elem
            }

            // Get the first digit and last digit and convert to int.
            // It could be the case that first and last are the same!
            (row.first() + "" + row.last()).toInt()
        }

        return numbers
    }

    fun part1(input: List<String>): Int {
        return parseContents(input).sum()
    }

    // A function to naively find all indexes of a word inside
    // a source string.
    fun findAllIndexes(source: String, word: String): List<Int> {
        val indexes = mutableListOf<Int>()
        var startIndex = 0
        while(true) {
            startIndex = source.indexOf(word, startIndex)
            // If word is not found, then the returned index is -1.
            if (startIndex == -1) {
                break
            } else {
                indexes.add(startIndex)
                startIndex += 1
            }
        }
        return indexes
    }

    fun part2(input: List<String>): Int {
        // Example: "zoneight234"
        // Here there is 1, 8 written in letters (even if overlapping)
        // then regular digits 2, 3, 4, so the "digits" are 1, 8, 2, 3, 4

        // Example: "oneight" - the digits are 1, 8.
        // At first, I thought of naively substituting words for digits, but this
        // would result in "1ight", losing the "e" from eight.

        val wordDigits = mapOf(
            "one" to 1, "two" to 2, "three" to 3,
            "four" to 4, "five" to 5, "six" to 6,
            "seven" to 7, "eight" to 8, "nine" to 9
        )

        val transformedInput = input.map { row ->
            // We only really care about the first wordDigit found
            // and the last one, the ones occurring in the middle of
            // the word have no impact on the end result.

            // Use this to store the first and last wordDigits occurring
            // in the row, together with the index in which they occur.
            var lowestPair = Pair("", row.length + 1)
            var highestPair = Pair("", -1)

            wordDigits.keys.map { wordDigit ->
                val indexes = findAllIndexes(row, wordDigit)
                // If a word digit is found inside the row...
                if (indexes.isNotEmpty()) {
                    val max = indexes.max()
                    val min = indexes.min()
                    // Update the lowest and highest pair of wordDigit and index.
                    if (min < lowestPair.second) {
                        lowestPair = Pair(wordDigit, min)
                    }
                    if (max > highestPair.second) {
                        highestPair = Pair(wordDigit, max)
                    }
                }
            }

            if (lowestPair.first != "") {
                // Build a new row where the positions of the first word-digit
                // found and the last word-digit found are used to insert the
                // actual digits.

                // Original row: 6three2sixsix9eightfour
                // Lowest wordDigit: (three, 1)
                // Highest wordDigit: (four, 19)
                // Row with lowest and highest wordDigits inserted: 63three2sixsix9eight4four
                row.subSequence(0, lowestPair.second).toString() +
                        wordDigits[lowestPair.first] +
                        row.subSequence(lowestPair.second, highestPair.second).toString() +
                        wordDigits[highestPair.first] +
                        row.subSequence(highestPair.second, row.length).toString()
            } else {
                row
            }
        }

        // After the input has been manipulated to replace the word-digits, use
        // the same code from the earlier problem to obtain the result.
        return parseContents(transformedInput).sum()
    }


    fun part2simpler(input: List<String>): Int {
        // I saw on the internet a solution that allows using substitutions
        // while accounting for the overlapping cases. It's so simple!
        val wordDigits = mapOf(
            "one" to "o1e", "two" to "t2o", "three" to "th3ee",
            "four" to "fo4r", "five" to "f5e", "six" to "s6x",
            "seven" to "se7en", "eight" to "ei8th", "nine" to "ni9e"
        )

        val transformedInput = input.map { row ->
            var mutableRow = row
            wordDigits.entries.map { entry ->
                mutableRow = mutableRow.replace(entry.key, entry.value)
            }
            mutableRow
        }

        // After the input has been manipulated to replace the word-digits, use
        // the same code from the earlier problem to obtain the result.
        return parseContents(transformedInput).sum()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_01/test_input")
    part1(testInput).println()
    part2(testInput).println()

    val input = readInput("Day_01/input")
    part1(input).println()
    part2(input).println()
    part2simpler(input).println()
}
