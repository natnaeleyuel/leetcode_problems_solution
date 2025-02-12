class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        holder = 0
        seek = 1
        while seek < len(nums):
            if nums[seek] != 0 and nums[holder] == 0:
                nums[holder], nums[seek],  = nums[seek], nums[holder]
                holder += 1
            elif nums[holder] != 0:
                holder += 1
                
            seek += 1
            
        return nums
            

        