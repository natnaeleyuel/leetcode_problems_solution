class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return math.ceil((i + 1) / 3)
            seen.add(nums[i])
        return 0