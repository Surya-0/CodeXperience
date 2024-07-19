from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for sp in spells:
            l = 0
            r = len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                target = sp * potions[mid]
                if target < success:
                    l = mid + 1

                else:
                    r = mid - 1

            # print(potions," ",l)
            res.append(len(potions) - l)

        return res