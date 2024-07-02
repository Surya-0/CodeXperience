from collections import Counter
import heapq
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        d = Counter(hand)
        min_heap = list(d.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                # Which means that we do not have the required values to complete the group
                if i not in d:
                    return False

                d[i] -= 1
                if d[i] == 0:
                    # Which means if we are not popping the minimum value
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True




