class Solution:
    def trailingZeroes(self, n: int) -> int:
        div = 5
        count = 0
        while n // div:
            count += n // div
            div = div * 5

        return count
