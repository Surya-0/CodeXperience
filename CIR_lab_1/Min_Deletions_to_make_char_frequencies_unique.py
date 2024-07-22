from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        used_freq = set()
        res = 0
        for ch, freq in count.items():
            while freq in used_freq and freq != 0:
                freq -= 1
                res += 1
            used_freq.add(freq)

        return res

