class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for char in s:
            if char.isalnum():
                if char.isalpha():
                    char = char.lower()
                ls.append(char)
        print(ls)

        l = 0
        r = len(ls) - 1

        while l <= r:
            if ls[l] != ls[r]:
                return False
            l = l + 1
            r = r - 1

        return True
