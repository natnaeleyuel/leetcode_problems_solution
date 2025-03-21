class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(ind):
            if ind == len(nums):
                result.append(nums[:])
                return
            
            for i in range(ind, len(nums)):
                nums[ind], nums[i] = nums[i], nums[ind]
                backtrack(ind + 1)
                nums[ind], nums[i] = nums[i], nums[ind]
        
        backtrack(0)
        return result