class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        temp = [0] * n 
        for l, r in queries:
            temp[l] += 1
            if r + 1 < n:
                temp[r + 1] -= 1
        
        for i in range(1, n):
            temp[i] += temp[i - 1]
        
        cond = True
        for i in range(n):
            if nums[i] > temp[i]:
                cond = False
        
        return cond
