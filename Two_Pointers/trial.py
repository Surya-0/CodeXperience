# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new = ""
#         for i in s:
#             if i.isalnum():
#                 new += i.lower()
#
#         l = 0
#         r = len(new) - 1
#         while l <= r:
#             if new[l] == new[r]:
#                 l += 1
#                 r -= 1
#             else:
#                 return False
#
#         return True

l = [11,12,13,14,15,16,17,18,19,20]
for i,val in enumerate(l):
    print(i," ",val)
