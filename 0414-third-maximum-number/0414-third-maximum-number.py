class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        return nums[-3] if len(nums) >= 3 else max(nums)
        