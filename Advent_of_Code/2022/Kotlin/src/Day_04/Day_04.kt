fun main() {

    fun part1(input: List<String>): Int {

        var totalFullyContained = 0

        input.forEach { assignment ->

            val leftRange = assignment
                .split(',')[0]
                .split('-')
                .map { it.toInt() }

            val rightRange = assignment
                .split(',')[1]
                .split('-')
                .map { it.toInt() }

            // Check if either range fully contains the other.
            totalFullyContained += when {
                // Right elf range is completely contained in left elf range.
                leftRange[0] <= rightRange[0] && leftRange[1] >= rightRange[1] -> 1
                // Left elf range is completely contained in right elf range.
                rightRange[0] <= leftRange[0] && rightRange[1] >= leftRange[1] -> 1
                else -> 0
            }
        }

        return totalFullyContained
    }

    fun part2(input: List<String>): Int {

        var totalOverlapping = 0

        input.forEach { assignment ->

            val leftRange = assignment
                .split(',')[0]
                .split('-')
                .map { it.toInt() }

            val rightRange = assignment
                .split(',')[1]
                .split('-')
                .map { it.toInt() }

            // Check if both ranges overlap at all.
            totalOverlapping += when {
                // Left elf start of range lies within right elf range.
                leftRange[0] >= rightRange[0] && leftRange[0] <= rightRange[1] -> 1
                // Left elf end of range lies within right elf range.
                leftRange[1] >= rightRange[0] && leftRange[1] <= rightRange[1] -> 1
                // Right elf start of range lies within left elf range.
                rightRange[0] >= leftRange[0] && rightRange[0] <= leftRange[1] -> 1
                // Right elf end of range lies within left elf range.
                rightRange[1] >= leftRange[0] && rightRange[1] <= leftRange[1] -> 1
                else -> 0
            }
        }

        return totalOverlapping
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_04/test_input")
    println(part1(testInput))
    println(part2(testInput))

     val input = readInput("Day_04/input")
     println(part1(input))
     println(part2(input))
}
