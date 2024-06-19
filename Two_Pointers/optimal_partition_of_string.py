class Solution:
    def partitionString(self, s: str) -> int:
        l = 0
        r = 0
        visit = set()
        count = 0
        # res = []
        # temp = ""
        while r < len(s):
            if s[r] not in visit:
                visit.add(s[r])
                # temp += s[r]
                r += 1

            else:
                # res.append(temp)
                count += 1
                l = r
                visit = set()
                # temp = ""

        # res.append(temp)
        # print(res)
        return count + 1
