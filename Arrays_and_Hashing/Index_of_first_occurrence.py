class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        substr_map = {haystack[i:i + len(needle)]: i for i in range(len(haystack) - len(needle) + 1)}

        return substr_map.get(needle, -1)