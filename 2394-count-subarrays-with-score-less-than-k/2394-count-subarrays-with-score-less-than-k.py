class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        curr = 0
        left = 0
        for right in range(n):
            curr += nums[right]
            while left <= right and curr * (right - left + 1) >= k:
                curr -= nums[left]
                left += 1
            result += right - left + 1
        
        return result
