class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            cur_sum = 0
            left = 0
            result = 0
            for right in range(len(nums)):
                cur_sum += nums[right]
                while cur_sum > x:
                    cur_sum -= nums[left]
                    left += 1
                
                result += right - left + 1
            return result
        
        return helper(goal) - helper(goal - 1)