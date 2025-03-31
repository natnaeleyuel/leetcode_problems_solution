class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        
        freq = {}
        cursum = 0
        maxsum = 0
        
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            cursum += nums[i]
        
        if len(freq) == k:
            maxsum = cursum
        
        for i in range(k, n):
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]
            
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            cursum += nums[i] - nums[i - k]
            
            if len(freq) == k:
                maxsum = max(maxsum, cursum)
        
        return maxsum if maxsum > 0 else 0
