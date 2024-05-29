class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count_arr = [0] * 26
        res = 0
        while r < len(s):
            count_arr[ord(s[r]) - 65] += 1
            # print(l," ",r," ",res," ",(r-l+1) -max(count_arr))
            while (r - l + 1) - max(count_arr) > k:
                count_arr[ord(s[l]) - 65] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res