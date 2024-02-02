# 75. Sort colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer method (注意是current和right做比較)
        left = 0
        right = len(nums)-1
        current = 0
        while current <= right:
            if nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right-=1
            elif nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left+=1
                current+=1
            else:
                current+=1