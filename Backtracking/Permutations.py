class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            print("The val of n : ", n)
            print("The value of the nums is : ", nums)
            perms = self.permute(nums)
            print("The perms is : ", perms)
            print(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            print("The result is : ", result)
            nums.append(n)

        return result
