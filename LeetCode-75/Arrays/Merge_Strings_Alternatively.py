class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        res = ""
        while n1 > 0 and n2 > 0:
            res += word1[i]
            n1 -= 1
            res += word2[i]
            n2 -= 1
            i += 1

        while n1 > 0:
            res += word1[i]
            i += 1
            n1 -= 1

        while n2 > 0:
            res += word2[i]
            i += 1
            n2 -= 1

        return res
