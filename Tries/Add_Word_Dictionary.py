import random


class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False


class WordDictionary:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = self.getNode()
            cur = cur.children[ch]
        cur.EOW = True

    def search(self, word: str) -> bool:

        def dfs(root, ind):
            cur = root
            for i in range(ind, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        # print(child)
                        if dfs(child, i + 1):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.EOW

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)