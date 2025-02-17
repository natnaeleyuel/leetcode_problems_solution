class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  
        prefix_sum = 1
        for i in range(n):
            result[i] = prefix_sum
            prefix_sum *= nums[i]
            
        suffix_sum = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_sum
            suffix_sum *= nums[i]

        return result