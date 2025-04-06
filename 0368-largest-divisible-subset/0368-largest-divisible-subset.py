class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        ms = 1
        mi = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > ms:
                        ms = dp[i]
                        mi = i
        result = []
        num = nums[mi]
        for i in range(mi, - 1, - 1):
            if num % nums[i] == 0 and dp[i] == ms:
                result.append(nums[i])
                num = nums[i]
                ms -= 1
        
        return result