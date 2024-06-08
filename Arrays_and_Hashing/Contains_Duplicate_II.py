class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        l = 0
        r = 0
        s = set()
        while r < len(nums):
            # print(s)
            if r - l <= k:
                if nums[r] not in s:
                    s.add(nums[r])
                    r += 1
                else:
                    return True

            else:
                s.remove(nums[l])
                l += 1

        return False

