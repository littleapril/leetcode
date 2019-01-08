class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = ''
        if len(strs) == 0:
            return str
        min = len(strs[0])
        for i in range(len(strs)):
            if len((strs[i]))<min:
                min = len((strs[i]))
        
        for j in range(min):
            a = []
            for i in range(len((strs))):
                a.append(strs[i][j])
            if len(set(a)) == 1:
                str +=a[0]
            else:
                break
        return str
