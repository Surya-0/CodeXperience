class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hasher_1 = {}
        for i in ransomNote:
            hasher_1[i] = 1 + hasher_1.get(i, 0)

        for j in magazine:
            if j in hasher_1:
                hasher_1[j] -= 1

        for k in hasher_1:
            if hasher_1[k] <= 0:
                continue
            else:
                return False
        return True


