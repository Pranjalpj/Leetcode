class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1=list()
        for i in nums1:
            if i in nums2:
                a1.append(i)
        return list(set(a1))
        
        