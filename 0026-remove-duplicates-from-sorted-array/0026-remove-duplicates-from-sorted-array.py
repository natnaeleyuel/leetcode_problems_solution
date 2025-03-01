class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[n] = nums[i]
                n += 1
        
        return n
            