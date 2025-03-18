class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        result = 0
        temp = 0
        for i in range(len(nums)):
            num = nums[i]
            while temp & num:
                temp ^= nums[left]
                left += 1
            result = max(result, i - left + 1)
            temp |= num
        return result
                
            
