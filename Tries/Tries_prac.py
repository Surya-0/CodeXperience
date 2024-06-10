class TrieNode:
    def __init__(self):
        # Initialize the node with an array of 26 'None' values, each representing a letter of the alphabet
        self.children = [None]*26
        # A boolean flag to indicate if a node marks the end of a word
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # Initialize the Trie with a root node
        self.root = self.getNode()

    def getNode(self):
        # Create and return a new TrieNode
        return TrieNode()

    def _charToIndex(self, ch):
        # Convert the character to an index (0-25) using ASCII values
        return ord(ch) - ord('a')

    def insert(self, word):
        # Start at the root node
        pCrawl = self.root
        length = len(word)

        # Iterate through each character in the word
        for level in range(length):
            # Convert the character to its corresponding index
            index = self._charToIndex(word[level])

            # If the child node for this character doesn't exist, create it
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()

            # Move to the child node
            pCrawl = pCrawl.children[index]

        # Mark the end of the word
        pCrawl.isEndOfWord = True

    def search(self, word):
        # Start at the root node
        pCrawl = self.root
        length = len(word)

        # Iterate through each character in the word
        for level in range(length):
            # Convert the character to its corresponding index
            index = self._charToIndex(word[level])

            # If the child node for this character doesn't exist, the word is not in the Trie
            if not pCrawl.children[index]:
                return False

            # Move to the child node
            pCrawl = pCrawl.children[index]

        # Check if the last node is indeed the end of the word
        return pCrawl != None and pCrawl.isEndOfWord
