class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0
        sumArr = []
        for i in accounts:
            for j in i:
                sum += j
            sumArr.append(sum)
            sum = 0
        sumArr.sort()
        return sumArr[-1]
