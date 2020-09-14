# 388 - Longest Absolute File Path (Medium)
# https://leetcode.com/problems/longest-absolute-file-path/

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # A file system: has either files or more fs/folders.
        class FileTree:
            def __init__(self, name, level, parent):
                self.name = name
                self.level = level
                self.parent = parent
                self.children = []

        # Separate input by \n newlines.
        lines = input.split("\n")
        # Filesystem object.
        fs = FileTree("", -1, None)
        # Current pointer.
        folder = fs

        for i in range(len(lines)):
            line = lines[i]
            tabCount = line.count("\t")
            line = line.replace("\t", "")
            # If line its at a previous or current level, go up until reaching
            # the parent of this line.
            while tabCount <= folder.level:
                folder = folder.parent
            # Append to the children of this level.
            folder.children.append(FileTree(line + "/", tabCount, folder))
            # If its a folder, enter that folder.
            if line.count(".") == 0:
                folder = folder.children[-1]
                
        # Do a DFS to build the longest possible chain.
        def DFS(fil):
            curName = fil.name
            # Remove the trailing "/" from a file.
            if curName.count(".") > 0:
                curName = curName.replace("/", "")
            maxName = curName
            # Iterate over the subfiles, if any. A file will not have
            # children and just the filename will be returned.
            for subfil in fil.children:
                nxt = curName + DFS(subfil)
                # Replace maxName only if length is exceeded and it has
                # a file at the end of the chain.
                if len(nxt) > len(maxName) and nxt.count(".") > 0:
                    maxName = nxt
            return maxName
        
        return len(DFS(fs))
