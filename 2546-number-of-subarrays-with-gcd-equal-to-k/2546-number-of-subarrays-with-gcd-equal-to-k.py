class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr == k:
                res += 1

            for j in range(i + 1, n):
                curr = gcd(nums[j], curr)
                if curr == k:
                    res += 1
        
        return res
