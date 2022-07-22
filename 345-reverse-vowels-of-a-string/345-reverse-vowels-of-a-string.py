class Solution:
    def reverseVowels(self, s: str) -> str:
        f=["a","e","i","o","u","A","E","I","O","U"]
        v=""
        t=""
        g=""
        for i in s:
            if i in f:
                v=v+i
                t=t+"*"
            else:
                t=t+i
        v=v[::-1]
        j=0
        for i in t:
            if i=="*" and j!=len(v):
                g=g+v[j]
                j+=1
            else:
                g=g+i
        return g
                
                
        