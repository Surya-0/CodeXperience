import heapq
class Solution:
    def kSmallestPairs(self, nums1: 'List[int]', nums2: 'List[int]', k: int) -> 'List[List[int]]':
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        # Initialize the heap with the smallest element from each row
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        # print(min_heap)
        res = []
        # Extract the smallest pairs up to k times
        while min_heap and len(res) < k:
            total, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res