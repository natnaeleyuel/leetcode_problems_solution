class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        diff = 0
        max_num = 0
        n = len(nums)
        
        for i in range(n):
            result = max(result, diff * nums[i])
            diff = max(diff, max_num - nums[i])
            max_num = max(max_num, nums[i])

        return result