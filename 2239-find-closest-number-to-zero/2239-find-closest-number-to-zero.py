class Solution(object):
    def findClosestNumber(self, nums):
        result = [[-abs(n), n] for n in nums]
        return max(result)[1]

