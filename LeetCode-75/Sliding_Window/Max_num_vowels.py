class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        refer = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        r = k
        max_sum = 0
        for i in range(k):
            if s[i] in refer:
                max_sum += 1

        temp = max_sum
        while r < len(s):
            if s[l] in refer:
                temp -= 1

            if s[r] in refer:
                temp += 1

            l += 1
            r += 1
            max_sum = max(temp, max_sum)

        return max_sum