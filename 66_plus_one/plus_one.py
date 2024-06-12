class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        for item in digits:
            string += str(item)
        string = int(string)
        string += 1
        string = list(str(string))
        for idx in range(len(string)):
            string[idx] = int(string[idx])
        return string
