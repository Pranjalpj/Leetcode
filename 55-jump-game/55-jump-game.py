class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums==[0]:
            return True
        if nums[0]==0:
            return False
        if 0 not in nums:
            return True
        reachable=0
        for i in range(len(nums)):
            if reachable<i:
                return False
            reachable=max(reachable,nums[i]+i)
        return True
                
        