class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        for i in range(len(s)):
            if s[i].isalnum():
                p=p+s[i].lower()
        if p==p[::-1]:
            return True
        else:
            return False
        