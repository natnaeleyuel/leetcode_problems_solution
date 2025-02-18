class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0]*len(nums)
        for q in range(len(requests)):
            l = requests[q][0]
            r = requests[q][1]
            prefix_sum[l] += 1
            if r < len(nums) - 1:
                prefix_sum[r+1] -= 1
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        
        nums.sort()
        prefix_sum.sort()
        result = 0
        for i in range(len(nums)):
            result += nums[i] * prefix_sum[i]
        
        return result % (10**9 + 7)