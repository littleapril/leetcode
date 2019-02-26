class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if nums[-1]<target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]<target:
                continue
            else:
                return i
                
==========================================================

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left<right:
            mid = left+(right-left)//2
            if nums[mid]>target:
                right = mid
            elif nums[mid]<target:
                left = mid + 1
            else:
                return mid
        return left
    
