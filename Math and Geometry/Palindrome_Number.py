class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        else:
            num = x
            no_digits = len(str(x))
            rev = 0
            while no_digits != 0:
                temp = x % 10
                x = x // 10
                rev = rev * 10 + temp
                no_digits -= 1

            # print(rev)
            return num == rev
