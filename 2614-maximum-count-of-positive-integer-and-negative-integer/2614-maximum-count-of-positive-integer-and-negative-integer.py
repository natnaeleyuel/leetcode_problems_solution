class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]
        return max(len(pos), len(neg))