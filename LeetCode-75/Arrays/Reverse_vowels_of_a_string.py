class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s = list(s)
        # print(len(s))
        # print(s)
        while l < r:
            # print(l," ",r)
            if s[l] not in vowels:
                l += 1

            if s[r] not in vowels:
                r -= 1

            if l < len(s) and r >= 0 and s[l] in vowels and s[r] in vowels:
                # print(l," ",r," ",s[l]," ",s[r])
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # print(s)
        return ''.join(s)