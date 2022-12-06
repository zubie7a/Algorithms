fun main() {

    fun part1(input: List<String>): Int {

        var currentElfWeight = 0
        var listOfElvesWeights = mutableListOf<Int>()

        input.forEach { row ->
            if (row.isNotEmpty()) {
                currentElfWeight += row.toInt()
            } else {
                listOfElvesWeights.add(currentElfWeight)
                currentElfWeight = 0
            }
        }

        return listOfElvesWeights.max()
    }

    fun part2(input: List<String>): Int {

        var currentElfWeight = 0
        var listOfElvesWeights = mutableListOf<Int>()

        input.forEach { row ->
            if (row.isNotEmpty()) {
                currentElfWeight += row.toInt()
            } else {
                listOfElvesWeights.add(currentElfWeight)
                currentElfWeight = 0
            }
        }

        // return listOfElvesWeights.sorted().reversed().subList(0, 3).sum()
        // return listOfElvesWeights.sorted().takeLast(3).sum()
        return listOfElvesWeights.sortedDescending().take(3).sum()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_01/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_01/input")
    println(part1(input))
    println(part2(input))
}
