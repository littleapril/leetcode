class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(s)%2 !=0:
            return False
        d = {'(':')','{':'}','[':']'}
        l = []
        for i in s:
            if i in d.keys():
                l.append(i)
            else:
                if len(l)==0 or d[l[-1]] != i:
                    return False
                else:
                    l.pop()
        if len(l)==0:
            return True
        else:
            return False
