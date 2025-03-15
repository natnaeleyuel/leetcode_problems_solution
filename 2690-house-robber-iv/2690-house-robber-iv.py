class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward = 1
        max_reward = max(nums)
        while min_reward < max_reward:
            mdr = (max_reward + min_reward) // 2
            possible = 0
            l = 0
            while l < len(nums):
                if nums[l] <= mdr:
                    possible += 1
                    l += 2
                else:
                    l += 1
            
            if possible >= k:
                max_reward = mdr
            else:
                min_reward = mdr + 1
        
        return min_reward
