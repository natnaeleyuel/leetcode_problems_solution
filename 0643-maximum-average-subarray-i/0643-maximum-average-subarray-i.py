class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_aver = cur_sum / k
        
        for right in range(k, len(nums)):
            cur_sum = cur_sum + nums[right] - nums[right-k]
            cur_aver = cur_sum / k
            max_aver = max(max_aver, cur_aver)
        
        return max_aver
