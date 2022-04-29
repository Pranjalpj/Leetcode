class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a1=list()
        a2=list()
        for i in nums1:
            if i in nums2:
                continue
            else:
                a1.append(i)
        for i in nums2:
            if i in nums1:
                continue
            else:
                a2.append(i)
        return list(set(a1)),list(set(a2))
        