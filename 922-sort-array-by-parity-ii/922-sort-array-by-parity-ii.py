class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=list()
        odd=list()
        final=list()
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(odd)):
            final.append(even[i])
            final.append(odd[i])
        return final
        