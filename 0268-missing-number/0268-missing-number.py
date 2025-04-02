class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (max(nums) + 1)
        for i in range(len(nums)):
            arr[nums[i]] = nums[i]
        
        for i in range(len(arr)):
            if arr[i] == -1:
                return i 
        
        return len(nums)