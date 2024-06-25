class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        temp = set()
        for i in range(len(s) - k + 1):
            temp.add(s[i:k + i])

        return len(temp) == 2 ** k
