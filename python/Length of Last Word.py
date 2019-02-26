class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        else:
            return len(s.split(" ")[-1])
          
==================================================

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1
        while i>=0:
            if s[i]==' ':
                n -=1 
                i -=1
            else:
                break
        if n==0:
            return 0
        start=0
        for j in range(n):
            if s[j]==' ':
                start = j+1
        return n-start
