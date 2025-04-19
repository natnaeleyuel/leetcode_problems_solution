class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        left = n - 1
        right = n - 1
        for i in range(n):
            while right >= 0 and nums[i] + nums[right] > upper:
                right -= 1
            while left >=0 and nums[i] + nums[left] >= lower:
                left -= 1
            if left < i and right >= i:
                result += right - left - 1
            else:
                result += right - left
        return result // 2