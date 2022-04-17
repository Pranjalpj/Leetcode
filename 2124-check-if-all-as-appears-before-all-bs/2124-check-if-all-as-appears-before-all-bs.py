class Solution:
    def checkString(self, s: str) -> bool:
        e=list()
        f=list()
        for i in range(len(s)):
            if s[i]=="a":
                e.append(i)
            else:
                f.append(i)
        if len(e)==0 or len(f)==0:
            return True
        elif e[-1]>f[0]:
            return False
        else:
            return True
                
        