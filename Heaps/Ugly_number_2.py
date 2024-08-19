import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        visit = set()
        factors = [2, 3, 5]
        for i in range(n):
            val = heapq.heappop(min_heap)
            if i == n - 1:
                return val

            for fact in factors:
                if val * fact not in visit:
                    visit.add(val * fact)
                    heapq.heappush(min_heap, val * fact)

