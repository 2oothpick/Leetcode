class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            temp = x
            x = list(str(x))
            x.reverse()
            newStr = ""
            for item in x:
                newStr += item
            return int(newStr) == temp
        return False
