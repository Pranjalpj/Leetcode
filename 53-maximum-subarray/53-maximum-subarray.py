class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=0
        if min(nums)>0 and max(nums)>0:
            return sum(nums)
        if min(nums)<0 and max(nums)<0:
            return max(nums)
        if len(nums)==1:
            return nums[0]
        for i in range(0,len(nums)):
            current_sum=current_sum+nums[i]
            if max_sum<current_sum:
                max_sum=current_sum
            if current_sum<0:
                current_sum=0
        return max_sum
        