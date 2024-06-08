class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for idx, value in enumerate(nums):
            for idx1, value1 in enumerate(nums[idx + 1 :]):
                if value + value1 == target:
                    ans.extend([idx, nums.index(value1, idx + 1)])
        return ans
