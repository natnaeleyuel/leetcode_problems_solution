class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        ss = nums[::]
        ps = nums[::]
        for i in range(1, n):
            ps[i] += ps[i-1]
        
        for i in range(n-2, -1, -1):
            ss[i] += ss[i+1]
        
        for i in range(n):
            if i == 0:
                if ss[i+1] == 0:
                    return 0
            elif i != n - 1:
                if ps[i-1] == ss[i + 1]:
                    return i
            elif i == n - 1:
                if ps[i - 1] == 0:
                    return n - 1

        return -1