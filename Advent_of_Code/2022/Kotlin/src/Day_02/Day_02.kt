enum class Choices {
    ROCK,
    PAPER,
    SCISSORS
}

fun main() {

    // Opponent:
    // A - Rock, B - Paper, C - Scissors
    // You:
    // X - Rock, Y - Paper, Z - Scissors
    // ...
    // You get 0 points for losing,
    // 3 points for drawing, and
    // 6 points for winning
    // ...
    // You can get extra points:
    // 1 points for playing X/rock
    // 2 points for playing Y/paper
    // 3 point for playing Z/scissors

    val mapOfExtraScores = mapOf(
        Choices.ROCK to 1,
        Choices.PAPER to 2,
        Choices.SCISSORS to 3
    )

    val mapOfChoices = mapOf(
        "A" to Choices.ROCK, "X" to Choices.ROCK,
        "B" to Choices.PAPER, "Y" to Choices.PAPER,
        "C" to Choices.SCISSORS, "Z" to Choices.SCISSORS
    )

    val mapOfAdvantages = mapOf(
        Choices.ROCK to Choices.SCISSORS,
        Choices.SCISSORS to Choices.PAPER,
        Choices.PAPER to Choices.ROCK
    )

    fun part1(input: List<String>): Int {

        val scores = input.map { game ->

            val choices = game.split(" ")
            val opponent = mapOfChoices[choices[0]]
            val you = mapOfChoices[choices[1]]

            mapOfExtraScores[you]!! + when {
                // You lost
                mapOfAdvantages[opponent] == you -> 0
                // You won
                mapOfAdvantages[you] == opponent -> 6
                // You drew
                else -> 3
            }
        }

        return scores.sum()
    }

    // So actually X, Y, Z didn't mean the answer but:
    // X: need to play a move to lose
    // Y: need to play a move to draw
    // Z: need to play a move to win

    val mapOfWeaknesses = mapOf(
        Choices.SCISSORS to Choices.ROCK,
        Choices.PAPER to Choices.SCISSORS,
        Choices.ROCK to Choices.PAPER
    )

    fun part2(input: List<String>): Int {

        val scores = input.map { game ->

            val row = game.split(" ")
            val opponent = mapOfChoices[row[0]]

            val you = when (row[1]) {
                // You need to lose, pick a move weak to opponent
                "X" -> mapOfAdvantages[opponent]
                // You need to win, pick a move opponent is weak to
                "Z" -> mapOfWeaknesses[opponent]
                // You need to draw, pick same move as opponent
                else -> opponent
            }

            mapOfExtraScores[you]!! + when {
                // You lost
                mapOfAdvantages[opponent] == you -> 0
                // You won
                mapOfAdvantages[you] == opponent -> 6
                // You drew
                else -> 3
            }
        }

        return scores.sum()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_02/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_02/input")
    println(part1(input))
    println(part2(input))
}
