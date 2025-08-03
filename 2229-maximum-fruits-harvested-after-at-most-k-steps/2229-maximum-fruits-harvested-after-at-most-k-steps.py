class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        sum_ = [0] * (n + 1)
        inds = [0] * n
        res = 0

        for i in range(n):
            sum_[i + 1] = sum_[i] + fruits[i][1]
            inds[i] = fruits[i][0]

        for x in range(k // 2 + 1):
            y = k - 2 * x
            l = startPos - x
            r = startPos + y
            start = bisect_left(inds, l)
            end = bisect_right(inds, r)
            res = max(res, sum_[end] - sum_[start])

            l = startPos - y
            r = startPos + x
            start = bisect_left(inds, l)
            end = bisect_right(inds, r)
            res = max(res, sum_[end] - sum_[start])

        return res
        