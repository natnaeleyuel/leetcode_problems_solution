class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = set()
        n = len(nums)
        for i in range(n - 1, - 1, - 1):
            if nums[i] not in distinct:
                distinct.add(nums[i])
            else:
                return math.ceil((i + 1) / 3)
        return 0