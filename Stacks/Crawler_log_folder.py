from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # stack = []
        c = 0
        for log in logs:

            if log == "../":
                if c > 0:
                    c -= 1
                else:
                    continue

            elif log == "./":
                c += 0

            else:
                c += 1
            # print(log," ",c)

        return c

