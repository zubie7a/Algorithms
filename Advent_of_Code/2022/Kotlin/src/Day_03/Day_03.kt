fun main() {

    fun part1(input: List<String>): Int {

        var prioritySum = 0

        input.forEach { rucksack ->

            val left = rucksack.substring(0 until rucksack.length/2)
            val right = rucksack.substring(rucksack.length/2)

            // groupBy creates map<K, List<Char>>
            // groupingBy creates grouping<Char, key>
            val countLeft = left.toList().groupingBy { it }.eachCount()
            val countRight = right.toList().groupingBy { it }.eachCount()
            // It was not really necessary to find counts, could've simply done intersects
            // on left.toSet() and right.toSet(), still nice to know these functions exist!
            val overlapping = countLeft.keys.intersect(countRight.keys)

            overlapping.forEach {
                val priority = when (it.isUpperCase()) {
                    true -> it.code - 'A'.code + 27
                    else -> it.code - 'a'.code + 1
                }
                prioritySum += priority
            }
        }

        return prioritySum
    }

    fun part2(input: List<String>): Int {

        var prioritySum = 0

        for (index in 0 until input.size step 3) {

            val rucksack1 = input[index]
            val rucksack2 = input[index + 1]
            val rucksack3 = input[index + 2]

            val overlapping = rucksack1.toSet().intersect(
                rucksack2.toSet().intersect(
                    rucksack3.toSet()
                )
            )

            overlapping.forEach {
                val priority = when (it.isUpperCase()) {
                    true -> it.code - 'A'.code + 27
                    else -> it.code - 'a'.code + 1
                }
                prioritySum += priority
            }
        }

        return prioritySum
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_03/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_03/input")
    println(part1(input))
    println(part2(input))
}
