class Solution:
    def sumZero(self, n: int) -> List[int]:
        final=list()
        if n==0:
            final.append(0)
            return final
        if n%2==0:
            for i in range(1,(n//2)+1):
                final.append(i)
                final.append(0-(i))
        elif n%2!=0:
            for i in range(1,(n//2)+1):
                final.append(i+1)
                final.append(0-(i+1))
            final.append(0)
        return final
            
        