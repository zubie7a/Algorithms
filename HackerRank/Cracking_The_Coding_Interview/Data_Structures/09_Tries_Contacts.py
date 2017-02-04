from __future__ import print_function
class Trie():
    def __init__(self):
        # The children of this node.
        self.children = {}
        # The amount of all children from this node downwards.
        self.count = 0
        
    def add(self, string, index):
        # Increase the count of childrens for this character.
        # At every insertion, when it goes through this node,
        # it will increase the value, keeping track of all
        # the children downwards.
        self.count += 1
        # If there's still characters left to insert.
        if index < len(string):
            # If there's currently not a children with a given char.
            char = string[index]
            if not self.children.get(char):
                self.children[char] = Trie()
            child = self.children[char]
            # After creating/retrieving the children, call add on it
            # and advance the index interator of the string.
            child.add(string, index + 1)
        
    def find(self, string, index):
        # If there's still characters to match.
        if index < len(string):
            # If there's a node with the current character.
            if self.children.get(string[index]):
                child = self.children[string[index]]
                # Go down recursively to it advancing the string index.
                return child.find(string, index + 1)
            else:
                return 0
        # When all characters in query have been matched.
        else:
            return self.count

n = int(raw_input())
trie = Trie()
for _ in xrange(n):
    op, word = raw_input().split()
    if op == "add":
        trie.add(word, 0)
    if op == "find":
        count = trie.find(word, 0)
        print(count)
