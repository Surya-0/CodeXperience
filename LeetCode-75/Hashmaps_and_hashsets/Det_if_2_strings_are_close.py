from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in word1:
            d1[i] += 1

        for i in word2:
            d2[i] += 1

        return sorted(d1.values()) == sorted(d2.values()) and set(d1.keys()) == set(d2.keys())