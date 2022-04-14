class Solution:
    def reverseWords(self, s: str) -> str:
        v=s.split(" ")
        r=""
        for i in v:
            r=r+ " " +i[::-1]
        return r.lstrip()
        