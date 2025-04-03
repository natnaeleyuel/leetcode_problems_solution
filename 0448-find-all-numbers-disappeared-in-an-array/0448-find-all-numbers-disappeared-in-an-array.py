class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_nums = set(range(1, n + 1))

        for i in range(n):
            all_nums.discard(nums[i])

        return list(all_nums)