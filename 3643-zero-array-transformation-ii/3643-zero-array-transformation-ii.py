class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        l, r = 0, len(queries)

        if not self.check(nums, queries, r):
            return -1

        while l <= r:
            m = l + (r - l) // 2
            if self.check(nums, queries, m):
                r = m - 1
            else:
                l = m + 1

        return l

    def check(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)
        tot = 0
        diff = [0] * (n + 1)

        for i in range(k):
            start, end, val = queries[i]

            diff[start] += val
            diff[end + 1] -= val

        for i in range(n):
            tot += diff[i]
            if tot < nums[i]:
                return False
        return True
