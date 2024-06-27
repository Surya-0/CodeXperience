from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: 'List[int]') -> bool:
        d1 = defaultdict(int)
        for i in arr:
            d1[i] += 1

        return len(set(d1.values())) == len(d1.values())