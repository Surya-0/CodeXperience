from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_res = []
        res = [1]
        final_res.append(res)
        for i in range(numRows-1):
            temp = [0] * (len(res)+1)
            for j in range(len(res)):
                temp[j] += res[j]
                temp[j+1] += res[j]
            # print(temp)
            final_res.append(temp)
            res = temp
        return final_res