class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        v=s.split(" ")
        f=list()
        for i in v:
            if i.isnumeric():
                f.append(int(i))
        t=sorted(list(set(f)))
        if t==f:
            return True
        else:
            return False
        