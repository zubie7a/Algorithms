fun main() {

    fun part1(input: List<String>): Int {

        val grid = mutableListOf<List<Int>>()

        input.forEach { treeRow ->
            val heights = treeRow.split("").mapNotNull { it.toIntOrNull() }
            grid.add(heights)
        }

        var visibleTrees = 0

        grid.indices.forEach { idxRow ->

            val row = grid[idxRow]
            row.indices.forEach {idxCol ->

                val treeHeight = grid[idxRow][idxCol]
                var visibleTop = true
                var visibleLeft = true
                var visibleRight = true
                var visibleDown = true

                // Check all other trees in the same row.
                (0 until grid[idxRow].size).forEach { idxOtherCol ->
                    val otherTreeHeight = grid[idxRow][idxOtherCol]
                    if (otherTreeHeight >= treeHeight) {
                        if (idxOtherCol < idxCol) {
                            visibleLeft = false
                        } else if (idxOtherCol > idxCol) {
                            visibleRight = false
                        }
                    }
                }

                // Check all other trees in the same column.
                (0 until grid.size).forEach { idxOtherRow ->
                    val otherTreeHeight = grid[idxOtherRow][idxCol]
                    if (otherTreeHeight >= treeHeight) {
                        if (idxOtherRow < idxRow) {
                            visibleTop = false
                        } else if (idxOtherRow > idxRow) {
                            visibleDown = false
                        }
                    }
                }

                if (visibleTop || visibleLeft || visibleRight || visibleDown) {
                    visibleTrees += 1
                }
            }
        }

        return visibleTrees
    }

    fun part2(input: List<String>): Int {

        val grid = mutableListOf<List<Int>>()

        input.forEach { treeRow ->
            val heights = treeRow.split("").mapNotNull { it.toIntOrNull() }
            grid.add(heights)
        }

        var bestVisibility = 0

        grid.indices.forEach { idxRow ->

            val row = grid[idxRow]
            row.indices.forEach {idxCol ->

                val treeHeight = grid[idxRow][idxCol]

                // Count how many trees are visible in each direction.
                var distanceVisibleTop = 0
                var distanceVisibleLeft = 0
                var distanceVisibleRight = 0
                var distanceVisibleDown = 0

                // Check all other trees to the left.
                for (idxOtherCol in idxCol - 1 downTo 0) {
                    val otherTreeHeight = grid[idxRow][idxOtherCol]
                    distanceVisibleLeft += 1
                    if (otherTreeHeight >= treeHeight) {
                        break
                    }
                }

                // Check all other trees to the right.
                for (idxOtherCol in idxCol + 1 until row.size) {
                    val otherTreeHeight = grid[idxRow][idxOtherCol]
                    distanceVisibleRight += 1
                    if (otherTreeHeight >= treeHeight) {
                        break
                    }
                }

                // Check all other trees above
                for (idxOtherRow in idxRow - 1 downTo 0) {
                    val otherTreeHeight = grid[idxOtherRow][idxCol]
                    distanceVisibleTop += 1
                    if (otherTreeHeight >= treeHeight) {
                        break
                    }
                }

                // Check all other trees below
                for (idxOtherRow in idxRow + 1 until grid.size) {
                    val otherTreeHeight = grid[idxOtherRow][idxCol]
                    distanceVisibleDown += 1
                    if (otherTreeHeight >= treeHeight) {
                        break
                    }
                }

                val visibility =
                    distanceVisibleTop * distanceVisibleLeft * distanceVisibleRight * distanceVisibleDown

                if (visibility > bestVisibility) {
                    bestVisibility = visibility
                }
            }
        }

        return bestVisibility
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_08/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_08/input")
    println(part1(input))
    println(part2(input))
}
