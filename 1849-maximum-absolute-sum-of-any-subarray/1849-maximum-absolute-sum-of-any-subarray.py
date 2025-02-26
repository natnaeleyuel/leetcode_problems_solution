class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        curr_max = 0
        curr_min = 0
        
        for num in nums:
            curr_max += num
            curr_min += num       
            res = max(res, abs(curr_max), abs(curr_min))
            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0
        
        return res
