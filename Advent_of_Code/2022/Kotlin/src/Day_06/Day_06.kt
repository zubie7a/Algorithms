fun main() {

    fun part1(input: List<String>): List<Int> {

        val resultIndices = mutableListOf<Int>()

        input.forEach { dataStream ->

            val markerSize = 4
            // Find the first group of 4 consecutive characters where they are all different.
            val index = (markerSize until dataStream.length).find {
                dataStream.subSequence(it - markerSize, it).toSet().size == markerSize
            }
            resultIndices.add(index!!)
        }
        return resultIndices
    }

    fun part2(input: List<String>): List<Int> {

        val resultIndices = mutableListOf<Int>()

        input.forEach { dataStream ->

            val markerSize = 14
            // Find the first group of 14 consecutive characters where they are all different.
            val index = (markerSize until dataStream.length).find {
                dataStream.subSequence(it - markerSize, it).toSet().size == markerSize
            }
            resultIndices.add(index!!)
        }
        return resultIndices
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_06/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_06/input")
    println(part1(input))
    println(part2(input))
}
