class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        u=list()
        y=list()
        for i in nums:
            if i%2==0:
                u.append(i)
            else:
                y.append(i)
        return u+y
        