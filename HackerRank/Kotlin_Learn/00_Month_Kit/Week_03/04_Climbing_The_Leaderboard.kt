// https://www.hackerrank.com/challenges/one-month-preparation-kit-climbing-the-leaderboard/problem

fun climbingLeaderboard(ranked: Array<Int>, player: Array<Int>): Array<Int> {
    val uniqueRanked = ranked.toList().distinct().reversed()
    val arrayOfPlayerRanks = mutableListOf<Int>()
    var playerScoreIndex = 0
    var rankIndex = 0
    // Let's advance two indices, one on the list of existing scores,
    // and one on the list of player scores. The list of existing scores is
    // sorted reversed (lower to higher). The list of player scores is also
    // in ascending order.
    while (rankIndex < uniqueRanked.size && playerScoreIndex < player.size) {
        val playerScore = player[playerScoreIndex]
        val rankScore = uniqueRanked[rankIndex]
        // Compare the current player score with the current existing score
        // in the ranks.
        if (playerScore < rankScore) {
            // If it's lower, it means the player is one position below the
            // score in the current ranks. We move the player score index
            // but not the existing rank index.
            arrayOfPlayerRanks.add(uniqueRanked.size - rankIndex + 1)
            playerScoreIndex += 1
        } else if (playerScore == rankScore) {
            // If it's the same, it means the player is in the same position
            // as the score in the current ranks. We move the player score
            // index but not the existing rank index.
            arrayOfPlayerRanks.add(uniqueRanked.size - rankIndex)
            playerScoreIndex += 1
        } else {
            // Player exceeded the current rank so lets advance the ranks
            // to compare player to until finding a rank the player is equal
            // or lower to.
            rankIndex +=1
        }
    }
    
    // If we exhausted the list of existing scores but the player still has
    // some unprocessed scores, it means all those scores are higher than
    // the highest existing score, so all those times the player will be in
    // the first rank.
    if (playerScoreIndex < player.size) {
        val ranksUnprocessed = player.size - playerScoreIndex
        for (i in 0 until ranksUnprocessed) {
            arrayOfPlayerRanks.add(1)
        }
    }
    return arrayOfPlayerRanks.toTypedArray()
}

fun main(args: Array<String>) {
    val rankedCount = readLine()!!.trim().toInt()

    val ranked = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val playerCount = readLine()!!.trim().toInt()

    val player = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    val result = climbingLeaderboard(ranked, player)

    println(result.joinToString("\n"))
}
