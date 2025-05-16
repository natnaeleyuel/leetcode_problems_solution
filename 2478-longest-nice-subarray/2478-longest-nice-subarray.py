class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        result = 0
        curr = 0
        for r in range(len(nums)):
            num = nums[r]
            while curr & num:
                curr ^= nums[l]
                l += 1
            result = max(result, r - l + 1)
            curr |= num
        return result
                
            
