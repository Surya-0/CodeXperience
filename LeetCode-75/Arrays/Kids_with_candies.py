class Solution:
    def kidsWithCandies(self, candies: 'List[int]', extraCandies: int) -> 'List[bool]':
        res = []
        max_cand = max(candies)

        for i in candies:
            res.append(i + extraCandies >= max_cand)

        return res

