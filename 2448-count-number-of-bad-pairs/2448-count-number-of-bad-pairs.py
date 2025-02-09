class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        countBadPairs = Counter()
        result = 0
        for i, val in enumerate(nums):
            result += i - countBadPairs[i - val]
            countBadPairs[i - val] += 1

        return result