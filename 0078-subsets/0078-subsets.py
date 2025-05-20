class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tot = 1 << n
        result = []
        for i in range(tot):
            ss = []
            for j in range(n):
                if i & (1 << j):
                    ss.append(nums[j])
            result.append(ss)
        
        return result




