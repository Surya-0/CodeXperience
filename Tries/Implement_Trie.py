class TreeNode:
    # Each node consists of an alphabets array of size 26 and an end of word pointer
    def __init__(self):
        self.children = [None] * 26
        self.EOW = False


class Trie:
    # Well we first initialise the root with a simple tree node
    def __init__(self):
        self.root = self.getNode()

    # Helper function to return a node
    def getNode(self):
        return TreeNode()

    def char_to_int(self, ch):
        return (ord(ch) - ord('a'))

    def insert(self, word: str) -> None:
        cur = self.root
        n = len(word)
        for i in range(n):
            val = self.char_to_int(word[i])
            if not cur.children[val]:
                cur.children[val] = self.getNode()
            cur = cur.children[val]
        cur.EOW = True

    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        for i in range(n):
            val = self.char_to_int(word[i])
            if not cur.children[val]:
                return False
            cur = cur.children[val]
        return cur.EOW == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        n = len(prefix)
        for i in range(n):
            val = self.char_to_int(prefix[i])
            if not cur.children[val]:
                return False
            cur = cur.children[val]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)