class Solution:
    def countOdds(self, low: int, high: int) -> int:
        temp = high - low + 1
        if temp % 2 == 0:
            return temp//2
        else:
            return temp//2 + 1 if low % 2 else temp//2

