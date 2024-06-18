from collections import deque


class Solution:
    def jump(self, nums: 'List[int]') -> int:
        temp_q = deque()
        visit = set()
        temp_q.append((0, 0))
        while temp_q:
            ind, moves = temp_q.popleft()
            for i in range(1, nums[ind] + 1):
                new_ind = ind + i
                if new_ind == len(nums) - 1:
                    return moves + 1
                if new_ind not in visit and new_ind < len(nums) - 1:
                    temp_q.append((new_ind, moves + 1))
                    visit.add(new_ind)

        return 0
