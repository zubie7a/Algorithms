fun main() {

    fun part1(input: List<String>): String {

        // For simplicity, let's say the crates rows are those that have "[" somewhere.
        val cratesRows = input.filter { it.contains("[") }

        // For simplicity, let's say the instruction rows are those that don't have "[".
        val nonCratesRows = input.filter { !it.contains("[") }.filter { it.isNotBlank() }

        // The first row of the non crate rows indicates the columns index.
        val indexes = nonCratesRows[0]

        /*
                    [D]
                [N] [C]
                [Z] [M] [P]
                 1   2   3

            The representation in code will be:

            val graph = mutableMapOf<Int, List<Char>>()
            { 1=[Z, N], 2=[M, C, D], 3=[P] }
            Key: a column id
            Value: a list of crate ids in that column.
            The graph is built bottom up meaning the last element on each list will be the
            element at the top of the column.
         */

        val graph = mutableMapOf<Int, MutableList<Char>>()

        indexes.forEachIndexed { index, char ->

            if (char.isDigit()) {

                // A list to contain the crates ids of a row.
                graph[char.digitToInt()] = mutableListOf()

                cratesRows.reversed().forEach { crateRow ->
                    if (index < crateRow.length && crateRow[index].isLetter()) {
                        // Because iterating rows in reverse, last element of the column ids
                        // list will be the id of the crate that's at the top of column.
                        graph[char.digitToInt()]!!.add(crateRow[index])
                    }
                }
            }
        }

        // Now evaluate the instructions
        nonCratesRows.subList(1, nonCratesRows.size).forEach { instructionRow ->

            // We are assuming that an instruction has this format:
            // "Move X from Y to Z" where X, Y, and Z are integers.
            val instruction = instructionRow
                .split(" ")
                .mapNotNull { it.toIntOrNull() }

            val amount = instruction[0]
            val source = instruction[1]
            val target = instruction[2]

            // Start moving boxes, one by one from the one at the top, meaning repeated
            // operations on same columns will move boxes in opposite order to target column.
            for (op in 0 until amount) {
                val sourceColumn = graph[source]!!
                val targetColumn = graph[target]!!
                val crateId = sourceColumn.removeLast()
                targetColumn.add(crateId)
            }
        }

        // Take the ids of the crates at the end/top of each column.
        return graph.map { it.value.last() }.joinToString(separator = "")
    }

    fun part2(input: List<String>): String {

        // For simplicity, let's say the crates rows are those that have "[" somewhere.
        val cratesRows = input.filter { it.contains("[") }

        // For simplicity, let's say the instruction rows are those that don't have "[".
        val nonCratesRows = input.filter { !it.contains("[") }.filter { it.isNotBlank() }

        // The first row of the non crate rows indicates the columns index.
        val indexes = nonCratesRows[0]

        /*
                    [D]
                [N] [C]
                [Z] [M] [P]
                 1   2   3

            The representation in code will be:

            val graph = mutableMapOf<Int, List<Char>>()
            { 1=[Z, N], 2=[M, C, D], 3=[P] }
            Key: a column id
            Value: a list of crate ids in that column.
            The graph is built bottom up meaning the last element on each list will be the
            element at the top of the column.
         */

        val graph = mutableMapOf<Int, MutableList<Char>>()

        indexes.forEachIndexed { index, char ->

            if (char.isDigit()) {

                // A list to contain the crates ids of a row.
                graph[char.digitToInt()] = mutableListOf()

                cratesRows.reversed().forEach { crateRow ->
                    if (index < crateRow.length && crateRow[index].isLetter()) {
                        // Because iterating rows in reverse, last element of the column ids
                        // list will be the id of the crate that's at the top of column.
                        graph[char.digitToInt()]!!.add(crateRow[index])
                    }
                }
            }
        }

        // Now evaluate the instructions
        nonCratesRows.subList(1, nonCratesRows.size).forEach { instructionRow ->

            // We are assuming that an instruction has this format:
            // "Move X from Y to Z" where X, Y, and Z are integers.
            val instruction = instructionRow
                .split(" ")
                .mapNotNull { it.toIntOrNull() }

            val amount = instruction[0]
            val source = instruction[1]
            val target = instruction[2]

            val sourceColumn = graph[source]!!
            val targetColumn = graph[target]!!

            // Start moving boxes, all together from the one at the top, meaning the boxes
            // will preserve their order when moved to the new column.
            val crateIds = sourceColumn.subList(sourceColumn.size - amount, sourceColumn.size)
            graph[source] = sourceColumn.subList(0, sourceColumn.size - amount)
            targetColumn.addAll(crateIds)
        }

        // Take the ids of the crates at the end/top of each column.
        return graph.map { it.value.last() }.joinToString(separator = "")
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_05/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_05/input")
    println(part1(input))
    println(part2(input))
}
