class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i+1, n-1):
                for k in range(j + 1, n):
                    curr = (nums[i] - nums[j]) * nums[k]
                    result = max(result, curr)
        return result