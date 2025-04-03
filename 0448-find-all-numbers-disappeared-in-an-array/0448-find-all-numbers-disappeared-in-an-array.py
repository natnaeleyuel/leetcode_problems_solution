class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_num = set(range(1, n + 1))

        for i in range(n):
            all_num.discard(nums[i])

        return list(all_num)