class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        count = [0] * 26
        count2 = [0] * 26

        for i in s:
            count[ord(i) - ord('a')] += 1

        for j in t:
            count[ord(j) - ord('a')] -= 1

        return count == count2
