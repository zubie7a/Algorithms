import kotlin.math.max

fun main() {

    fun processRounds(game: String): List<List<String>> {
        // game: "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

        return game
                // ["3 blue, 4 red", " 1 red, 2 green, 6 blue", " 2 green"]
                .split(";")
                .map { round ->
                    // [["3 blue", "4 red"], ["1 red", "2 green", "6 blue"], ["2 green"]]
                    round.split(",")
                        .map { pick ->
                            pick.trim()
                        }
                }
    }

    fun part1(input: List<String>): Int {
        // Find which games would be possible if bag contained only
        // 12 red cubes, 13 green cubes, and 14 blue cubes.

        val limits = mapOf(
            "red" to 12,
            "green" to 13,
            "blue" to 14
        )

        // Each line of input will have this form:
        // Every game will consist of several rounds, each round may or may not
        // take cubes from all colors or just some of them.
        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        val validGameIndexes = input.map {
            // "Game 1"
            val gameId = it.split(":")[0]
            // 1
            val gameIndex = gameId.split(" ")[1].toInt()

            val gameRounds = processRounds(it.split(":")[1])

            // Assume validity at first.
            var valid = true
            gameRounds.forEach { round ->
                // Each step is the amount of a certain cube color picked.
                round.forEach { pick ->
                    val (amount, color) = pick.split(" ")
                    // If for any pick of the round, the picked amount of cubes
                    // of a certain color exceeds the limit for that color, then
                    // this entire round is invalid.
                    if (limits.getOrDefault(color, 0) < amount.toInt()) {
                        valid = false
                    }
                }
            }

            if (valid) {
                gameIndex
            } else {
                0
            }
        }

        return validGameIndexes.sum()
    }

    fun part2(input: List<String>): Int {
        val powers = input.map {
            // Keep track of the minimum amount of cubes required to make a game valid.
            // For this we need to know the maximum amount of cubes of each color that
            // appears in each round of a game.
            val minimumCubes = mutableMapOf(
                "red" to 0,
                "green" to 0,
                "blue" to 0
            )
            val gameRounds = processRounds(it.split(":")[1])

            gameRounds.forEach { round ->
                // Each step is the amount of a certain cube color picked.
                round.forEach { pick ->
                    val (amount, color) = pick.split(" ")
                    // In each round, keep increasing the maximum seen value for each
                    // cube color.
                    minimumCubes[color] = max(
                        minimumCubes.getOrDefault(color, 0),
                        amount.toInt()
                    )
                }
            }

            // Now find the power by multiplying the amount of minimum cubes required.
            minimumCubes.values.reduce {
                acum, elem -> acum * elem
            }
        }

        return powers.sum()
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_02/test_input")
    part1(testInput).println()
    part2(testInput).println()

    val input = readInput("Day_02/input")
    part1(input).println()
    part2(input).println()
}
