from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]

        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for n, c in d.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
