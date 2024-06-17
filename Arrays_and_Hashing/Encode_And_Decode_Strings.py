class Solution:
    def encode(self, strs: 'List[str]') -> str:
        if len(strs) == 0:
            return ""
        delimiter = "$"
        temp = ""
        for i in strs:
            temp += str(len(i)) + delimiter + i

        return temp

    def decode(self, s: str) -> 'List[str]':
        if not s:
            return []

        res = []
        delimiter = "$"
        i = 0
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        return res