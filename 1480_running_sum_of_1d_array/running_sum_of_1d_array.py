class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        newnums = []
        for rsum in nums:
            sum += rsum
            newnums.append(sum)
        return newnums
