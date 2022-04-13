class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(0,len(nums)):
            for i in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
                else:
                    continue
        
                
                    
        