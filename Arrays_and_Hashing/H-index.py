from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0
        # print(citations)
        for ct in range(0, max(citations) + 1):
            count = 0
            if ct <= len(citations):
                for ele in citations:
                    # print(ele," ",ct)
                    if ct <= ele:
                        count += 1

                if count >= ct:
                    res = max(res, ct)

        return res



