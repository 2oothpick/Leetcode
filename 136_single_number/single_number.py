class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for item in nums:
            answer ^= item
        return answer
