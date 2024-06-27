class Solution:
    def largestAltitude(self, gain: 'List[int]') -> int:
        length = len(gain) + 1
        prefix_arr = [0] * length

        for i in range(len(gain)):
            prefix_arr[i + 1] = prefix_arr[i] + gain[i]

        # print(prefix_arr)
        return max(prefix_arr)