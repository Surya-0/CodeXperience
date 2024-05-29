from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

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

# import heapq
#
# def max_sum(nums, C):
#     # Calculate the size of each subarray
#     M = len(nums) // C
#     # Initialize the sum
#     total_sum = 0
#     # Iterate over the array with a sliding window
#     for i in range(len(nums) - M + 1):
#         # Initialize a min heap
#         heap = []
#         # Add all the elements in the current window to the heap
#         for j in range(i, i + M):
#             heapq.heappush(heap, nums[j])
#         # Pop the smallest k elements from the heap and add them to the sum
#         for _ in range(M // C):
#             total_sum += heapq.heappop(heap)
#     # Return the sum
#     return total_sum
#
# nums = [1,3,5,3,6,1]
# C = 3
# print(max_sum(nums,C))