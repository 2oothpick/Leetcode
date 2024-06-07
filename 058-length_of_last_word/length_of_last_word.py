class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # method chaining learnt from js
        return len(s.strip().split(' ')[-1])
