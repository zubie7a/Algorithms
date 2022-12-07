fun main() {

    data class MyFile(val name: String, val size: Int)

    data class MyFolder(
        val name: String,
        val files: MutableMap<String, MyFile>,
        val folders: MutableMap<String, MyFolder>,
        val parent: MyFolder?
    )

    fun recursiveFileSizeCount(folder: MyFolder): Pair<Int, List<Int>> {

        // Size of all folders and files in the current folder.
        var folderSize = 0
        // List of all individual subfolders sizes
        val subFolderSizes = mutableListOf<Int>()

        // First add up the sizes of the files in the folder.
        folderSize += folder.files.values.sumOf { file -> file.size }
        // Then add up recursively the sizes of the subfolders.
        folderSize += folder.folders.values.sumOf { subFolder ->

            val result = recursiveFileSizeCount(subFolder)
            subFolderSizes.addAll(result.second)
            result.first
        }

        subFolderSizes.add(folderSize)
        return Pair(folderSize, subFolderSizes)
    }

    fun partX(input: List<String>): Pair<Int, List<Int>> {

        val myFileSystem = MyFolder(
            name = "",
            files = mutableMapOf(),
            folders = mutableMapOf(),
            parent = null
        )

        var currentFolder = myFileSystem

        input.forEach { line ->

            // The line is a command
            if (line.startsWith("$")) {

                // `cd`: change directory
                // `ls`: list
                val arguments = line.split(" ")
                if (arguments[1] == "cd") {

                    val target = arguments[2]

                    if (target == "..") {
                        // Go up one level
                        currentFolder = currentFolder.parent!!
                    } else {
                        // If the folder is not there, create it. "cd" is not a folder creating
                        // operation, but we are assuming that the filesystem is already there
                        // and navigating from the input is just exploring/finding out.
                        currentFolder.folders.putIfAbsent(
                            target, MyFolder(
                                name = target,
                                files = mutableMapOf(),
                                folders = mutableMapOf(),
                                parent = currentFolder
                            )
                        )
                        // Navigate to the folder.
                        currentFolder = currentFolder.folders[target]!!
                    }
                } else if (arguments[1] == "ls") {
                    // If it's list, do nothing, the output will come in the next line.
                }
            } else {
                // The lines are output to previous command, and for now the only output
                // commands are `ls` outputs.
                val output = line.split(" ")
                val name = output[1]

                if (output[0] == "dir") {
                    // A directory, create it in the current filesystem level.
                    currentFolder.folders.putIfAbsent(
                        name, MyFolder(
                            name = name,
                            files = mutableMapOf(),
                            folders = mutableMapOf(),
                            parent = currentFolder
                        )
                    )
                } else {
                    // A file, create it in the current filesystem level.
                    val size = output[0].toInt()
                    currentFolder.files.putIfAbsent(
                        name, MyFile(
                            name = name,
                            size = size
                        )
                    )
                }
            }
        }

        return recursiveFileSizeCount(myFileSystem)
    }

    fun part1(input: List<String>): Int {

        // Compute the filesystem structure and then get the total size and a list of
        // the individual folders' sizes.
        val result = partX(input)
        // Return the sum of individual folder sizes that are smaller than 100000.
        return result.second.filter { it <= 100000 }.sum()
    }

    fun part2(input: List<String>): Int {

        // Compute the filesystem structure and then get the total size and a list of
        // the individual folders' sizes.
        val result = partX(input)
        val totalSpace = 70000000
        val requiredSpace = 30000000
        // The actual space left is the total - the current "/" folder size.
        val spaceLeft = totalSpace - result.first
        // Find how much more space is needed to reach the required space for update.
        val spaceNeeded = requiredSpace - spaceLeft
        // Find the size of the smallest possible folder that can be deleted to have enough space.
        return result.second.sorted().find { it > spaceNeeded }!!
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("Day_07/test_input")
    println(part1(testInput))
    println(part2(testInput))

    val input = readInput("Day_07/input")
    println(part1(input))
    println(part2(input))
}
