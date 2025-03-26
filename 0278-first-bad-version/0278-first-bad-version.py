class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            num = (left + right) // 2
            if isBadVersion(num):
                right = num - 1
            else:
                left = num + 1
        return left