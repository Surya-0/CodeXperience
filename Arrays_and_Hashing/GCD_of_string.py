class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1

        # if str2 not in str1 or set(str1) != set(str2):
        #     return ""

        def euclidean(n1, n2):
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1

        l1 = len(str1)
        l2 = len(str2)

        sl = euclidean(l1, l2)

        f1 = l1 // sl
        f2 = l2 // sl

        res = str1[:sl]

        if res * f1 != str1 or res * f2 != str2:
            return ""

        return res
