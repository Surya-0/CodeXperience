class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_str = s + s
        return s in doubled_str[1:-1]