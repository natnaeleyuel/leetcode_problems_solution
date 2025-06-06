class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = 0
        result = [-1] * (n - k + 1)
        for right in range(n):
            if right > 0 and nums[right - 1] + 1 != nums[right]:
                left = right
            if right - left + 1 >= k:
                result[right - (k - 1)] = nums[right]
        
        return result
