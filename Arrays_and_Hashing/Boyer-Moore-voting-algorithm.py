"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.
"""

# The intuition behind the algorithm is that if there is a majority element in the array, it will always remain as
# the candidate at the end of the traversal, because its count will never reach 0.
# Time complexity is O(n) and space complexity is O(1)
class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count += 1

            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1

        return candidate

