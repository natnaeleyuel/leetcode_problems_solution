class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    result += 1

        return result