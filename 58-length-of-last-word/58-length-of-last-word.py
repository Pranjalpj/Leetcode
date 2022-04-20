import string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v=s[::-1]
        c=""
        for i in range(len(v)):
            if v[i]==" ":
                continue
            else:
                c=v[i:]
                break
        c=c[::-1]
        t=c.split(" ")
        return len(t[-1])
        