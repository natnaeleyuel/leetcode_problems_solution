class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(nums, ind, curr):
            if ind == len(nums):
                return curr
            
            xor1 = backtrack(nums, ind + 1, curr ^ nums[ind])
            xor2 = backtrack(nums, ind + 1, curr)

            return xor1 + xor2
        
        return backtrack(nums, 0, 0)