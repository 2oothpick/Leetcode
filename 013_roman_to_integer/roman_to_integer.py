class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        store = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

        for idx in range(0, len(s)):
            for i in range(idx + 1, len(s)):
                if i == idx + 1:
                    print(idx, i)
                    # subtractive bit: next > current
                    if store[s[i]] > store[s[idx]]:
                        sum -= store[s[idx]]
                    else:
                        sum += store[s[idx]]
        sum += store[s[-1]]
        return sum
