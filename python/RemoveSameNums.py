class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return len(nums)
        copy = nums.copy()
        for i in range(len(copy)-1):
            if copy[i]==copy[i+1]:
                nums.remove(copy[i])
        return len(nums)

================================

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        a = None
        for num in nums:
            if num!=a:
                nums[i]=num
                a=num
                i +=1
        return i
