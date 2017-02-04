class Trie():
    def __init__(self, char):
        # The data value for this node.
        self.char = char
        # The current word so far.
        self.word = ""
        # The children of this node.
        self.children = {}
        # Whether this node is a complete word or not.
        self.final = False
        # The amount of all children from this node downwards.
        self.countChildren = 0
        
    def add(self, string, index):
        # If its the last position of the word being inserted.
        if index + 1 == len(string):
            # Mark the word as finalized.
            self.final = True
        # If there's still characters left to insert.
        if index + 1 < len(string):
            # If there's currently not a children with a given character.
            if not self.children.get(string[index + 1]):
                self.children[string[index + 1]] = Trie(string[index + 1])
            # Increase the count of childrens for this character. At every
            # insertion, when it goes through this node, it will increase
            # the value, keeping track of all the children downwards.
            self.countChildren += 1
            # Call the add method on the children recursively from the
            # next character onwards.
            child = self.children[string[index + 1]]
            child.add(string, index + 1)
        
    def find(self, string, index):
        # If the current node's character is the current query string
        # character (it means it has matched so far).
        if self.char == string[index]:
            if index + 1 < len(string):
                if self.children.get(string[index + 1]):
                    child = self.children[string[index + 1]] 
                    return child.find(string, index + 1)
                else:
                    return 0, False
            else:
                completed = 0
                if self.final == True:
                    completed = 1
                return self.countChildren + completed, True          
        else:
            return 0, False

n = int(raw_input())
# A table of Tries for each possible starting letter.
tries = {}
for _ in xrange(n):
    op, word = raw_input().split()
    if op == "add":
        if not tries.get(word[0]):
            tries[word[0]] = Trie(word[0])
        tries[word[0]].add(word, 0)
    if op == "find":
        if not tries.get(word[0]):
            print 0
        else:
            count, _ = tries[word[0]].find(word, 0)
            print count  
