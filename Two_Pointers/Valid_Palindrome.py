class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ""
        for char in s:
            if char.isalnum():
                if char.isalpha():
                    char = char.lower()
                string+=char
        print(string)
        l = 0
        r = len(string) - 1
        if string == "":
            return True
        else:
            while l<= r:
                if string[l] == string[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

