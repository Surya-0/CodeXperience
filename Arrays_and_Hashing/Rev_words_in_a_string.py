class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l = l[-1:-len(l)-1:-1]
        res = ' '.join(l)
        print(l)

        return res