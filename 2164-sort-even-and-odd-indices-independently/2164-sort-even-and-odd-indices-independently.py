class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = nums[1::2]
        odd.sort(reverse=True)
        even = nums[::2]
        even.sort()
        for i in range(len(nums)):
            if i&1 :
                nums[i] = odd[(i-1)//2]
            else:
                nums[i] = even[i//2]
        return nums