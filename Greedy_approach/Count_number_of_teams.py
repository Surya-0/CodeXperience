from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for middle in range(1, len(rating) - 1):
            left_smaller = right_larger = 0
            for i in range(middle):
                if rating[i] < rating[middle]:
                    left_smaller += 1

            for i in range(middle + 1, len(rating)):
                if rating[i] > rating[middle]:
                    right_larger += 1

            res += left_smaller * right_larger
            left_larger = middle - left_smaller
            right_smaller = len(rating) - middle - 1 - right_larger

            res += left_larger * right_smaller

        return res

