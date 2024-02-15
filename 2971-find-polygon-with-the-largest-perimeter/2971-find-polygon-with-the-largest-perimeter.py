class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        perimeter=0
        maxi=-1
        for i in range(len(nums)):
            if i>=2 and nums[i]<perimeter:
                maxi=perimeter+nums[i]
            perimeter+=nums[i]
        return maxi