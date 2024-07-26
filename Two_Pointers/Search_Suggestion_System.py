from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Two pointer approach
        products.sort()
        res = []
        l = 0
        r = len(products) - 1
        for i in range(len(searchWord)):
            ch = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != ch):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != ch):
                r -= 1

            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])

        return res


