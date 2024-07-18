from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list
        adList = defaultdict(list)
        for u, v, p in flights:
            adList[u].append((p, v))

        # Priority queue: (price, node, stops)
        minheap = [(0, src, 0)]

        # Dictionary to track minimum cost to reach a node with a certain number of stops
        best = {}

        while minheap:
            price, node, stops = heapq.heappop(minheap)

            if node == dst:
                return price

            if stops > k or (node, stops) in best and best[(node, stops)] <= price:
                continue

            best[(node, stops)] = price

            for nei_cost, nei_node in adList[node]:
                if stops + 1 <= k + 1:  # We can have at most k stops, which means k+1 edges
                    heapq.heappush(minheap, (price + nei_cost, nei_node, stops + 1))

        return -1


class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # We are going to use Bellman Ford
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            tempPrices = prices.copy()
            # source,destination,prices
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue

                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p

            prices = tempPrices

        return -1 if prices[dst] == float('inf') else prices[dst]
