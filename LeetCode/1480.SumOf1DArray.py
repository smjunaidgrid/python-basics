class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        add = 0
        for i in nums:
            add += i
            result.append(add)
        return result
        