class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = "0b" + a
        b = "0b" + b
        result = int(a, base=2) + int(b, base=2)
        output = str(bin(result))[2:]
        return output
