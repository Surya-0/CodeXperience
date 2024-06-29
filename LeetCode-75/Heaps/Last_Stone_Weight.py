import heapq


class Solution:
    def lastStoneWeight(self, stones: 'List[int]') -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)  # min in the negative side(-8)
            y = heapq.heappop(stones)  # Second min in the negative side(-7)
            if x != y:
                y = x - y
                heapq.heappush(stones, y)

        return -stones[0] if stones else 0