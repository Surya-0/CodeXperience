class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.s = s

        def check_pairs(pair, score):
            res = 0
            stack = []
            for c in self.s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score

                else:
                    stack.append(c)

            self.s = ''.join(stack)
            return res

        res = 0
        pair = "ab" if x > y else "ba"
        res += check_pairs(pair, max(x, y))
        res += check_pairs(pair[::-1], min(x, y))

        return res