class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(len(nums)):
            a = target - nums[i]

            if a in d:
                return [d[a], i]

            d[nums[i]] = i


# C++ solution
"""
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> d;
        for(int i =0;i < nums.size();i++){
            int rem = target - nums[i];
            if (d.find(rem) != d.end()){
                return {d[rem],i};
            }
            d[nums[i]] = i;
        }
        return {};
    }
};
"""
