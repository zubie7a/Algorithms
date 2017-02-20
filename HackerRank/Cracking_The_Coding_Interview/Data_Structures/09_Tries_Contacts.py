# https://www.hackerrank.com/challenges/ctci-contacts/forum
class Trie(object):
    # Optimization to save space, instead of having a
    # dictionary for any amount of attributes, have the
    # attributes fixed from start. It fixed memory
    # problems for really big amount of instances!
    # https://docs.python.org/2/reference/datamodel.html#slots
    __slots__ = ('children', 'count')
    def __init__(self):
        # The children of this node.
        self.children = {}
        # The amount of all words this node acts as
        # a prefix for.
        self.count = 0
        
    def add(self, string, index):
        # Increase the count of childrens for this 
        # character. At every insertion, when it goes 
        # through this node, it will increase the value, 
        # keeping track of all the children downwards.
        self.count += 1
        # If there's still characters left to insert.
        if index < len(string):
            char = string[index]
            # If there's currently not a children with a 
            # given char.
            if not self.children.get(char):
                self.children[char] = Trie()
            child = self.children[char]
            # After creating/retrieving the children, call 
            # add on it and advance the index interator of 
            # the string.
            child.add(string, index + 1)
        
    def find(self, string, index):
        # If there's still characters to match.
        if index < len(string):
            # If there's a node with the current character.
            if self.children.get(string[index]):
                child = self.children[string[index]]
                # Go down recursively to it advancing the 
                # string index.
                return child.find(string, index + 1)
            else:
                return 0
        # When all characters in query have been matched.
        else:
            return self.count

n = int(input())
trie = Trie()
for _ in range(n):
    op, word = input().split()
    if op == "add":
        trie.add(word, 0)
    if op == "find":
        count = trie.find(word, 0)
        print(count)