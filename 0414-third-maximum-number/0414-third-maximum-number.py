class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        return nums[-3] if len(nums) >= 3 else max(nums)