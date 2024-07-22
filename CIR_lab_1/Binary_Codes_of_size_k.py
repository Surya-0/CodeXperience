class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        temp = set()
        for i in range(0, n - k + 1):
            temp.add(s[i:i + k])

        return len(temp) == 2 ** k
