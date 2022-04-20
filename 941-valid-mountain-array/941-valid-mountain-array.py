class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        j=1
        while(j<len(arr) and arr[j]>arr[j-1]):
            j+=1
        if j==len(arr):
            return False
        while(j!=1 and j<len(arr) and arr[j]<arr[j-1]):
            j+=1
        if j==len(arr):
            return True
        else:
            return False
            
        